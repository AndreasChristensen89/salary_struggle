from django.test import TestCase
from .forms import ProfileForm


class TestProfileForm(TestCase):
    """
    Tests for form for users not logged in
    """

    def test_empty_form(self):
        """
        Tests that empty form is not valid
        """
        form = ProfileForm()
        self.assertFalse(form.is_valid())

    def test_form_with_no_username_field(self):
        """
        Tests that username field is required
        """

        form = ProfileForm({'username': ''})
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')
        self.assertFalse(form.is_valid())

    def test_form_with_no_first_name_field(self):
        """
        Tests that first_name is required
        """

        form = ProfileForm({
            'username': 'test',
            'first_name': ''
            })
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0],
                         'This field is required.')
        self.assertFalse(form.is_valid())

    def test_form_with_no_last_name_field(self):
        """
        Tests that last name is required
        """

        form = ProfileForm({
            'username': 'test',
            'first_name': 'mosh@email.com',
            'last_name': ''
            })
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0],
                         'This field is required.')
        self.assertFalse(form.is_valid())

    def test_form_with_no_email_field(self):
        """
        Tests that email is required
        """

        form = ProfileForm({
            'username': 'test',
            'first_name': 'mosh@email.com',
            'last_name': 'tester',
            'email': ''
            })
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
        self.assertFalse(form.is_valid())

    def test_form_with_non_email(self):
        """
        Tests that email needs to be correct
        """

        form = ProfileForm({
            'username': 'test',
            'first_name': 'mosh@email.com',
            'last_name': 'tester',
            'email': 'moshmosh.com'
            })
        self.assertFalse(form.is_valid())
