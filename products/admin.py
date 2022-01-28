from django.contrib import admin
from .models import Produce, Category


class ProduceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Produce, ProduceAdmin)
admin.site.register(Category, CategoryAdmin)
