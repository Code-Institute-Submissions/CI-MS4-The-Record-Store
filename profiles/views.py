from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Address
from .forms import DefaultAddressForm
# Create your views here.


@login_required
def profile(request):
    
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    addresses = Address.objects.filter(user=request.user)
    form = DefaultAddressForm()
    form.fields['default_address'].choices = [(address.pk, address.address_line_1) for address in addresses]
    context = {
        'profile' : profile,
        'form' : form
    }

    return render(request, template, context)

@login_required
def addresses(request):
    template = 'profiles/addresses.html'
    addresses = Address.objects.filter(user=request.user)
    print(addresses)
    context = {
        'addresses': addresses
    }

    return render(request, template, context)