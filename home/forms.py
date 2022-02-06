from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):

    '''Contact us form'''
    class Meta:
        ''' Helper class'''

        model = ContactUs
        fields = '__all__'

# adopted and modified from course material
    def __init__(self, *args, **kwargs):

        '''
        Add placeholders and classes by removing auto-generated
        labels and set autofocus on first field
        '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'comment': 'Comments or Messages',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False