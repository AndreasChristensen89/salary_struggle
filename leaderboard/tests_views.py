from django.test import TestCase


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
