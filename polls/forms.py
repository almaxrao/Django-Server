import re

from django.contrib.auth.models import User
from django import forms
from .models import Profile

from .models import Product



class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']    


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password')


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('product_name','product_price','product_detail')