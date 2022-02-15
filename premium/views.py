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
        message.error(request, "The bag is currently empty")
        return redirect(reverse('shop:all_products'))

    order_form = OrderForm()
    template = 'premium/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
