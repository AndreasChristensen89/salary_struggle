from random import randint
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib import messages
from profiles.models import Profile, ActiveCharacter


def validate_user(request):
    """
    Checks if user is logged and has a character
    """
    profile = get_object_or_404(Profile, user=request.user)
    
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))


def set_energy(user, consumed):
    """ Locating character and subtracting stated energy """

    curr_energy = ActiveCharacter.objects.get(user=user).energy
    ActiveCharacter.objects.filter(user=user).update(energy=curr_energy-consumed)


def dice_roll(chance, odds):
    """
    Produces a random number between 1 and the odds
    If random number is the chance or below then player wins
    e.g. chance is 20, odds are 60 ==> 1-20 are winning numbers
    """
    dare_number = randint(1, odds+1)
    return dare_number <= chance
