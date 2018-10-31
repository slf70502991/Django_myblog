from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Product

def validate_even(value):
    if value <0 :
        raise forms.ValidationError(
            _('Price should not be smaller than 0.'),
            params={'value': value},
        )

class ProductModelForm(forms.ModelForm):
    img= forms.ImageField(label='Image')
    price = forms.IntegerField(validators=[validate_even])
    class Meta:
        model = Product
        fields = [
            'name',
            'img',
            'price',
            'description'
        ]

