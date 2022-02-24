from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import Profile, ActiveCharacter
from codex.models import Item
from .functions import set_energy, validate_user, dice_roll


@login_required
def enter_game(request):
    """ Delete a product from the store """

    validate_user(request)

    return render(request, 'grind/enter_grind.html')


@login_required
def city(request):
    """ A view to return the city page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/city.html')


@login_required
def bar_page(request):
    """ A view to return the bar page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/bar.html')


@login_required
def library_page(request):
    """ A view to return the library page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/library.html')


@login_required
def downtown_page(request):
    """ A view to return the downtown page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/downtown.html')


@login_required
def house_page(request):
    """ A view to return the home page """

    validate_user(request)

    return render(request, 'grind/house.html')


@login_required
def agency_page(request):
    """ A view to return the agency page """

    validate_user(request)

    character = get_object_or_404(ActiveCharacter, user=request.user)

    context = {
        'character': character,
    }

    return render(request, 'grind/agency.html', context)


@login_required
def store_page(request):
    """ A view to return the store page """

    validate_user(request)

    items = Item.objects.all()
    character = get_object_or_404(ActiveCharacter, user=request.user)    

    context = {
        'items': items,
        'character': character,
    }

    return render(request, 'grind/store.html', context)


@login_required
def call_center_page(request):
    """ A view to return the call-center page """

    validate_user(request)

    return render(request, 'grind/call_center.html')


@login_required
def back_alley_page(request):
    """ A view to return the back alley page """

    validate_user(request)

    return render(request, 'grind/back_alley.html')


# Update views

@login_required
def update_charm_home(request):
    """ Update view to add more charm """

    validate_user(request)

    character = get_object_or_404(ActiveCharacter, user=request.user)

    if character.energy >= 40:
        curr_charm = ActiveCharacter.objects.get(user=request.user).charm
        ActiveCharacter.objects.filter(user=request.user).update(charm=curr_charm+1)
        set_energy(request.user, 40)
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:house'))


@login_required
def sleep(request):
    """ Update view to add full energy """
    
    validate_user(request)

    character = get_object_or_404(ActiveCharacter, user=request.user)
    
    if character.energy < 100:
        ActiveCharacter.objects.filter(user=request.user).update(energy=100)
        curr_day = ActiveCharacter.objects.get(user=request.user).day
        ActiveCharacter.objects.filter(user=request.user).update(day=curr_day+1)
        messages.error(request, f'Day {character.day} - take your time')
    else:
        messages.error(request, 'Your energy is full. No need to sleep')
    
    return redirect(reverse('grind:house'))


@login_required
def study_home(request):
    """ Update view to add more charm """
    
    validate_user(request)
    
    character = get_object_or_404(ActiveCharacter, user=request.user)
 
    if character.energy >= 40:
        curr_coding = ActiveCharacter.objects.get(user=request.user).coding
        ActiveCharacter.objects.filter(user=request.user).update(coding=curr_coding+1)
        set_energy(request.user, 40)
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:house'))


@login_required
def bar_converse(request):
    """ Update view to add more charm """
    
    validate_user(request)
    
    character = get_object_or_404(ActiveCharacter, user=request.user)
 
    if character.energy >= 40:
        if dice_roll(2, 3):
            curr_coding = ActiveCharacter.objects.get(user=request.user).coding
            ActiveCharacter.objects.filter(user=request.user).update(coding=curr_coding+1)
            set_energy(request.user, 40)
        else:
            set_energy(request.user, 40)
            messages.error(request, 'Out of luck!')
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:bar'))


@login_required
def bar_drink(request):
    """ Update view to add more charm """
    
    validate_user(request)
    
    character = get_object_or_404(ActiveCharacter, user=request.user)
 
    if character.energy >= 40:
        if character.money > 1000:
            curr_charm = ActiveCharacter.objects.get(user=request.user).charm
            curr_money = ActiveCharacter.objects.get(user=request.user).money
            ActiveCharacter.objects.filter(user=request.user).update(charm=curr_charm+1)
            ActiveCharacter.objects.filter(user=request.user).update(money=curr_money-1000)
            set_energy(request.user, 40)
        else:
            messages.error(request, "Get a job, you're too broke to even buy a beer")
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:bar'))


@login_required
def library_study(request):
    """ Update view to add more charm """
    
    validate_user(request)
    
    character = get_object_or_404(ActiveCharacter, user=request.user)
 
    if character.energy >= 60:
        curr_coding = ActiveCharacter.objects.get(user=request.user).coding
        curr_intellect = ActiveCharacter.objects.get(user=request.user).intellect
        if dice_roll(2, 3):
            ActiveCharacter.objects.filter(user=request.user).update(coding=curr_coding+2)
            ActiveCharacter.objects.filter(user=request.user).update(intellect=curr_intellect+2)
            set_energy(request.user, 60)
        else:
            ActiveCharacter.objects.filter(user=request.user).update(coding=curr_coding+1)
            ActiveCharacter.objects.filter(user=request.user).update(intellect=curr_intellect+1)
            set_energy(request.user, 60)
            messages.error(request, 'Your friends came along and distracted you. Half effort = half reward')
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:library'))


@login_required
def agency_knowledge(request):
    """ Update view to add more charm """

    validate_user(request)

    character = get_object_or_404(ActiveCharacter, user=request.user)

    if dice_roll(character.intellect, 20):
        curr_level = ActiveCharacter.objects.get(user=request.user).level
        ActiveCharacter.objects.filter(user=request.user).update(level=curr_level+1)
        messages.success(request, 'Nicely done, he is completely floored. Your level went up and an HR interview is now available to you')
    else:
        ActiveCharacter.objects.filter(user=request.user).update(energy=0)
        messages.error(request, '"That made absolutely no sense." he quietly told you. Your morale is broken = energy drained')

    return redirect(reverse('grind:agency'))


@login_required
def agency_charm(request):
    """ Update view to add more charm """

    validate_user(request)

    character = get_object_or_404(ActiveCharacter, user=request.user)

    if dice_roll(character.charm, 20):
        curr_level = ActiveCharacter.objects.get(user=request.user).level
        ActiveCharacter.objects.filter(user=request.user).update(level=curr_level+1)
        messages.success(request, 'Awesome, you see stars in his eyes! Your level went up and an HR interview is now available to you')
    else:
        ActiveCharacter.objects.filter(user=request.user).update(energy=0)
        messages.error(request, '"...Are you coming on to me?" he asks you with an annoying look on his face. Your morale is broken = energy drained')

    return redirect(reverse('grind:agency'))


@login_required
def agency_coding(request):
    """ Update view to add more charm """

    validate_user(request)

    character = get_object_or_404(ActiveCharacter, user=request.user)

    if dice_roll(character.coding, 20):
        curr_level = ActiveCharacter.objects.get(user=request.user).level
        ActiveCharacter.objects.filter(user=request.user).update(level=curr_level+1)
        messages.success(request, 'His eyes are the size of dinner plates! Your level went up and an HR interview is now available to you')
    else:
        ActiveCharacter.objects.filter(user=request.user).update(energy=0)
        messages.error(request, '"I know a bit of code, and that there was just amateurish" he tells you with half closed eyes. Your morale is broken = energy drained')

    return redirect(reverse('grind:agency'))


@login_required
def agency_combine(request):
    """ Update view to add more charm """

    validate_user(request)

    character = get_object_or_404(ActiveCharacter, user=request.user)

    chances = character.coding + character.intellect + character.charm
    print(chances)

    if dice_roll(chances, 60):
        curr_level = ActiveCharacter.objects.get(user=request.user).level
        ActiveCharacter.objects.filter(user=request.user).update(level=curr_level+1)
        messages.success(request, '"Wow"! he says enthusiastically. "Consider yourself on to the next stage". Your level went up and an HR interview is now available to you')
    else:
        ActiveCharacter.objects.filter(user=request.user).update(energy=0)
        messages.error(request, '"You probably need some experience before moving on", he says with a dry voice. manage.py Your morale is broken = energy drained')

    return redirect(reverse('grind:agency'))


def add_item(request, item_id):
    """
    Updates the character to match
    """

    validate_user(request)

    item = get_object_or_404(Item, id=item_id)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if character.money >= item.price:
        ActiveCharacter.objects.filter(user=request.user).update(
            intellect=character.intellect+item.intellect,
            charm=character.charm+item.charm,
            coding=character.coding+item.coding,
            energy=character.energy+item.energy,
            money=character.money-item.price,
            )
        if item.permanent:
            character.items.add(item)
    else:
        messages.error(request, 'You cannot afford this')

    return redirect(reverse('grind:store'))
