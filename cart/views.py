from django.shortcuts import render


def view_cart(request):
    ''' A view that returns cart contents'''

    return render(request, 'cart/cart.html')
