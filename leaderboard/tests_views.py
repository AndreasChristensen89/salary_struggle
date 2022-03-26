from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from profiles.models import ActiveCharacter
from leaderboard.models import Leaderboard


class TestLeaderboardViews(TestCase):
    """
    Test all pages for the shop navigation
    """

    def test_leaderboard_page(self):
        """
        Tests if leaderboard page works
        """

        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leaderboard/leaderboard.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_winning_page(self):
        """
        Tests if winning page works
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')
        Profile.objects.filter(user=new_user).update(paid=True)
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(level=6)
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/leaderboard/winning-page/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leaderboard/winning_page.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_calculate_leaderboard_spot_success_view(self):
        """
        Tests if calcualte leaderboard spot view works
        Created 10 low-score entries, sees if new user gets a spot
        Score calculated from restarted character is higher,
        which is due to low day integer
        """
        user = User.objects.create_user('paul', 'mccartney@thebeatles.com',
                                        'paulpassword')

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

        new_user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                            'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(level=6)
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/leaderboard/calculate-leaderboard-spot/',
                                   follow=True)

        self.assertRedirects(response, '/leaderboard/')
        self.assertEqual(len(Leaderboard.objects.filter(user=user)), 9)
        self.assertEqual(len(Leaderboard.objects.filter(user=new_user)), 1)

    def test_calculate_leaderboard_spot_fail_view(self):
        """
        Tests if user not on top 10 if criteria not met
        Creating 10 entries, then attempting to sumbit char with lower score
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                        'johnpassword')

        for i in range(2, 12):
            Leaderboard.objects.create(
                user=user,
                score=1000+i,
                char_intellect=i,
                char_charm=i,
                char_coding=i,
                char_endurance=i,
                char_money=i,
                char_day=i)

        new_user = User.objects.create_user('paul', 'mccartney@thebeatles.com',
                                            'paulpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(level=6, money=1,
                                                             day=25)
        self.client.login(username='paul', password='paulpassword')
        response = self.client.get('/leaderboard/calculate-leaderboard-spot/',
                                   follow=True)

        self.assertRedirects(response, '/')
        self.assertEqual(len(Leaderboard.objects.filter(user=user)), 10)
        self.assertEqual(len(Leaderboard.objects.filter(user=new_user)), 0)
