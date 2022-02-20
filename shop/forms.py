from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """
    For superusers to add products
    """
    class Meta:
        """ Specify model and fields"""
        model = Product
        fields = '__all__'
