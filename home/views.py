from django.shortcuts import render
# from django.contrib import messages
from .forms import ContactUsForm


def index(request):
    ''' A view to return the home page'''

    return render(request, 'home/index.html')


def contact_us(request):
    ''' A view to return the contact us page'''

    contact_form = ContactUsForm()
    context = {
        'contact_form': contact_form
    }

    return render(request, 'home/contact_us.html', context)
