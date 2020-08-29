from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
        ]

class RawProductForm(forms.Form):
    title       = forms.Charfield()
    description = forms.Charfield()
    price       = forms.DecimalField()