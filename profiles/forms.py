from django import forms
from .models import UserProfile

class DefaultAddressForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['default_address',]