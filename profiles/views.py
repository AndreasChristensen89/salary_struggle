from django.shortcuts import render


def profile(request):
    """ A view to return the profile page """

    return render(request, 'profile/profile.html')
