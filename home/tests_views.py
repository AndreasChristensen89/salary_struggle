from django.test import TestCase


class TestViews(TestCase):
    """
    Test all html pages for the codex
    """

    def test_index_page(self):
        """ Test index page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateUsed(response, 'base.html')
