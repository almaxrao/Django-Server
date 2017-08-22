import re

from django.contrib.auth.models import User
from django import forms


from APIs.models import Product




class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('product_name','product_price','product_detail')