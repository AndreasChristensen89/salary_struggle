from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.generic import UpdateView
from profiles.models import Profile, ActiveCharacter
from codex.models import Item
from .functions import set_energy, validate_user, dice_roll
import json


@login_required
def enter_game(request):
    """ Delete a product from the store """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    context = {
        'character': character,
    }

    return render(request, 'grind/enter_grind.html', context)


@login_required
def city(request):
    """ A view to return the city page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    context = {
        'character': character,
        'no_bag_display': True,
    }

    return render(request, 'grind/city.html', context)


@login_required
def bar_page(request):
    """ A view to return the bar page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    context = {
        'character': character,
        'no_bag_display': True,
    }

    return render(request, 'grind/bar.html', context)


@login_required
def library_page(request):
    """ A view to return the library page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    context = {
        'character': character,
        'no_bag_display': True,
    }

    return render(request, 'grind/library.html', context)


@login_required
def downtown_page(request):
    """ A view to return the downtown page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    context = {
        'character': character,
        'no_bag_display': True,
    }

    return render(request, 'grind/downtown.html', context)


@login_required
def house_page(request):
    """ A view to return the home page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    context = {
        'character': character,
        'no_bag_display': True,
    }

    return render(request, 'grind/house.html', context)


@login_required
def agency_page(request):
    """ A view to return the agency page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    context = {
        'character': character,
        'no_bag_display': True,
    }

    return render(request, 'grind/agency.html', context)


@login_required
def store_page(request):
    """ A view to return the store page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    items = Item.objects.all()
    character_items = character.items.all()

    context = {
        'items': items,
        'character': character,
        'character_items': character_items,
        'no_bag_display': True,
    }

    return render(request, 'grind/store.html', context)


@login_required
def call_center_page(request):
    """ A view to return the call-center page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    context = {
        'character': character,
        'no_bag_display': True,
    }

    return render(request, 'grind/call_center.html', context)


@login_required
def back_alley_page(request):
    """ A view to return the back alley page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    context = {
        'character': character,
        'no_bag_display': True,
    }

    return render(request, 'grind/back_alley.html', context)


# ------------------------ Update views --------------------------

class update_charm_home(UpdateView):
    """
    Updates charm from home
    """
    def post(self, *args, **kwargs):
        """
        Overrides POST method to ensure the request is AJAX,
        Updates the user's active character profile with the
        information received via AJAX, and returns the appropriate HTTP
        responses accoringly.
        """
        if self.request.is_ajax():
            # Obtain Active Character
            character = ActiveCharacter.objects.get(user=self.request.user)
            # Update Active Character
            if character.energy >= 40-character.endurance:
                character.charm = character.charm + 1
                character.energy = character.energy - (40-character.endurance)
                character.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class sleep(UpdateView):
    """
    Restores energy, advances one day, and applies penalties
    """
    def post(self, *args, **kwargs):
        """
        Overrides POST method to ensure the request is AJAX,
        Updates the user's active character profile with the
        information received via AJAX, and returns the appropriate HTTP
        responses accoringly.
        """
        if self.request.is_ajax():
            # Obtain Active Character
            c = ActiveCharacter.objects.get(user=self.request.user)
            # Update Active Character
            if c.energy < 100:
                # subtracts penalties from the day
                c.energy = 100-c.energy_penalty
                c.intellect = c.intellect-c.intellect_penalty
                c.charm = c.charm-c.charm_penalty
                c.coding = c.coding-c.coding_penalty
                c.endurance = c.endurance-c.endurance_penalty
                c.day = c.day+1
                # resets all penalties to 0 for new day
                c.energy_penalty = 0
                c.intellect_penalty = 0
                c.charm_penalty = 0
                c.coding_penalty = 0
                c.endurance_penalty = 0
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class study_home(UpdateView):
    """
    Restores energy, advances one day, and applies penalties
    """
    def post(self, *args, **kwargs):
        """
        Overrides POST method to ensure the request is AJAX,
        Updates the user's active character profile with the
        information received via AJAX, and returns the appropriate HTTP
        responses accoringly.
        """
        if self.request.is_ajax():
            # Obtain Active Character
            c = ActiveCharacter.objects.get(user=self.request.user)
            # Update Active Character
            if c.energy >= 40-c.endurance:
                c.coding = c.coding + 1
                c.energy = c.energy-(40-c.endurance)
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class bar_drink(UpdateView):
    """
    Test if ajax updates without refresh
    """
    def post(self, *args, **kwargs):
        """
        Overrides POST method to ensure the request is AJAX,
        Updates the user's active character profile with the
        information received via AJAX, and returns the appropriate HTTP
        responses accoringly.
        """
        if self.request.is_ajax():
            # Obtain Active Character
            character = ActiveCharacter.objects.get(user=self.request.user)
            # Update Active Character
            if character.energy >= 40-character.endurance:
                if character.money > 1000:
                    character.charm = character.charm + 2
                    character.energy = character.energy - (40-character.endurance)
                    character.money = character.money-1000
                    character.energy_penalty = character.energy_penalty+20
                    character.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class bar_converse(UpdateView):
    """
    Calcualtes odds 2 to 1, checks energy, and updates charm if ok
    """
    def post(self, *args, **kwargs):
        """
        Overrides POST method to ensure the request is AJAX,
        Updates the user's active character profile with the
        information received via AJAX, and returns the appropriate HTTP
        responses accoringly.
        """
        if self.request.is_ajax():
            # Obtain Active Character
            c = ActiveCharacter.objects.get(user=self.request.user)
            # receive random number
            random_number = json.loads(self.request.POST['random_number'])
            # Update Active Character
            if c.energy >= 40-c.endurance and random_number <= 2:
                c.charm = c.charm + 2
                c.energy = c.energy - (40-c.endurance)
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class library_study(UpdateView):
    """
    Calcualtes odds 2 to 1, checks energy, and updates charm if ok
    """
    def post(self, *args, **kwargs):
        """
        Overrides POST method to ensure the request is AJAX,
        Updates the user's active character profile with the
        information received via AJAX, and returns the appropriate HTTP
        responses accoringly.
        """
        if self.request.is_ajax():
            # Obtain Active Character
            c = ActiveCharacter.objects.get(user=self.request.user)
            # receive random number
            random_number = json.loads(self.request.POST['random_number'])
            # Update Active Character
            if c.energy >= 60-c.endurance:
                if random_number <= 2:
                    c.intellect = c.intellect + 2
                    c.coding = c.coding + 2
                    c.energy = c.energy - (60-c.endurance)
                    c.save()
                else:
                    c.intellect = c.intellect + 1
                    c.coding = c.coding + 1
                    c.energy = c.energy - (60-c.endurance)
                    c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class agency_skill(UpdateView):
    """
    Compares player's stat level to random number
    Updates level if success
    """
    def post(self, *args, **kwargs):
        """
        Overrides POST method to ensure the request is AJAX,
        Updates the user's active character profile with the
        information received via AJAX, and returns the appropriate HTTP
        responses accoringly.
        """
        if self.request.is_ajax():
            # Obtain Active Character
            c = ActiveCharacter.objects.get(user=self.request.user)
            # receive random number
            random_number = json.loads(self.request.POST['random_number'])
            skill = self.request.POST['skill']
            print(random_number)
            print(skill)
            print(c.intellect >= random_number)
            print(c.charm >= random_number)
            print(c.coding >= random_number)
            # Update Active Character
            if skill == "intellect" and c.intellect >= random_number:
                c.level = c.level + 1
                c.save()
            elif skill == "charm" and c.charm >= random_number:
                c.level = c.level + 1
                c.save()
            elif skill == "coding" and c.coding >= random_number:
                c.level = c.level + 1
                c.save()
            else:
                c.energy = 0
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class agency_combine(UpdateView):
    """
    Compares player's stat level to random number
    Updates level if success
    """
    def post(self, *args, **kwargs):
        """
        Overrides POST method to ensure the request is AJAX,
        Updates the user's active character profile with the
        information received via AJAX, and returns the appropriate HTTP
        responses accoringly.
        """
        if self.request.is_ajax():
            # Obtain Active Character
            c = ActiveCharacter.objects.get(user=self.request.user)
            # receive random number
            random_number = json.loads(self.request.POST['random_number'])
            # Update Active Character
            if (c.intellect + c.charm + c.coding) >= random_number:
                c.level = c.level + 1
                c.save()
            else:
                c.energy = 0
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


@login_required
def add_item(request, item_id):
    """
    Updates the character's stats according to item stats
    Attaches the item to character if permanent
    """

    profile = get_object_or_404(Profile, user=request.user)
    c = get_object_or_404(ActiveCharacter, user=request.user)
    i = get_object_or_404(Item, id=item_id)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and c.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if c.money >= i.price:
        if i not in c.items.all():
            ActiveCharacter.objects.filter(user=request.user).update(
                intellect=c.intellect+i.intellect,
                charm=c.charm+i.charm,
                coding=c.coding+i.coding,
                energy=c.energy+i.energy,
                endurance=c.endurance+i.endurance,
                intellect_penalty=c.intellect_penalty+i.intellect_penalty,
                charm_penalty=c.charm_penalty+i.charm_penalty,
                coding_penalty=c.coding_penalty+i.coding_penalty,
                energy_penalty=c.energy_penalty+i.energy_penalty,
                endurance_penalty=c.endurance_penalty+i.endurance_penalty,
                money=c.money-i.price
                )

            if i.permanent:
                c.items.add(i)
        else:
            messages.error(request, 'You already own this')
    else:
        messages.error(request, 'You cannot afford this')

    return redirect(reverse('grind:store'))


@login_required
def apply_job(request):
    """
    Updates characters job status to true if successfull outcome
    """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if dice_roll(character.charm, 20):
        ActiveCharacter.objects.filter(user=request.user).update(has_job=True)
        messages.success(request, '"Get in the damn chair and start working" - You now have a part time job')
    else:
        messages.error(request, '"Get lost kid", says the manager')

    return redirect(reverse('grind:call-center'))


@login_required
def work(request):
    """
    View to increase money, given enough energy
    """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    salary = character.charm * 100

    if character.energy >= 60-character.endurance:
        ActiveCharacter.objects.filter(user=request.user).update(money=character.money+salary)
        messages.error(request, f'You made ¥{salary}')
        set_energy(request.user, 60-character.endurance)
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:call-center'))


@login_required
def fight(request):
    """
    Updates endurance, given winning outcome
    """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if character.energy >= 60-character.endurance:
        if dice_roll(5, 10):
            ActiveCharacter.objects.filter(user=request.user).update(endurance=character.endurance+3)
            messages.success(request, 'Nicely done, the other guy looks pretty roughed up. Your endurance went up')
            set_energy(request.user, 60-character.endurance)
        else:
            ActiveCharacter.objects.filter(user=request.user).update(
                energy=0,
                energy_penalty=character.energy_penalty+50)
            messages.error(request, 'Auch, you may need a trip to the hospital. No more energy for you today, and make sure to rest tomorrow')
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:back-alley'))


@login_required
def gamble(request):
    """
    Updates endurance, given winning outcome
    """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if character.money >= 1000:
        if dice_roll(1, 3):
            ActiveCharacter.objects.filter(user=request.user).update(money=character.money+3000)
            messages.success(request, 'Lucky you, you just pocketed ¥3000')
        else:
            ActiveCharacter.objects.filter(user=request.user).update(money=character.money-1000)
            messages.error(request, 'Better luck next time. Try to win it back, or stay sensible.')
    else:
        messages.error(request, "In your current financial situation you probably shouldn't")

    return redirect(reverse('grind:back-alley'))
