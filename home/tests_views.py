from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    """
    Test all html pages for the codex
    """

    def test_index_page(self):
        """ Test index page """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_contact_page(self):
        """
        Tests contact page
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_contact_page_logged_in(self):
        """
        Tests contact page for logged in users
        """
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/contact-user/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact_login.html')
        self.assertTemplateUsed(response, 'base.html')
