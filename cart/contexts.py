# adopted and modified from course material
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Produce


def cart_contents(request):
    ''' Function for displaying cart contents'''

    cart_items = []
    total = 0
    produce_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        produce = get_object_or_404(Produce, pk=item_id)
        total += quantity * produce.price
        produce_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'produce': produce,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'produce_count': produce_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
