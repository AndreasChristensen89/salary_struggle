from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from premium.models import Order
from .forms import ProfileDetailsForm
from .models import Profile


def profile(request):
    """ A view to return the profile page """
    user_profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileDetailsForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile information updated')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid')
    else:
        form = ProfileDetailsForm(instance=user_profile)
    
    orders = user_profile.orders.all()
    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    View to show the order history
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'premium/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,   # So we can check if the user got there via the order history view
    }

    return render(request, template, context)
