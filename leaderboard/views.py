from django.shortcuts import render
from leaderboard.models import Leaderboard
from django.contrib.auth.decorators import login_required


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

    return render(request, 'leaderboard/winning_page.html')
