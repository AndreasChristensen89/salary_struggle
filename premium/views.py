import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe

from shop.models import Product
from profiles.models import Profile
from shopping_bag.contexts import shopping_bag_contents
from .forms import OrderForm
from .models import Order, OrderItem


@require_POST
@login_required
def cache_checkout_data(request):
    """
    View create in connection to having the user be able to save info
    Before we call the confirm card method in JS we make a post request
    to this view, give it the client secret.
    We add this to the payment intent in a key called metadata
    """

    try:
        # payment intent id
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # add the meta data
        stripe.PaymentIntent.modify(pid, metadata={
            # json dump of their shopping bag
            'bag': json.dumps(request.session.get('bag', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as error:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=error, status=400)


@login_required
def checkout(request):
    """ A view to return the checkout """

    # payment intent
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }
        order_form = OrderForm(form_data)
        profile = Profile.objects.get(user=request.user)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.user_profile = profile
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                    # if the item is premium membership profile is set to paid
                    if product.name == "Premium Membership":
                        profile = Profile.objects.get(user=request.user)
                        profile.paid = True
                        profile.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products was not in our database. "
                        "Please reach out for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            return redirect(reverse('premium:checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error in the form. \
                Please double check the input.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "The bag is currently empty")
            return redirect(reverse('shop:all_products'))

        current_bag = shopping_bag_contents(request)
        total = current_bag['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key has not been set.\
            Could it be missing in your environment?')

    template = 'premium/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)
    profile = Profile.objects.get(user=request.user)

    if request.user.is_authenticated:
        if profile == order.user_profile:
            # profile = Profile.objects.get(user=request.user)
            # # Attach the user's profile to the order
            # order.user_profile = profile
            # order.save()
            messages.success(request, 'Order is successful!')
        else:
            messages.warning(request, 'No access')
            return redirect(reverse('home:index'))
    else:
        messages.warning(request, 'Correct login needed to see order details')
        return redirect(reverse('home:index'))

    if 'bag' in request.session:
        del request.session['bag']

    template = 'premium/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
