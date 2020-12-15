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

        # order_exists = False
        # attempt = 1
        # while attempt <= 5:
        #     try:
        #         print(f'Trying To Find Order attempt {attempt}')
        #         order = Order.objects.get(stripe_pid=pid, grand_total=grand_total)
        #         order_exists = True
        #         print('order already exists')
        #         break
        #     except Order.DoesNotExist:
        #         attempt += 1
        #         time.sleep(1)

        print("If the order exist just send and email")
        if order_exists:
            print('Order exists')
            self._send_confirmation_email(order)
            return HttpResponse(content=(f'Webhook received: {event["type"]} | SUCCESS: ' 'Verified order already in database'),status=200)
        else:
            print("Order doesn't exist")
        
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """

        return HttpResponse(content=f'Webhook received: Payment Succeeded {event["type"]}', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
