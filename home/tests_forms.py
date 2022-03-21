from django.test import TestCase
from .forms import ContactForm, ContactFormLoggedin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class TestContactForm(TestCase):
    """
    Tests for form for users not logged in
    """

    def test_empty_form(self):
        """
        Tests that empty form is not valid
        """
        form = ContactForm()
        self.assertFalse(form.is_valid())

    def test_form_with_no_name_field(self):
        """
        Tests that name field is required
        """

        form = ContactForm({'name': ''})
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertFalse(form.is_valid())

    def test_form_with_no_email_field(self):
        """
        Tests that email is required
        """

        form = ContactForm({
            'name': 'test',
            'email_address': ''
            })
        self.assertIn('email_address', form.errors.keys())
        self.assertEqual(form.errors['email_address'][0], 'This field is required.')
        self.assertFalse(form.is_valid())

    def test_form_with_no_message_field(self):
        """
        Tests that message is required
        """

        form = ContactForm({
            'name': 'test',
            'email_address': 'mosh@email.com',
            'message': ''
            })
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')
        self.assertFalse(form.is_valid())

    def test_form_with_non_email(self):
        """
        Tests that email needs to be correct
        """

        form = ContactForm({
            'name': 'name',
            'email_address': 'mosh.com',
            'message': 'Hi'
            })
        self.assertFalse(form.is_valid())


class TestContactFormLogin(TestCase):
    """
    Tests for contact form for logged in users
    """

    def test_empty_form(self):
        """
        Tests that empty form is not validated
        """

        form = ContactFormLoggedin()
        self.assertFalse(form.is_valid())

    def test_form_with_no_message_field(self):
        """
        Tests that message field is required
        """

        form = ContactFormLoggedin({'message': ''})
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')
        self.assertFalse(form.is_valid())
