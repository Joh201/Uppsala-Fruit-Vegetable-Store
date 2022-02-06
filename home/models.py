from django.db import models


class ContactUs(models.Model):

    ''' A model for customers to leave their comments about
        produce and services '''

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    comment = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.full_name


