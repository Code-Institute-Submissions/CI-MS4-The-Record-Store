from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the class and label on all fields in the form
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = ('form-control')
            if field != 'country':
                self.fields[field].widget.attrs['placeholder'] = (
                    self.fields[field].label)

        # Hide the fields that don't require user input
        self.fields['user_profile'].widget = forms.HiddenInput()
        self.fields['order_total'].widget = forms.HiddenInput()
        self.fields['delivery_cost'].widget = forms.HiddenInput()
        self.fields['grand_total'].widget = forms.HiddenInput()
