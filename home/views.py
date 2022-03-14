from django.shortcuts import render
from profiles.models import Profile
from shop.models import Product
from profiles.models import ActiveCharacter


def index(request):
    """ A view to return the index page """
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
    else:
        profile = False
    membership = Product.objects.get(name="Premium Membership")
    character = ActiveCharacter.objects.get(user=request.user)

    context = {
        'profile': profile,
        'membership': membership,
        'character': character,
    }

    return render(request, 'home/index.html', context)
