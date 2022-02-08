from django.shortcuts import render


def interview(request):
    """ A view to return the interview page """

    return render(request, 'interview/interview.html')
