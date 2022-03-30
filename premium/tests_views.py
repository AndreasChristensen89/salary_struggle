from django.test import TestCase
from premium.models import Order
from profiles.models import Profile
from django.contrib.auth.models import User
from django.conf import settings


class TestLeaderboardViews(TestCase):
    """
    Test all pages for the shop navigation
    """

    def test_checkout_page(self):
        """
        Tests if checkout page load
        """

        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')

        self.client.login(username='john', password='johnpassword')

        Order.objects.create(
            user_profile=Profile.objects.get(user=new_user),
            full_name='random guy',
            email='lennon@thebeatles.com',
        )
        order_number = Order.objects.get(full_name="random guy").order_number

        response = self.client.get(f'/premium/checkout/{order_number}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premium/checkout.html')
        self.assertTemplateUsed(response, 'base.html')
