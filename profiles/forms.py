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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
