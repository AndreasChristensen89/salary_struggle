from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """
    Tests for product form
    """

    def test_empty_form(self):
        """
        Tests that empty form is not valid
        """
        form = ProductForm()
        self.assertFalse(form.is_valid())

    def test_form_with_no_name_field(self):
        """
        Tests that name field is required
        """

        form = ProductForm({'name': ''})
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertFalse(form.is_valid())

    def test_form_with_no_email_field(self):
        """
        Tests that price field is required
        """

        form = ProductForm({
            'name': 'test',
            'price': ''
            })
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')
        self.assertFalse(form.is_valid())

    def test_form_with_wrong_type(self):
        """
        Tests that price needs to be correct type
        """

        form = ProductForm({
            'name': 'test',
            'price': 'fire'
            })
        self.assertFalse(form.is_valid())
