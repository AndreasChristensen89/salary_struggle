from random import randint
from profiles.models import ActiveCharacter


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
