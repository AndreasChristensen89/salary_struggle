from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from shop.models import Product


def view_shopping_bag(request):
    """ A view that renders the shopping bag """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))    # convert since it comes as a string from the template
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})    # We check to see if there's a bag var, if not we create one {}
    # now we have a python object
    
    if item_id in list(bag.keys()):  # if there's already a key in the dictionary
        bag[item_id] += quantity     # increment the quantity
    else:
        bag[item_id] = quantity  # create a key of the product's id and set it equal to the quatity
        messages.success(request, f'{product.name} was added to the shopping bag')

    request.session['bag'] = bag    # put the bag into the session, override the variable with an update version
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag:shopping_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
