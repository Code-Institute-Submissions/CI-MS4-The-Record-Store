from django import forms
from .models import UserProfile, Address


class DefaultAddressForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['default_address', ]


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'
