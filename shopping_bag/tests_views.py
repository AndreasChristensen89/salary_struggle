from django.test import TestCase
from django.contrib.auth.models import User
from shop.models import Product
from .contexts import shopping_bag_contents


class TestViews(TestCase):
    """
    Test shopping bag
    """

    def test_contact_page_logged_in(self):
        """
        Tests shopping bag page
        """
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/shopping_bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_bag/shopping_bag.html')
        self.assertTemplateUsed(response, 'base.html')

    # def test_add_to_bag(self):
    #     """
    #     Tests if item is added to bag
    #     """
    #     Product.objects.create(name='test', price='100')
    #     User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    #     self.client.login(username='john', password='johnpassword')

    #     response = self.client.get('/shopping_bag/add/1/')

    #     # current_bag = shopping_bag_contents(response.context['user'])

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(current_bag.items().count(), 1)
