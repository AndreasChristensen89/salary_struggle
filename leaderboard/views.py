from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from leaderboard.models import Leaderboard
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from profiles.models import Profile, ActiveCharacter
from django.contrib import messages


def leaderboard(request):
    """ A view to return the leaderboard page """

    board = Leaderboard.objects.all().order_by('-score')

    context = {
        'leaderboard': board,
    }

    return render(request, 'leaderboard/leaderboard.html', context)


@login_required
def gameover_page(request):
    """ A view to return the winning page """

    profile = get_object_or_404(Profile, user=request.user)
    if profile.active_char:
        character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'Active character needed')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid:
        messages.error(request, 'Upgrade to premium to get full access')
        return redirect(reverse('profiles:profile'))
    elif not character.day > 30:
        messages.error(request, 'Your character run is still ongoing')
        return redirect(reverse('profiles:profile'))

    return render(request, 'leaderboard/gameover_page.html')


@login_required
def winning_page(request):
    """ A view to return the winning page """

    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'Active character needed')
        return redirect(reverse('profiles:profile'))
    elif not profile.paid:
        messages.error(request, 'Upgrade to premium to get full access')
        return redirect(reverse('profiles:profile'))
    elif character.level < 6:
        messages.error(request, 'Level not high enough')
        return redirect(reverse('profiles:profile'))

    return render(request, 'leaderboard/winning_page.html')


@login_required
def calculate_leaderboard_spot(request):
    """
    View that calculates if player made it to top 10
    Create entry if so
    If not redirects to home
    """
    c = ActiveCharacter.objects.get(user=request.user)

    check = Leaderboard.leaderboard_check(c)

    if check:
        messages.success(request,
                         "You made it to the leaderboard! Congratulations")
        return redirect(reverse('leaderboard:leaderboard'))
    else:
        messages.info(request, "Unfortunately, you didn't make the top 10")
        return redirect(reverse('home:index'))
