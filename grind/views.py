from django.shortcuts import render


def city(request):
    """ A view to return the city page """

    return render(request, 'grind/city.html')


def bar_page(request):
    """ A view to return the bar page """

    return render(request, 'grind/bar.html')


def library_page(request):
    """ A view to return the library page """

    return render(request, 'grind/library.html')


def downtown_page(request):
    """ A view to return the downtown page """

    return render(request, 'grind/downtown.html')


def home_page(request):
    """ A view to return the home page """

    return render(request, 'grind/house.html')


def agency_page(request):
    """ A view to return the agency page """

    return render(request, 'grind/agency.html')


def store_page(request):
    """ A view to return the store page """

    return render(request, 'grind/store.html')


def call_center_page(request):
    """ A view to return the call-center page """

    return render(request, 'grind/call_center.html')


def back_alley_page(request):
    """ A view to return the back alley page """

    return render(request, 'grind/back_alley.html')
