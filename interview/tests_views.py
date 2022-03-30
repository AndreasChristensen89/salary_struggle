import tempfile
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import ActiveCharacter
from codex.models import Interviewer

# Create your tests here.


class TestNavigationViews(TestCase):

    """
    Test all interview pages
    """

    def test_hr_interview(self):
        """ Test hr interview is functional """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(level=2)
        Interviewer.objects.create(name="test", level=1,
                                   image=tempfile.
                                   NamedTemporaryFile(suffix=".jpg").name)
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/interview/hr-interview/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interview/hr_interview.html')
        self.assertTemplateUsed(response, 'grind/game_base.html')

    def test_coding_interview(self):
        """ Test hr interview is functional """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(level=3)
        Interviewer.objects.create(name="test", level=2,
                                   image=tempfile.
                                   NamedTemporaryFile(suffix=".jpg").name)
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/interview/coding-interview/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interview/coding_interview.html')
        self.assertTemplateUsed(response, 'grind/game_base.html')

    def test_coding_difficult_interview(self):
        """ Test hr interview is functional """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(level=4)
        Interviewer.objects.create(name="test", level=3,
                                   image=tempfile.
                                   NamedTemporaryFile(suffix=".jpg").name)
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/interview/difficult-coding-interview/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'interview/coding_difficult_interview.html')
        self.assertTemplateUsed(response, 'grind/game_base.html')

    def test_final_interview(self):
        """ Test hr interview is functional """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(level=5)
        Interviewer.objects.create(name="test", level=4,
                                   image=tempfile.
                                   NamedTemporaryFile(suffix=".jpg").name)
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/interview/final-interview/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interview/final_interview.html')
        self.assertTemplateUsed(response, 'grind/game_base.html')


class TestPassInterviewTestCase(TestCase):
    """
    Test all pages to upgrade character
    """

    def test_pass_interview(self):
        """
        Tests if character's level goes up
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        response = self.client.post(
            '/interview/interview-success/',
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.level == 2)
