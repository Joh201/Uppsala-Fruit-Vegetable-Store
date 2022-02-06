from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUsForm


def index(request):
    ''' A view to return the home page'''

    return render(request, 'home/index.html')


def contact_us(request):
    ''' A view to return the contact us page'''

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for your comments!')

    contact_form = ContactUsForm()
    context = {
        'contact_form': contact_form
    }

    return render(request, 'home/contact_us.html', context)
