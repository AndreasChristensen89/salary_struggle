from django.db import models
import random
import string


class Product(models.Model):
    """ Model for products"""

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Overrides save method to set alphanumeric sku
        Generate code taken from stackover:
        https://stackoverflow.com/questions/2511222/efficiently-generate-a-16-character-alphanumeric-string
        """
        if not self.sku:
            sku = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
            self.sku = sku
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
