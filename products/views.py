from django.shortcuts import render
from .models import Produce


def all_produce(request):
    ''' A view for all produce and search queries'''

    products = Produce.objects.all()

    context = {
        'products':  products,
    }

    return render(request, 'products/produce.html', context)


