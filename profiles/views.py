from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import ProfileForm

from .models import Profile


def profile(request):
    """ A view to return the profile page """
    user_profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile information updated')
    
    orders = user_profile.orders.all()

    form = ProfileForm(instance=user_profile)
    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)
