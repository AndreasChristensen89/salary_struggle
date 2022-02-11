from django.shortcuts import render


def view_shopping_bag(request):
    """ A view that renders the shopping bag """

    return render(request, 'shopping_bag/shopping_bag.html')
