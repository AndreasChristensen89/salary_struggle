from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from leaderboard.models import Leaderboard
from django.contrib.auth.decorators import login_required
from profiles.models import Profile, ActiveCharacter


def leaderboard(request):
    """ A view to return the leaderboard page """

    board = Leaderboard.objects.all()

    context = {
        'leaderboard': board,
    }

    return render(request, 'leaderboard/leaderboard.html', context)


@login_required
def winning_page(request):
    """ A view to return the winning page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)
    leaderboard_spot = False

    if not profile.active_char:
        messages.error(request, 'Active character needed')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid:
        messages.error(request, 'Upgrade to premium to get full access')
        return redirect(reverse('profiles:profile'))
    elif character.level < 6:
        messages.error(request, 'Level not high enough')
        return redirect(reverse('profiles:profile'))

    context = {
        'leaderboard_spot': leaderboard_spot
    }

    return render(request, 'leaderboard/winning_page.html', context)
