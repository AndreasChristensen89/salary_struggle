from django.shortcuts import render, get_object_or_404

from .models import Profile


def profile(request):
    """ A view to return the profile page """
    profile = get_object_or_404(Profile, user=request.user)

    template = 'profiles/profiles.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
