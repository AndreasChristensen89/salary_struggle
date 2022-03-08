from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Order form for the Order Model
    """

    class Meta:
        """
        Meta class to specify model and fields
        """
        model = Order
        # fields = ('full_name', 'email', 'phone_number',
        #           'street_address1', 'street_address2',
        #           'town_or_city', 'postcode', 'country',
        #           'county',)
        fields = ('full_name', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, replace auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            # 'phone_number': 'Phone Number',
            # 'postcode': 'Postal Code',
            # 'town_or_city': 'Town or City',
            # 'street_address1': 'Street Address 1',
            # 'street_address2': 'Street Address 2',
            # 'county': 'County, state, or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
