from django.test import TestCase
from .models import Leaderboard
from django.contrib.auth.models import User
from profiles.models import ActiveCharacter


class TestLeaderboardModel(TestCase):
    """ tests for the the leaderboard model """

    def test_leaderboard_object_exists(self):
        """ test if object is created """
        
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        
        self.client.login(username='john', password='johnpassword')
        Leaderboard.objects.create(
            user=user,
            char_intellect=1,
            char_charm=1,
            char_coding=1,
            char_endurance=1,
            char_money=1,
            char_day=1
            )
        self.assertEqual(Leaderboard.objects.all().count(), 1)

    def test_active_char_to_leaderboard_class_method(self):
        """
        Tests if entry is made
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        character = ActiveCharacter.create_new_character(user)

        Leaderboard.active_char_to_leaderboard(character)

        self.assertEqual(Leaderboard.objects.all().count(), 1)
