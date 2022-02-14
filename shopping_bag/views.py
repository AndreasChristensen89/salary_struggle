from django.shortcuts import render, redirect


def view_shopping_bag(request):
    """ A view that renders the shopping bag """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))    # convert since it comes as a string from the template
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})    # We check to see if there's a bag var, if not we create one {}
    # now we have a python object
    
    if product_id in list(bag.keys()):  # if there's already a key in the dictionary
        bag[product_id] += quantity     # increment the quantity
    else:
        bag[product_id] = quantity  # create a key of the product's id and set it equal to the quatity

    request.session['bag'] = bag    # put the bag into the session, override the variable with an update version
    return redirect(redirect_url)
