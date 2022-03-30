from django import forms
from .models import Product
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    For superusers to add products
    """
    class Meta:
        """ Specify model and fields"""
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)
