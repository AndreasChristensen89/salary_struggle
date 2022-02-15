from django.test import TestCase
from .models import Order, OrderItem
import tempfile


class TestOrder(TestCase):
    """ tests to test the item model """

    def test_item_object_exists(self):
        """ test if object is created """
        Order.objects.create(
            order_number='12345678',
            full_name='random guy',
            email='mosh@email.com',
            phone_number=12345678,
            country='Macedonia',
            postcode=12345,
            town_or_city='schzlechic',
            street_address1='schzlechic main 34',
        self.assertEqual(Order.objects.all().count(), 1)
