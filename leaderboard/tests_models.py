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
            score=1,
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

        Leaderboard.active_char_to_leaderboard(character, 100)

        self.assertEqual(Leaderboard.objects.all().count(), 1)

    def test_calculate_score_static_method(self):
        """
        Tests if score is calculated.
        Unchanged character will give 101.0
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        character = ActiveCharacter.create_new_character(user)

        score = Leaderboard.calculate_score(character)

        self.assertEqual(score, 101.0)

    def test_leaderboard_check_success(self):
        """
        Tests if entry is made to leaderboard model if top 10
        """
        user = User.objects.create_user('paul', 'mccartney@thebeatles.com',
                                        'paulpassword')
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')

        for i in range(2, 12):
            Leaderboard.objects.create(
                user=user,
                score=i,
                char_intellect=i,
                char_charm=i,
                char_coding=i,
                char_endurance=i,
                char_money=i,
                char_day=i)

        character = ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(level=6)
        Leaderboard.leaderboard_check(character)

        self.assertEqual(len(Leaderboard.objects.filter(user=user)), 9)
        self.assertEqual(len(Leaderboard.objects.filter(user=new_user)), 1)

    def test_leaderboard_check_fail(self):
        """
        Tests if entry is not made to leaderboard model too low
        """
        user = User.objects.create_user('paul', 'mccartney@thebeatles.com',
                                        'paulpassword')
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')

        for i in range(2, 12):
            Leaderboard.objects.create(
                user=user,
                score=1000+1,
                char_intellect=i,
                char_charm=i,
                char_coding=i,
                char_endurance=i,
                char_money=i,
                char_day=i)

        character = ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(level=6)
        Leaderboard.leaderboard_check(character)

        self.assertEqual(len(Leaderboard.objects.filter(user=user)), 10)
        self.assertEqual(len(Leaderboard.objects.filter(user=new_user)), 0)
