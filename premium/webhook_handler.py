import json
import time

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from profiles.models import Profile
from shop.models import Product
from .models import Order, OrderItem


class StripeWHookHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'premium/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'premium/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        pid = intent.id
        bag = intent.metadata.bag

        billing_details = intent.charges.data[0].billing_details
        order_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        # for field, value in shipping_details.address.items():
        #     if value == "":
        #         shipping_details.address[field] = None  # Need Null in the DB

        # Update profile information if save_info was checked
        profile = None  # allows anonymous users to check out
        username = intent.metadata.username
        if username != 'AnonymousUser':     # -> know they're authenticated
            profile = Profile.objects.get(user__username=username)

        order_exists = False    # first we assume that order doesn't exist
        attempt = 1     # If the view is slow for some reason, we introduce some delay 
        while attempt <= 5:
            try:
                order = Order.objects.get(  # Try to get the order with the info from the payment intent
                    full_name__iexact=billing_details.name,    # iexact to find exact match but case insentitve
                    email__iexact=billing_details.email,
                    order_total=order_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True # if order is found we set this to true...
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)   # Will look for the order 5 times over 5 seconds, before giving up and creating the order itself
        if order_exists:    # ... and return a 200 response if it exist
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200) # At this point we know the order has been created by the wh, so we return a response to Stripe
        else:   # ... otherwise we'll create the order
            order = None
            try:
                order = Order.objects.create(   # we don't have a form to save, so we use order.create instead
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                # code taken from view that creates the order, but bag.items is changed...
                for item_id, item_data in json.loads(bag).items():  # ... to json version from the payment intent
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                    if product.name == "Premium Membership":
                        profile.paid = True
                        profile.save()
            except Exception as e:  # delete the order if it was created
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)     # return 500 error, which will cause Stripe to try again later
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
