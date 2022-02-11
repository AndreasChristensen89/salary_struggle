from django.test import TestCase
from .models import Item, Interviewer
import tempfile


class TestItem(TestCase):
    """ tests to test the item model """

    def test_item_object_exists(self):
        """ test if object is created """
        Item.objects.create(
            name='Pepper',
            price=500,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name)
        self.assertEqual(Item.objects.all().count(), 1)

    def test_item_class_works(self):
        """ test if default fields work """
        Item.objects.create(
            name='Pepper',
            price=500,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name)
        self.assertEqual(Item.objects.filter(intellect=0).count(), 1)
        self.assertEqual(Item.objects.filter(charm=0).count(), 1)
        self.assertEqual(Item.objects.filter(coding=0).count(), 1)
        self.assertEqual(Item.objects.filter(energy=0).count(), 1)


class TestInterviewer(TestCase):
    """ tests to test the interviewer model """

    def test_item_class_works(self):
        """ test if object with LOW as default """
        Interviewer.objects.create(
            name='John',
            friendly_name='John',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name)
        self.assertEqual(Interviewer.objects.filter(intellect=1).count(), 1)
        self.assertEqual(Interviewer.objects.filter(coldness=1).count(), 1)
        self.assertEqual(Interviewer.objects.filter(coding=1).count(), 1)
        self.assertEqual(Interviewer.objects.filter(impress_lvl=1).count(), 1)
        self.assertEqual(Interviewer.objects.filter(paid=False).count(), 1)
        self.assertEqual(Interviewer.objects.filter(level=1).count(), 1)
