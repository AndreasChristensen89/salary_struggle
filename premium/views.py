from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def premium(request):
    """ A view to return the premium page """

    return render(request, 'premium/premium.html')


def checkout(request):
    """ A view to return the checkout """

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "The bag is currently empty")
        return redirect(reverse('shop:all_products'))

    order_form = OrderForm()
    template = 'premium/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KTjPeDGj8gZbV1S5AervqzGY60YLX252uD0RwTaSJmc1uCfiS7PoiFPz3VzwLMA5ylSftvQZfdniZLAbx61uDli00Xg4O9ybe',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
