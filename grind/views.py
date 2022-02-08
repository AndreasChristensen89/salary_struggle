from django.shortcuts import render


def city(request):
    """ A view to return the city page """

    return render(request, 'grind/city.html')
