from django import forms
from .models import UserCart
from django.db import models
from django.contrib.postgres.fields import ArrayField


class UserCartForm (forms.ModelForm):
    cart_products = ArrayField(
        models.IntegerField(blank=True),
    )
    class Meta:
        model= UserCart
        fields=('user_cart','cart_products')