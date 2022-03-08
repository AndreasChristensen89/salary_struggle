import uuid     # to generate order number

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from shop.models import Product
from profiles.models import Profile


class Order(models.Model):
    """
    Class for instances of orders
    Linked to OrderItem class, which handles totals
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, 
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    # original_bag added to keep track of individual bags to avoid duplicates,
    # as customers can purchase the same things multiple times


    def _generate_order_number(self):
        """
        Private method, generates a unique order number
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates grand total when item is added, accounting for delivery costs.
        Uses Sum() across all items
        """
        self.order_total = self.orderitems.aggregate(Sum('item_total'))['item_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Overrides save method to set the order number,
        if not set already, bu using method above
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """
    Class that iterates through every item from an order instance,
    attaches it to the order, and updates the delivery costs and total
    """

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Overrides save method to set the item_total,
        and update the order_total in the Order class
        """
        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
