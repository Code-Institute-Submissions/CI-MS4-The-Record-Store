from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from profiles.forms import AddressForm
from profiles.views import Address_Manager
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from django.conf import settings
import re
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        print(f"sending email to {cust_email}")
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print("Handle Payment Intent Succeeded")
        intent = event.data.object
        pid = intent.id
        billing_details = intent.charges.data[0].billing_details
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        grand_total = round(intent.charges.data[0].amount / 100, 2)




        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            print(profile)
            if save_info:
                address_data = {
                    'user': profile.user,
                    'first_name':(re.search('(.*) ', billing_details.name,)).group(1),
                    'last_name':(re.search(' (.*)', billing_details.name,)).group(1),
                    'address_line_1': billing_details.address.line1,
                    'address_line_2': billing_details.address.line2,
                    'town_or_city': billing_details.address.city,
                    'county_or_province': billing_details.address.state,
                    'country': billing_details.country,
                    'post_code_or_zip_code': billing_details.address.postal_code,
                    'phone_number': billing_details.phone,
                    'primary_address': True}
                print(address_data)
                address_form = AddressForm(address_data)
                address_manager = Address_Manager()
                if (address_manager.address_already_exists(address_form) is False):
                    address_manager.clear_previous_primary_address(profile.user)
                    address_form.save()
                print('address saved')

        
        print('check if order exists already')
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                print(f'Trying To Find Order attempt {attempt}')
                order = Order.objects.get(stripe_pid=pid, grand_total=grand_total)
                order_exists = True
                print('order already exists')
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        print("If the order exist just send and email")
        if order_exists:
            print('Order exists')
            self._send_confirmation_email(order)
            return HttpResponse(content=(f'Webhook received: {event["type"]} | SUCCESS: ' 'Verified order already in database'),status=200)
        else:
            order = None
            try:
                print('Try To Create The Order')
                order = Order.objects.create(
                    first_name=profile.user.first_name,
                    second_name=profile.user.second_name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    stripe_pid=pid,
                )
                print('Add Line Items')
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,)
                    order_line_item.save()
            except Exception as e:
                print("Error Creating Order")
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} | ERROR: {e}', status=500)
            self._send_confirmation_email(order)
            return HttpResponse(content=(f'Webhook received: {event["type"]} | SUCCESS: ''Created order in webhook'),status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
