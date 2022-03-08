from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from profiles.models import Profile

from shop.models import Product


def view_shopping_bag(request):
    """ A view that renders the shopping bag """

    context = {
        'no_bag_display': True,
    }

    return render(request, 'shopping_bag/shopping_bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    profile = Profile.objects.get(user=request.user)
    redirect_url = request.POST.get('redirect_url')
    if not profile.paid:
        product = Product.objects.get(pk=item_id)
        quantity = int(request.POST.get('quantity'))    # convert since it comes as a string from the template
        bag = request.session.get('bag', {})    # We check to see if there's a bag var, if not we create one {}
        # now we have a python object
        
        if item_id in list(bag.keys()):  # if there's already a key in the dictionary
            if product.name != "Premium Membership":
                bag[item_id] += quantity     # increment the quantity
                messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
            else:
                messages.error(request, 'Premium membership already in the bag')
        else:
            bag[item_id] = quantity  # create a key of the product's id and set it equal to the quatity
            messages.success(request, f'{product.name} was added to the shopping bag')

        request.session['bag'] = bag    # put the bag into the session, override the variable with an update version
    else:
        messages.error(request, "You are already a premium user.")
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'{product.name} was removed from the shopping bag')

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag:shopping_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'{product.name} was removed from the shopping bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
