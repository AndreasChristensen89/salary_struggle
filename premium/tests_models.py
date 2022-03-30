from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from .models import Order, OrderItem
import tempfile


class TestOrder(TestCase):
    """ tests to test the item model """

    def test_item_object_exists(self):
        """ test if object is created """

        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')
        Order.objects.create(
            user_profile=Profile.objects.get(user=new_user),
            full_name='random guy',
            email='mosh@email.com',
        )
        self.assertEqual(Order.objects.all().count(), 1)
        self.assertEqual(len(Order.objects.get(full_name="random guy").order_number), 32)
