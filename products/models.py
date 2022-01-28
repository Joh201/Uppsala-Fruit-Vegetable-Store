from django.db import models


class Category(models.Model):
    class Meta:
        ''' Helper class'''
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Produce(models.Model):
    ''' model for the produce '''
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name