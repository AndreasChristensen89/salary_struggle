from django.shortcuts import render


def profile(request):
    """ A view to return the profile page """

    template = 'profiles/profiles.html'
    context = {}

    return render(request, template, context)
