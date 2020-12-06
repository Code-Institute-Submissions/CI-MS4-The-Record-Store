from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from .forms import OrderForm
from profiles.models import UserProfile
from products.models import Product
from .models import Order, OrderLineItem
from profiles.forms import AddressForm
from profiles.views import Address_Manager
from django.conf import settings
from cart.contexts import cart_contents
import stripe
from django.contrib import messages
from django.views.decorators.http import require_POST
import json
# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        print(request.POST)
        cart = cart_contents(request)
        user = request.user
        pid = request.POST.get('client_secret').split('_secret')[0]
        original_request = request.POST.copy()
        updated_request = add_hidden_info(original_request, cart, user, pid)
        order_form = OrderForm(updated_request)

        if order_form.is_valid():
            print("Checkout Order Form Is Valid")
            order = order_form.save(commit=False)
            order.save()

            for cart_item in cart['cart_items']:
                product = Product.objects.get(id=cart_item['item_id'])
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=cart_item['quantity'],
                )
                order_line_item.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))

        else:
            print(order_form.errors)
    else:
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            user_primary_address = user_profile.primary_address
            order_form = OrderForm(instance=user_primary_address)
            order_form.fields["email"].initial = user_profile.user.email
        else:
            order_form = OrderForm()

        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            metadata={'integration_check': 'accept_a_payment'},
        )

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        if save_info:
            address_data = {'user': order.user_profile.user,
                            'first_name': order.first_name,
                            'last_name': order.last_name,
                            'address_line_1': order.address_line_1,
                            'address_line_2': order.address_line_2,
                            'town_or_city': order.town_or_city,
                            'county_or_province': order.county_or_province,
                            'country': order.country,
                            'post_code_or_zip_code':
                            order.post_code_or_zip_code,
                            'phone_number': order.phone_number,
                            'primary_address': True}
            address_form = AddressForm(address_data)
            if address_form.is_valid():
                print("address is valid")
                address_manager = Address_Manager()
                if address_manager.address_already_exists(address_form) \
                        is False:
                    address_manager.clear_previous_primary_address(
                        request.user)
                    address_form.save()
            else:
                print(address_form.errors)
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {'order': order,
               'hide_checkout_preview': True}
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    return render(request, template, context)


def add_hidden_info(original_request, cart, user, pid):

    if user.id is not None:
        original_request.update(
            {'user_profile': UserProfile.objects.get(user=user)})
    original_request.update(
        {'delivery_cost': cart['delivery_cost']})
    original_request.update(
        {'order_total': cart['total']})
    original_request.update(
        {'grand_total': cart['grand_total']})
    original_request.update(
        {'stripe_pid': pid})
    return original_request
