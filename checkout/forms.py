from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = ('form-control')
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label

        self.fields['user_profile'].widget = forms.HiddenInput()
        self.fields['order_total'].widget = forms.HiddenInput()
        self.fields['delivery_cost'].widget = forms.HiddenInput()
        self.fields['grand_total'].widget = forms.HiddenInput()
