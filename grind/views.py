from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from profiles.models import Profile, ActiveCharacter
from codex.models import Item
from .functions import set_energy, validate_user, dice_roll


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


# Update views

@login_required
def update_charm_home(request):
    """ Update view to add more charm """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if character.energy >= 40-character.endurance:
        ActiveCharacter.objects.filter(user=request.user).update(charm=character.charm+1)
        set_energy(request.user, 40-character.endurance)
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:house'))


@login_required
def sleep(request):
    """ Update view to add full energy """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if character.energy < 100:
        # subtracts penalties from the day
        ActiveCharacter.objects.filter(user=request.user).update(
            energy=100-character.energy_penalty,
            intellect=character.intellect-character.intellect_penalty,
            charm=character.charm-character.charm_penalty,
            coding=character.coding-character.coding_penalty,
            endurance=character.endurance-character.endurance_penalty,
            day=character.day+1
            )
        # resets all penalties to 0 for new day
        ActiveCharacter.objects.filter(user=request.user).update(
            energy_penalty=0,
            intellect_penalty=0,
            charm_penalty=0,
            coding_penalty=0,
            endurance_penalty=0,
            )
        messages.info(request, f'Day {character.day+1} - take your time')
        if (100-character.energy_penalty) < 0:
            ActiveCharacter.objects.filter(user=request.user).update(energy=0)
            messages.info(request, 'No energy. Looks like you went too rough on yourself yesterday.')
    else:
        messages.error(request, 'Your energy is full. No need to sleep')

    return redirect(reverse('grind:house'))


@login_required
def study_home(request):
    """ Update view to add more charm """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if character.energy >= 40-character.endurance:
        ActiveCharacter.objects.filter(user=request.user).update(coding=character.coding+1)
        set_energy(request.user, 40-character.endurance)
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:house'))


@login_required
def bar_converse(request):
    """ Update view to add more charm """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if character.energy >= 40-character.endurance:
        if dice_roll(2, 3):
            ActiveCharacter.objects.filter(user=request.user).update(charm=character.charm+2)
            set_energy(request.user, 40-character.endurance)
        else:
            set_energy(request.user, 40-character.endurance)
            messages.error(request, 'Out of luck!')
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:bar'))


@login_required
def bar_drink(request):
    """ Update view to add more charm """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if character.energy >= 40-character.endurance:
        if character.money > 1000:
            ActiveCharacter.objects.filter(user=request.user).update(
                charm=character.charm+2,
                money=character.money-1000,
                energy_penalty=character.energy_penalty+20)
            set_energy(request.user, 40-character.endurance)
        else:
            messages.error(request, "Get a job, you're too broke to even buy a beer")
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:bar'))


@login_required
def library_study(request):
    """ Update view to add more charm """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if character.energy >= 60-character.endurance:
        if dice_roll(2, 3):
            ActiveCharacter.objects.filter(user=request.user).update(coding=character.coding+2)
            ActiveCharacter.objects.filter(user=request.user).update(intellect=character.intellect+2)
            set_energy(request.user, 60-character.endurance)
        else:
            ActiveCharacter.objects.filter(user=request.user).update(coding=character.coding+1)
            ActiveCharacter.objects.filter(user=request.user).update(intellect=character.intellect+1)
            set_energy(request.user, 60-character.endurance)
            messages.error(request, 'Your friends came along and distracted you. Half effort = half reward')
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:library'))


@login_required
def agency_knowledge(request):
    """ Update view to add more charm """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if dice_roll(character.intellect, 20):
        ActiveCharacter.objects.filter(user=request.user).update(level=character.level+1)
        messages.success(request, 'Nicely done, he is completely floored. Your level went up and an HR interview is now available to you')
    else:
        ActiveCharacter.objects.filter(user=request.user).update(energy=0)
        messages.error(request, '"That made absolutely no sense." he quietly told you. Your morale is broken = energy drained')

    return redirect(reverse('grind:agency'))


@login_required
def agency_charm(request):
    """ Update view to add more charm """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if dice_roll(character.charm, 20):
        ActiveCharacter.objects.filter(user=request.user).update(level=character.level+1)
        messages.success(request, 'Awesome, you see stars in his eyes! Your level went up and an HR interview is now available to you')
    else:
        ActiveCharacter.objects.filter(user=request.user).update(energy=0)
        messages.error(request, '"...Are you coming on to me?" he asks you with an annoying look on his face. Your morale is broken = energy drained')

    return redirect(reverse('grind:agency'))


@login_required
def agency_coding(request):
    """ Update view to add more charm """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    if dice_roll(character.coding, 20):
        ActiveCharacter.objects.filter(user=request.user).update(level=character.level+1)
        messages.success(request, 'His eyes are the size of dinner plates! Your level went up and an HR interview is now available to you')
    else:
        ActiveCharacter.objects.filter(user=request.user).update(energy=0)
        messages.error(request, '"I know a bit of code, and that there was just amateurish" he tells you with half closed eyes. Your morale is broken = energy drained')

    return redirect(reverse('grind:agency'))


@login_required
def agency_combine(request):
    """ Update view to add more charm """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid and character.level >= 3:
        messages.error(request, 'Free version limit reached. Upgrade to premium to get the full experience')
        return redirect(reverse('profiles:profile'))

    chances = character.coding + character.intellect + character.charm

    if dice_roll(chances, 60):
        ActiveCharacter.objects.filter(user=request.user).update(level=character.level+1)
        messages.success(request, '"Wow"! he says enthusiastically. "Consider yourself on to the next stage". Your level went up and an HR interview is now available to you')
    else:
        ActiveCharacter.objects.filter(user=request.user).update(energy=0)
        messages.error(request, '"You probably need some experience before moving on", he says with a dry voice. manage.py Your morale is broken = energy drained')

    return redirect(reverse('grind:agency'))


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



