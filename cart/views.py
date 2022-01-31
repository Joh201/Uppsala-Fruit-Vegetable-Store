from django.shortcuts import (render, redirect, reverse, HttpResponse,
                              get_object_or_404)
from django.contrib import messages
from products.models import Produce


def view_cart(request):
    ''' A view that returns cart contents'''

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add the quantity of a product to cart"""

    produce = get_object_or_404(Produce, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'updated {produce.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {produce.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the quantity of the produce"""

    produce = get_object_or_404(Produce, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if request.POST:

        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'updated {produce.name} quantity to {cart[item_id]}')

        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {produce.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Removes the produce from the shopping cart"""

    try:
        produce = get_object_or_404(Produce, pk=item_id)
        cart = request.session.get('cart', {})

        if request.POST:
            cart.pop(item_id)
            messages.success(request, f'Removed {produce.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
