from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    ''' A view that returns cart contents'''

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add the quantity of a product to cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the quantity of the produce"""

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if request.POST:

        if quantity > 0:
            cart[item_id] = quantity

        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Removes the produce from the shopping cart"""

    cart = request.session.get('cart', {})

    if request.POST:
        cart.pop(item_id)

    request.session['cart'] = cart
    return HttpResponse(status=200)

