from django.shortcuts import render
from profiles.models import Profile
from shop.models import Product
from profiles.models import ActiveCharacter


def index(request):
    """ A view to return the index page """

    character = False
    profile = False

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if profile.active_char:
            character = ActiveCharacter.objects.get(user=request.user)

    membership = Product.objects.get(name="Premium Membership")

    context = {
        'profile': profile,
        'membership': membership,
        'character': character,
    }

    return render(request, 'home/index.html', context)
