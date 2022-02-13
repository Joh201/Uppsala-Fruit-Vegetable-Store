from django.contrib import admin
from .models import Produce, Category


class ProduceAdmin(admin.ModelAdmin):
    ''' produce admin'''
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    '''category admin'''
    list_display = ('name',)


admin.site.register(Produce, ProduceAdmin)
admin.site.register(Category, CategoryAdmin)
