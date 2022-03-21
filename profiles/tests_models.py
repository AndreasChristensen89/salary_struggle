from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, ActiveCharacter


class TestProfileForm(TestCase):
    """ tests to test the profile model """

    def test_profile_object_exists(self):
        """ test if object is created """

        User.objects.create_user('John', 'lennon@thebeatles.com', 'johnpassword')
        self.assertEqual(Profile.objects.all().count(), 1)

    def test_profile_class_works(self):
        """ test if Profile class method sets active character to False """

        new_user = User.objects.create_user('John', 'lennon@thebeatles.com', 'johnpassword')
        Profile.objects.filter(user=new_user).update(active_char=True)
        Profile.remove_active_char(new_user)
        self.assertEqual(Profile.objects.filter(active_char=False).count(), 1)


class TestActiveCharacter(TestCase):
    """ test the ActiveCharacter model """

    def test_active_character_model_works(self):
        """ test if object is created """

        new_user = User.objects.create_user('John', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.objects.create(
            user=new_user,
        )
        self.assertEqual(ActiveCharacter.objects.all().count(), 1)

    def test_active_character_class_method(self):
        """ test if the class method updates the user """
        new_user = User.objects.create_user('John', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.assertEqual(Profile.objects.filter(active_char=True).count(), 1)
