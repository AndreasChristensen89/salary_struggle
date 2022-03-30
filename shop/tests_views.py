from django.test import TestCase
from django.contrib.auth.models import User

from .models import Product


class TestNavigationViews(TestCase):

    """
    Test all pages for the shop navigation
    """

    def test_product_page(self):
        """ Test products page """
        User.objects.create_user('john', 'lennon@thebeatles.com',
                                 'johnpassword')
        self.client.login(username='john', password='johnpassword')

        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/products.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_product_detail_page(self):
        """
        Tests product detail page
        """

        User.objects.create_user('john', 'lennon@thebeatles.com',
                                 'johnpassword')
        self.client.login(username='john', password='johnpassword')

        Product.objects.create(name='name', price=1)

        response = self.client.get('/shop/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product_details.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_edit_product_page(self):
        """
        Tests edit product page
        """

        Product.objects.create(name='name', price=1)

        User.objects.create_superuser('superuser', 'superuser@admin.com',
                                      'adminpass')
        self.client.login(username='superuser', password='adminpass')
        response = self.client.get('/shop/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/edit_product.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_add_product_page(self):
        """
        Tests Add product page
        """

        User.objects.create_superuser('superuser', 'superuser@admin.com',
                                      'adminpass')
        self.client.login(username='superuser', password='adminpass')
        response = self.client.get('/shop/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/add_product.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_delete_product_page(self):
        """
        Tests if product is deleted
        """

        Product.objects.create(name='name', price=1)

        User.objects.create_superuser('superuser', 'superuser@admin.com',
                                      'adminpass')
        self.client.login(username='superuser', password='adminpass')
        self.client.get('/shop/delete/1/')
        self.assertEqual(Product.objects.count(), 0)
