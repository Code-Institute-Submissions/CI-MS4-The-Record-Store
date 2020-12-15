from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Address
from wishlist.views import update_wishlist
from .forms import DefaultAddressForm, AddressForm
from django.contrib import messages
# Create your views here.


@login_required
def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    addresses = Address.objects.filter(user=request.user)
    primary_address = None
    primary_address = profile.primary_address

    orders = profile.orders.all()
    context = {
        'profile': profile,
        'primary_address': primary_address,
        'orders': orders,
        'hide_checkout_preview': True
    }
    update_wishlist(request.user, request.session)
    return render(request, template, context)


@login_required
def addresses(request):
    template = 'profiles/addresses.html'
    addresses = Address.objects.filter(user=request.user)
    context = {
        'addresses': addresses
    }

    return render(request, template, context)


@login_required
def add_address(request):
    address_manager = Address_Manager()
    if request.method == 'POST':
        updated_request = request.POST.copy()
        updated_request.update({'user': request.user})
        form = AddressForm(updated_request)
        if form.is_valid():
            if form.cleaned_data['primary_address'] is True:
                address_manager.clear_previous_primary_address(request.user)
            new_primary_address = form.save()
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.primary_address = new_primary_address
            user_profile.save()
            return redirect(reverse('addresses'))
    else:
        form = AddressForm()

    template = 'profiles/add_address.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_address(request, item_id):
    address_manager = Address_Manager()
    address = get_object_or_404(Address, pk=item_id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            if form.cleaned_data['primary_address'] is True:
                address_manager.clear_previous_primary_address(request.user)
            new_primary_address = form.save()
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.primary_address = new_primary_address
            user_profile.save()
            return redirect(reverse('addresses'))
        else:
            messages.error(
                request, f'{form.errors}')
    else:
        form = AddressForm(instance=address)

    template = 'profiles/edit_address.html'
    context = {
        'form': form,
        'address': address,
    }

    return render(request, template, context)


@login_required
def delete_address(request, item_id):
    address = get_object_or_404(Address, pk=item_id)
    address.delete()
    return redirect(reverse('addresses'))


class Address_Manager:

    def clear_previous_primary_address(self, user):
        previous_primary_address = (
            Address.objects.filter(primary_address=True).first())
        if(previous_primary_address):
            previous_primary_address.primary_address = False
            previous_primary_address.save()

    # Check is address already exist in the database
    def address_already_exists(self, address_form):
        if Address.objects.filter(
                first_name=address_form['first_name'].value(),
                last_name=address_form['last_name'].value(),
                address_line_1=address_form['address_line_1'].value(),
                address_line_2=address_form['address_line_2'].value(),
                town_or_city=address_form['town_or_city'].value(),
                county_or_province=address_form['county_or_province'].value(),
                country=address_form['country'].value(),
                post_code_or_zip_code=address_form['post_code_or_zip_code'
                                                   ].value(),
                phone_number=address_form['phone_number'].value()).exists():
            return True
        else:
            return False
