from allauth.account.forms import SignupForm
from profiles.models import UserProfile
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):

        print("Custsom Save")
        user = super(CustomSignupForm, self).save(request)
        new_user_profile = UserProfile()
        new_user_profile.user = user
        new_user_profile.save()
        return user

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
