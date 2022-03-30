from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import Profile

from shop.models import Product


@login_required
def view_shopping_bag(request):
    """ A view that renders the shopping bag """

    context = {
        'no_bag_display': True,
    }

    return render(request, 'shopping_bag/shopping_bag.html', context)


@login_required
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    profile = Profile.objects.get(user=request.user)
    redirect_url = request.POST.get('redirect_url')
    product = Product.objects.get(pk=item_id)

    # if premium users attempt to add premum again
    if profile.paid and product.name == "Premium Membership":
        messages.error(request, "You are already a premium user.")
    else:
        # convert as it comes as a string from the template
        quantity = int(request.POST.get('quantity'))
        # Check for bag var, if not create dictionary
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            if product.name != "Premium Membership":
                bag[item_id] += quantity
                messages.success(request,
                                 f'Updated {product.name} quantity to {bag[item_id]}')
            else:
                messages.error(request, 'Premium membership already in bag')
        else:
            # create key of id and set it equal to quantity
            bag[item_id] = quantity
            messages.success(request,
                             f'{product.name} was added to the shopping bag')

        # put bag into session, override the var with an updated version
        request.session['bag'] = bag
    return redirect(redirect_url)


@login_required
def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request,
                         f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request,
                         f'{product.name} was removed from the shopping bag')

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag:shopping_bag'))


@login_required
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request,
                         f'{product.name} was removed from the shopping bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
