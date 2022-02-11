from django.shortcuts import render, redirect


def view_shopping_bag(request):
    """ A view that renders the shopping bag """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})    # We check to see if there's a bag var, if not we create one {}
    # now we have a python object
    # create a key of the product's id and set it equal to the quatity
    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag    # override the var in the session with the updated version
    print(request.session['bag'])
    return redirect(redirect_url)
