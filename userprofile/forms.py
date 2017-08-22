from django import forms
from .models import UserProfile2

class UserProfileForm (forms.ModelForm):

    class Meta:
        model= UserProfile2
        fields=('user_address','user_phone')