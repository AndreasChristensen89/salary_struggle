from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .forms import ProfileForm
from premium.models import Order
# from .forms import ProfileDetailsForm
from .models import Profile
from .models import ActiveCharacter
from shop.models import Product


@login_required
def profile(request):
    """ A view to return the profile page """
    user_profile = get_object_or_404(Profile, user=request.user)
    membership = Product.objects.get(name="Premium Membership")

    orders = user_profile.orders.all()
    template = 'profiles/profiles.html'
    context = {
        'orders': orders,
        'on_profile_page': True,
        'membership': membership,
    }

    return render(request, template, context)


class UpdateProfile(SuccessMessageMixin, generic.UpdateView):
    """
    View and update user profile
    """
    form_class = ProfileForm
    template_name = 'profiles/update_profile.html'
    success_message = 'Profile updated successfully!'
    success_url = '/profile/'

    def get_object(self):
        return self.request.user


@login_required
def confirm_new_char(request):
    """ 
    Makes user confirm that old character is deleted,
    and new one is created 
    """

    return render(request, 'profiles/restart_character.html')


@login_required
def create_new_character(request):
    """ Delete a product from the store """

    ActiveCharacter.create_new_character(request.user)
    return redirect(reverse('profiles:profile'))


def order_history(request, order_number):
    """
    View to show the order history
    """
    order = get_object_or_404(Order, order_number=order_number)
    profile = Profile.objects.get(user=request.user)

    if request.user.is_authenticated:
        if not profile == order.user_profile:
            messages.warning(request, 'Access restricted')
            return redirect(reverse('home:index'))

    template = 'premium/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,   # So we can check if the user got there via the order history view
    }

    return render(request, template, context)
