from django.test import TestCase
from .models import Product


class TestProductModel(TestCase):
    """ tests for the product model """

    def test_product_object_exists_and_sku_generated(self):
        """ test if object is created """
        product = Product.objects.create(
            name='test',
            price=500,)
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertEqual(len(product.sku), 8)
