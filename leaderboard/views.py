from django.shortcuts import render
from leaderboard.models import Leaderboard


def leaderboard(request):
    """ A view to return the leaderboard page """

    board = Leaderboard.objects.all()

    context = {
        'leaderboard': board,
    }

    return render(request, 'leaderboard/leaderboard.html', context)
