from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import UpdateView
from profiles.models import Profile, ActiveCharacter
from codex.models import Item
import json


@login_required
def intro(request):
    """ Intro for level 1 players """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level > 1:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    return render(request, 'grind/intro.html')


@login_required
def enter_game(request):
    """ Delete a product from the store """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    return render(request, 'grind/enter_grind.html')


@login_required
def city(request):
    """ A view to return the city page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    context = {
        'no_bag_display': True,
    }

    return render(request, 'grind/city.html', context)


@login_required
def bar_page(request):
    """ A view to return the bar page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    context = {
        'no_bag_display': True,
    }

    return render(request, 'grind/bar.html', context)


@login_required
def cafe_page(request):
    """ A view to return the cafe page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    context = {
        'no_bag_display': True,
    }

    return render(request, 'grind/cafe.html', context)


@login_required
def downtown_page(request):
    """ A view to return the downtown page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    context = {
        'no_bag_display': True,
    }

    return render(request, 'grind/downtown.html', context)


@login_required
def house_page(request):
    """ A view to return the home page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    context = {
        'no_bag_display': True,
    }

    return render(request, 'grind/house.html', context)


@login_required
def agency_page(request):
    """ A view to return the agency page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    context = {
        'no_bag_display': True,
    }

    return render(request, 'grind/agency.html', context)


@login_required
def store_page(request):
    """ A view to return the store page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    items = Item.objects.all()
    character_items = character.items.all()

    context = {
        'items': items,
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
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    context = {
        'no_bag_display': True,
    }

    return render(request, 'grind/call_center.html', context)


@login_required
def back_alley_page(request):
    """ A view to return the back alley page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request,
                       'You need to create a character to enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request,
                       'Free limit reached. Go premium for full access')
        return redirect(reverse('profiles:profile'))
    elif character.day > 30:
        return redirect(reverse('leaderboard:gameover_page'))

    context = {
        'no_bag_display': True,
    }

    return render(request, 'grind/back_alley.html', context)


# ------------------------ Update views --------------------------

class UpdateCharmHome(UpdateView):
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


class Sleep(UpdateView):
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
                c.day = c.day+1
                # resets all penalties to 0 for new day
                c.energy_penalty = 0
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class StudyHome(UpdateView):
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


class BarDrink(UpdateView):
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
            c = ActiveCharacter.objects.get(user=self.request.user)
            # Update Active Character
            if c.energy >= 40-c.endurance and c.energy_penalty <= 80:
                if c.money >= 1000:
                    c.charm = c.charm + 2
                    c.energy = c.energy - (40-c.endurance)
                    c.money = c.money-1000
                    c.energy_penalty = c.energy_penalty+20
                    c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class BarConverse(UpdateView):
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
            if c.energy >= 40-c.endurance:
                if (random_number <= 2):
                    c.charm = c.charm + 2

                c.energy = c.energy - (40-c.endurance)
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class CafeStudy(UpdateView):
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
                else:
                    c.intellect = c.intellect + 1
                    c.coding = c.coding + 1
                c.energy = c.energy - (60-c.endurance)
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class AgencySkill(UpdateView):
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

            if c.energy >= 100:
                # Update Active Character
                if skill == "intellect" and c.intellect >= random_number:
                    c.level = c.level + 1
                elif skill == "charm" and c.charm >= random_number:
                    c.level = c.level + 1
                elif skill == "coding" and c.coding >= random_number:
                    c.level = c.level + 1
                else:
                    c.energy = 0
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class AgencyCombine(UpdateView):
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
            if c.energy >= 100:
                # Update Active Character
                if (c.intellect + c.charm + c.coding) >= random_number:
                    c.level = c.level + 1
                else:
                    c.energy = 0
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class AddItem(UpdateView):
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
            # receive item
            item_id = json.loads(self.request.POST['item_id'])
            i = get_object_or_404(Item, id=item_id)
            # Update Active Character
            if c.money >= i.price:
                # Checks if char owns item
                if i not in c.items.all():
                    c.intellect = c.intellect + i.intellect
                    c.charm = c.charm + i.charm
                    c.coding = c.coding + i.coding
                    if c.energy <= 180:
                        c.energy = c.energy + i.energy
                    c.endurance = c.endurance + i.endurance
                    c.money = c.money - i.price
                    c.save()
                    # additional save if permanent
                    if i.permanent:
                        c.items.add(i)
                        c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class ApplyJob(UpdateView):
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
            # Update Active Character
            if c.energy >= (60-c.endurance):
                if c.charm >= 20:
                    c.has_job = True
                c.energy = c.energy - (60-c.endurance)
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class Work(UpdateView):
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
            # calculate salary
            salary = c.charm * 100
            # Update Active Character
            if c.energy >= (60-c.endurance) and c.has_job:
                c.money = c.money + salary
                c.energy = c.energy - (60-c.endurance)
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class Fight(UpdateView):
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
            if c.energy >= 60 and c.energy_penalty <= 50:
                if c.endurance <= 21:
                    if random_number >= 5:
                        c.energy = c.energy - 60
                        c.endurance = c.endurance + 3
                    else:
                        c.energy = 0
                        c.energy_penalty = c.energy_penalty + 50
                    c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)


class Gamble(UpdateView):
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
            if c.money >= 1000:
                if random_number == 1:
                    c.money = c.money + 1500
                else:
                    c.money = c.money - 1000
                c.save()
            return HttpResponse(200)
        else:
            return HttpResponse(400)
