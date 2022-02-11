from django.test import TestCase
from .models import Item, Interviewer
import tempfile


class TestViews(TestCase):

    """
    Test all html pages for the codex
    """

    def test_items_page(self):
        """ Test items page """
        response = self.client.get('/codex/items/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codex/items.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_interviewers_page(self):
        """ Test interviewers page """
        response = self.client.get('/codex/interviewers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codex/interviewers.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_item_details(self):
        """ Test item details page """
        item = Item.objects.create(
            name='Pepper',
            price=500,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name)
        response = self.client.get(f'/codex/items/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codex/item_details.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_iterviewer_details(self):
        """ Test interviewer details page """
        interviewer = Interviewer.objects.create(
            name='John',
            friendly_name='John',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name)
        response = self.client.get(f'/codex/interviewers/{interviewer.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codex/interviewer_details.html')
        self.assertTemplateUsed(response, 'base.html')
