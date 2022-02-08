from django.shortcuts import render


def leaderboard(request):
    """ A view to return the leaderboard page """

    return render(request, 'leaderboard/leaderboard.html')
