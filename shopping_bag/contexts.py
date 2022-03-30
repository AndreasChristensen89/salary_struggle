from django.shortcuts import get_object_or_404
from shop.models import Product
from profiles.models import Profile, ActiveCharacter


def shopping_bag_contents(request):
    """
    context function that makes the shopping bag available
    across the entire application
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    character = False
    profile = False

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if profile.active_char and ActiveCharacter.objects.filter(user=request.user).exists():
            character = ActiveCharacter.objects.get(user=request.user)

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'profile': profile,
        'character': character,
    }

    return context
