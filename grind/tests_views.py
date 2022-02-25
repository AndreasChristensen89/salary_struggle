from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import ActiveCharacter, Profile
from codex.models import Item


# class TestNavigationViews(TestCase):

#     """
#     Test all pages for the grind navigation
#     """

#     def test_agency_page(self):
#         """ Test agency page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         login = self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/agency/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/agency.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_back_alley_page(self):
#         """ Test back alley page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         login = self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/back-alley/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/back_alley.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_bar_page(self):
#         """ Test bar page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         login = self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/bar/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/bar.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_call_center_page(self):
#         """ Test call center page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         login = self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/call-center/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/call_center.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_city_page(self):
#         """ Test city page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         login = self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/city/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/city.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_downtown_page(self):
#         """ Test downtown page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         login = self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/downtown/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/downtown.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_enter_grind_page(self):
#         """ Test downtown page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         login = self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/enter/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/enter_grind.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_house_page(self):
#         """ Test house page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         login = self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/house/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/house.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_library_page(self):
#         """ Test library page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         login = self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/library/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/library.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')

#     def test_store_page(self):
#         """ Test store page """
#         new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         ActiveCharacter.create_new_character(new_user)
#         login = self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/grind/store/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'grind/store.html')
#         self.assertTemplateUsed(response, 'grind/game_base.html')


class TestUpdateCharacterViews(TestCase):

    """
    Test all pages to upgrade character
    """
    def test_charm_update(self):
        """
        Tests if charm is updated and energy taken
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/grind/update-charm-home/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/house/')
        self.assertEqual(char.charm, 2)
        self.assertEqual(char.energy, 60)

    def test_sleep_update(self):
        """
        Tests if restores energy and handles penalties
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        ActiveCharacter.objects.filter(user=new_user).update(
            energy=40,
            energy_penalty=1,
            charm_penalty=1,
            coding_penalty=1,
            intellect_penalty=1,
            endurance_penalty=1)
        response = self.client.get('/grind/sleep/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/house/')
        self.assertEqual(char.energy, 99)
        self.assertEqual(char.energy_penalty, 0)
        self.assertEqual(char.charm_penalty, 0)
        self.assertEqual(char.coding_penalty, 0)
        self.assertEqual(char.intellect_penalty, 0)
        self.assertEqual(char.endurance_penalty, 0)

    def test_study_home(self):
        """
        Tests if restores energy and handles penalties
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/grind/study-home/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/house/')
        self.assertEqual(char.coding, 2)
        self.assertEqual(char.energy, 60)

    def test_bar_converse(self):
        """
        See if charm raises and energy is drained
        for loop 20 to make sure of winning outcome, needs 800 energy
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        
        array_charm = []
        array_energy = []
        for i in range(20):
            response = self.client.get('/grind/bar-converse/', follow=True)
            char = ActiveCharacter.objects.get(user=new_user)
            array_charm.append(char.charm)
            array_energy.append(char.energy)
            ActiveCharacter.objects.filter(user=new_user).update(
                charm=1,
                energy=100)
    
        self.assertRedirects(response, '/grind/bar/')
        self.assertTrue(3 in array_charm)
        self.assertTrue(1 in array_charm)
        self.assertEqual(char.energy, 60)

    def test_bar_drink(self):
        """
        Tests if restores energy and increases penalty
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        response = self.client.get('/grind/bar-drink/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/bar/')
        self.assertEqual(char.charm, 3)
        self.assertEqual(char.energy, 60)
        self.assertEqual(char.energy_penalty, 20)

    def test_library_study(self):
        """
        See if charm+coding raise and energy is drained
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        array_coding = []
        array_intellect = []
        array_energy = []
        for i in range(20):
            response = self.client.get('/grind/library-study/', follow=True)
            char = ActiveCharacter.objects.get(user=new_user)
            array_coding.append(char.coding)
            array_intellect.append(char.intellect)
            array_energy.append(char.energy)
            ActiveCharacter.objects.filter(user=new_user).update(
                coding=1,
                energy=100,
                intellect=1)
        
        self.assertRedirects(response, '/grind/library/')
        self.assertTrue(2 in array_coding)
        self.assertTrue(3 in array_coding)
        self.assertTrue(2 in array_intellect)
        self.assertTrue(3 in array_intellect)
        self.assertTrue(40 in array_energy)

    def test_agency_knowledge(self):
        """
        Test if level goes up
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(intellect=20)
        self.client.login(username='john', password='johnpassword')

        response = self.client.get('/grind/agency-knowledge/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/agency/')
        self.assertEqual(char.level, 2)

    def test_agency_charm(self):
        """
        Test if level goes up
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(charm=20)
        self.client.login(username='john', password='johnpassword')

        response = self.client.get('/grind/agency-charm/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/agency/')
        self.assertEqual(char.level, 2)

    def test_agency_coding(self):
        """
        Test if level goes up
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(coding=20)
        self.client.login(username='john', password='johnpassword')

        response = self.client.get('/grind/agency-coding/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/agency/')
        self.assertEqual(char.level, 2)

    def test_agency_combined(self):
        """
        Test if level goes up
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(
            coding=20,
            charm=20,
            intellect=20)
        self.client.login(username='john', password='johnpassword')

        response = self.client.get('/grind/agency-combine/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/agency/')
        self.assertEqual(char.level, 2)

    def test_add_item(self):
        """
        Tests if item stats are added and permanent items linked
        """
        item = Item.objects.create(name='shades', price='1000', charm=5, permanent=True)
        itemtwo = Item.objects.create(name='energydrink', price='500', energy=20, permanent=False)
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        response = self.client.get('/grind/add-item/1/', follow=True)
        response = self.client.get('/grind/add-item/2/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/store/')
        self.assertEqual(char.energy, 120)
        self.assertEqual(char.charm, 6)
        self.assertTrue(item in char.items.all())
        self.assertFalse(itemtwo in char.items.all())

    def test_apply_job(self):
        """
        Test if character has_job is set to True
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(charm=20)
        self.client.login(username='john', password='johnpassword')

        response = self.client.get('/grind/apply-job/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/call-center/')
        self.assertEqual(char.has_job, True)

    def test_work(self):
        """
        Test if character is paid and correct energy subtracted
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        ActiveCharacter.objects.filter(user=new_user).update(charm=10)
        self.client.login(username='john', password='johnpassword')

        response = self.client.get('/grind/work/', follow=True)
        char = ActiveCharacter.objects.get(user=new_user)
        self.assertRedirects(response, '/grind/call-center/')
        self.assertEqual(char.money, 22000)
        self.assertEqual(char.energy, 40)

    def test_fight(self):
        """
        Test if endurance goes up and energy subtracted...
        ... or same endurance, 0 energy and energy penalty
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')
        array_endurance = []
        array_energy = []
        array_energy_penalty = []
        for i in range (20):
            response = self.client.get('/grind/fight/', follow=True)
            char = ActiveCharacter.objects.get(user=new_user)
            array_endurance.append(char.endurance)
            array_energy.append(char.energy)
            array_energy_penalty.append(char.energy_penalty)
            ActiveCharacter.objects.filter(user=new_user).update(endurance=1,
                energy=100,
                energy_penalty=0)
        
        self.assertRedirects(response, '/grind/back-alley/')
        self.assertTrue(4 in array_endurance)
        self.assertTrue(1 in array_endurance)
        self.assertTrue(40 in array_energy)
        self.assertTrue(0 in array_energy)
        self.assertTrue(50 in array_energy_penalty)
        self.assertTrue(0 in array_energy_penalty)

    def test_gamle(self):
        """
        Test if money is inserted/taken
        """
        new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ActiveCharacter.create_new_character(new_user)
        self.client.login(username='john', password='johnpassword')

        array_money = []
        for i in range (20):
            response = self.client.get('/grind/gamble/', follow=True)
            char = ActiveCharacter.objects.get(user=new_user)
            array_money.append(char.money)
            ActiveCharacter.objects.filter(user=new_user).update(money=20000)
        
        self.assertRedirects(response, '/grind/back-alley/')
        self.assertTrue(23000 in array_money)
        self.assertTrue(19000 in array_money)
