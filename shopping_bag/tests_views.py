from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    """
    Test shopping bag
    """

    def test_shopping_bag_page(self):
        """
        Tests shopping bag page
        """
        User.objects.create_user('john', 'lennon@thebeatles.com',
                                 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/shopping_bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_bag/shopping_bag.html')
        self.assertTemplateUsed(response, 'base.html')
