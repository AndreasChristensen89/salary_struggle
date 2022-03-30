from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    """
    Allows us to add and edit line items from inside the order model
    When we see an order we see the list of editable items on same page
    """
    model = OrderItem
    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin class. Readonly fields so that they're not edited.
    Inlines to allow other class to edit
    """

    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'order_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
