# adopted and modified from course material
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    ''' User profile form'''

    class Meta:
        ''' Helper class'''
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        '''
        Add placeholders and classes by removing auto-generated
        labels and set autofocus on first field
        '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address': 'Street Address ',
        }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input'
                )
            self.fields[field].label = False