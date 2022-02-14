from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product


def shopping_bag_contents(request):
    """ context function that makes the shopping bag available across the entire application """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'product_id': product.id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
