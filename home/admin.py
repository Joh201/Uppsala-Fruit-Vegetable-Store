
from django.contrib import admin
from .models import ContactUs


# class OrderLineItemAdminInline(admin.TabularInline):
#     model = OrderLineItem
#     readonly_fields = ('lineitem_total',)


class ContactUsAdmin(admin.ModelAdmin):

    ''' Handles customer contact for admin'''

    fields = ('full_name', 'email', 'phone_number', 'comment',)

    list_display = ('full_name', 'email', 'phone_number', 'comment',)

    ordering = ('full_name',)


admin.site.register(ContactUs, ContactUsAdmin)
