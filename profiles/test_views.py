from django.test import TestCase
from shop.models import Product
from django.urls import reverse
from profiles.models import Profile, ActiveCharacter
from django.contrib.auth.models import User


class TestProfileViews(TestCase):

    """
    Test all pages for the shop navigation
    """

    def test_profile_page(self):
        """ Test products page """

        Product.objects.create(name='Premium Membership', price=1)
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        
        self.client.login(username='john', password='johnpassword')

        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profiles.html')
        self.assertTemplateUsed(response, 'base.html')

    # def test_restart_character(self):
    #     """
    #     Test if character is restarts
    #     """
    #     new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    #     ActiveCharacter.create_new_character(new_user)
    #     ActiveCharacter.objects.filter(user=new_user).update(day=10)
    #     response = self.client.get('/profile/new_character/')

    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(ActiveCharacter.objects.filter(day=1).count(), 1)

    def test_update_profile(self):
        """
        Tests if profile is updated
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
    
        response = self.client.post(
            reverse('update_profile'),
            {'username': 'tester',
             'first_name': 'test',
             'last_name': 'testtwo',
             'email': 'lennon@thebeatles.com'})
        new_user.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_user.username, 'tester')
