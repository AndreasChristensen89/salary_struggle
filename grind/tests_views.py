from django.test import TestCase


class TestViews(TestCase):

    """
    Test all html pages for the grind
    """

    def test_agency_page(self):
        """ Test agency page """
        response = self.client.get('/grind/agency/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grind/agency.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_back_alley_page(self):
        """ Test back alley page """
        response = self.client.get('/grind/back-alley/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grind/back_alley.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_bar_page(self):
        """ Test bar page """
        response = self.client.get('/grind/bar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grind/bar.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_call_center_page(self):
        """ Test call center page """
        response = self.client.get('/grind/call-center/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grind/call_center.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_city_page(self):
        """ Test city page """
        response = self.client.get('/grind/city/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grind/city.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_downtown_page(self):
        """ Test downtown page """
        response = self.client.get('/grind/downtown/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grind/downtown.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_house_page(self):
        """ Test house page """
        response = self.client.get('/grind/house/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grind/house.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_library_page(self):
        """ Test library page """
        response = self.client.get('/grind/library/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grind/library.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_store_page(self):
        """ Test store page """
        response = self.client.get('/grind/store/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grind/store.html')
        self.assertTemplateUsed(response, 'base.html')
