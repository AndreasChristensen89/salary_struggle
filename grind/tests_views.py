import json
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import ActiveCharacter
from codex.models import Item


def create_new_character():
    """
    Creates user, character, and logs in
    """
    new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    ActiveCharacter.create_new_character(new_user)
    self.client.login(username='john', password='johnpassword')

# class TestNavigationViews(TestCase):

#     """
#     Test all pages for the grind navigation
#     """

#     def test_agency_page(self):
#         """ Test agency page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/agency/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/agency.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_back_alley_page(self):
#         """ Test back alley page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/back-alley/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/back_alley.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_bar_page(self):
#         """ Test bar page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/bar/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/bar.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_cafe_page(self):
#         """ Test cafe page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/cafe/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/cafe.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_call_center_page(self):
#         """ Test call center page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/call-center/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/call_center.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_city_page(self):
#         """ Test city page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/city/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/city.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_downtown_page(self):
#         """ Test downtown page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/downtown/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/downtown.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_enter_grind_page(self):
#         """ Test downtown page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/enter/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/enter_grind.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_house_page(self):
#         """ Test house page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/house/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/house.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_intro_page(self):
#         """ Test house page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/intro/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/intro.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_store_page(self):
#         """ Test store page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/store/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/store.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')


class TestUpdateCharacterAjaxViews(TestCase):
    """
    Tests all Ajax calls if they update the character
    """

    def test_update_charm_home_ajax(self):
        """
        Tests if charm is upgraded, energy subtracted, and http response given
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        response = self.client.post(
            '/grind/charm-home/',
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.energy == 61)
        self.assertTrue(character.charm == 2)

    def test_sleep_ajax(self):
        """
        Tests if energy is recharged,
        penalties applied and reset,
        day progressed
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(
            energy=60,
            energy_penalty=20,
            charm_penalty=1,
            coding_penalty=1,
            intellect_penalty=1,
            endurance_penalty=1)

        self.client.login(username='john', password='johnpassword')
        response = self.client.post(
            '/grind/sleep/',
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.energy == 80)
        self.assertTrue(character.charm == 0)
        self.assertTrue(character.coding == 0)
        self.assertTrue(character.intellect == 0)
        self.assertTrue(character.endurance == 0)
        self.assertTrue(character.day == 2)

    def test_study_home_ajax(self):
        """
        Tests if coding is upgraded, energy subtracted, and http response given
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        response = self.client.post(
            '/grind/study-home/',
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.energy == 61)
        self.assertTrue(character.coding == 2)

    def test_bar_drink_ajax(self):
        """
        Tests if energy subtracted, charm upgraded,
        penalty applied, money subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        response = self.client.post(
            '/grind/bar-drink/',
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.energy == 61)
        self.assertTrue(character.money == 19000)
        self.assertTrue(character.energy_penalty == 20)
        self.assertTrue(character.charm == 3)

    def test_bar_converse_success_ajax(self):
        """
        Tests if, given winning outcome, charm upgraded,
        energy subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        data = {'random_number':  2}
        response = self.client.post(
            '/grind/bar-converse/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.charm == 3)
        self.assertTrue(character.energy == 61)

    def test_bar_converse_fail_ajax(self):
        """
        Tests if, given failing outcome, charm not upgraded,
        energy subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        data = {'random_number':  3}
        response = self.client.post(
            '/grind/bar-converse/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.charm == 1)
        self.assertTrue(character.energy == 61)

    def test_cafe_study_success_ajax(self):
        """
        Tests if, given winning outcome, intellect upgraded,
        coding upgraded, energy subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        data = {'random_number':  2}
        response = self.client.post(
            '/grind/cafe-study/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.intellect == 3)
        self.assertTrue(character.coding == 3)
        self.assertTrue(character.energy == 41)

    def test_cafe_study_fail_ajax(self):
        """
        Tests if, given failing outcome, intellect not upgraded,
        coding not upgraded, energy subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        data = {'random_number': 3}
        response = self.client.post(
            '/grind/cafe-study/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.intellect == 2)
        self.assertTrue(character.coding == 2)
        self.assertTrue(character.energy == 41)

    def test_agency_skill_success_ajax(self):
        """
        Tests if, given winning outcome, level upgraded
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        ActiveCharacter.objects.filter(user=new_user).update(intellect=15)

        data = {
            'random_number': 15,
            'skill': 'intellect',
        }
        response = self.client.post(
            '/grind/agency-skill/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.level == 2)

    def test_agency_skill_fail_ajax(self):
        """
        Tests if, given failing outcome, level not upgraded,
        energy depleted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        ActiveCharacter.objects.filter(user=new_user).update(intellect=15)

        data = {
            'random_number': 16,
            'skill': 'intellect',
        }
        response = self.client.post(
            '/grind/agency-skill/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.level == 1)
        self.assertTrue(character.energy == 0)

    def test_agency_combine_success_ajax(self):
        """
        Tests, given winning outcome, level upgraded,
        energy not changed
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        ActiveCharacter.objects.filter(user=new_user).update(
            intellect=15, coding=15, charm=15)

        data = {'random_number': 45}

        response = self.client.post(
            '/grind/agency-combine/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )

        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.level == 2)
        self.assertTrue(character.energy == 100)
    
    def test_agency_combine_fail_ajax(self):
        """
        Tests, given winning outcome, level upgraded,
        energy not changed
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        ActiveCharacter.objects.filter(user=new_user).update(
            intellect=15, coding=15, charm=15)

        data = {'random_number': 46}

        response = self.client.post(
            '/grind/agency-combine/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )

        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.level == 1)
        self.assertTrue(character.energy == 0)

    def test_add_item_permanent_ajax(self):
        """
        Tests if permanent item is added to character,
        and money subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        Item.objects.create(name='item', price=100, permanent=True)
        self.client.login(username='john', password='johnpassword')

        data = {'item_id': 1}

        response = self.client.post(
            '/grind/add-item/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )

        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        item = Item.objects.get(id=1)
        self.assertTrue(item in character.items.all())
        self.assertTrue(character.money == 19900)

    def test_add_item_not_permanent_ajax(self):
        """
        Tests if permanent item is not added to character,
        and money subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        Item.objects.create(name='item', price=100)
        self.client.login(username='john', password='johnpassword')

        data = {'item_id': 1}

        response = self.client.post(
            '/grind/add-item/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )

        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        item = Item.objects.get(id=1)
        self.assertTrue(item not in character.items.all())
        self.assertTrue(character.money == 19900)

    def test_apply_job_success_ajax(self):
        """
        Tests, if charm is sufficient, character has_job,
        energy subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        ActiveCharacter.objects.filter(user=new_user).update(charm=15)

        data = {'random_number': 15}

        response = self.client.post(
            '/grind/apply-job/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )

        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.has_job)
        self.assertTrue(character.energy == 41)

    def test_apply_job_fail_ajax(self):
        """
        Tests, if charm is insufficient, character has_job is False,
        energy subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        ActiveCharacter.objects.filter(user=new_user).update(charm=15)

        data = {'random_number': 17}

        response = self.client.post(
            '/grind/apply-job/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )

        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(not character.has_job)
        self.assertTrue(character.energy == 41)

    def test_work_ajax(self):
        """
        Tests if energy subtracted and money increased
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        ActiveCharacter.objects.filter(user=new_user).update(charm=10)

        response = self.client.post(
            '/grind/work/',
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.energy == 41)
        self.assertTrue(character.money == 21000)

    def test_fight_success_ajax(self):
        """
        Tests, given winning outcome, endurance upgraded,
        energy subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        data = {'random_number': 5}

        response = self.client.post(
            '/grind/fight/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.energy == 41)
        self.assertTrue(character.endurance == 4)

    def test_fight_fail_ajax(self):
        """
        Tests, given winning outcome, endurance upgraded,
        energy subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        data = {'random_number': 2}

        response = self.client.post(
            '/grind/fight/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.energy == 0)
        self.assertTrue(character.endurance == 1)
        self.assertTrue(character.energy_penalty == 50)

    def test_gamle_success_ajax(self):
        """
        Tests if winning outcome increases money
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        data = {'random_number': 1}

        response = self.client.post(
            '/grind/gamble/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.money == 22000)

    def test_gamle_fail_ajax(self):
        """
        Tests if winning outcome increases money
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        data = {'random_number': 2}

        response = self.client.post(
            '/grind/gamble/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=new_user)
        self.assertTrue(character.money == 19000)
