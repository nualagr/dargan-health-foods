from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from cart.models import DiscountCode
from products.models import Product
from profiles.models import UserProfile, DiscountCode2User

import json
import time
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    Code taken from the Code Institute Boutique Ado project
    and then modified.
    """

    # Assign the request as an attribute of the class
    # So attributes of the request coming from Stripe
    # can be accessed.
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Check to see whether a discount code was used.
        If so, render the discounted amount within the email.
        Send the user a confirmation email.
        """
        cust_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order},
        )
        if order.discount_code is not None:
            discount_code = order.discount_code
            discount_amount = f"-€{order.discount_amount}"
        else:
            discount_code = ""
            discount_amount = ""
        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {
                "order": order,
                "discount_code": discount_code,
                "discount_amount": discount_amount,
                "contact_email": settings.DEFAULT_FROM_EMAIL,
            },
        )
        # The subject, body and from email are strings.
        # The cust_email list is a list of strings.
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        # Return a response indicating that it was received.
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe which will
        be sent each time a user successfully completes the payment process.
        """
        intent = event.data.object
        pid = intent.id
        # Get the cart info added in checkout/views.py cache_checkout_data
        cart = intent.metadata.cart
        discount = intent.metadata.discount
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Replace any empty strings from Stripe in Shipping Details with 'None'
        # this ensures the data is in the form necessary for the database -Null
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile info if save_info box was checked
        # Set profile to none so that anonymous users can checkout
        profile = None
        # Get username added in checkout/views.py cache_checkout_data
        username = intent.metadata.username
        # If the user is logged in
        if username != "AnonymousUser":
            logger.info(f"Searching the database for {username}s profile.")
            profile = UserProfile.objects.get(user__username=username)
            if save_info is True:
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address1 = (
                    shipping_details.address.line1
                )
                profile.default_street_address2 = (
                    shipping_details.address.line2
                )
                profile.default_town_or_city = shipping_details.address.city
                profile.default_county = shipping_details.address.state
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.save()
                logger.info(f"Updated {username}s default profile info.")

        # Assume the order does not exist
        order_exists = False
        attempt = 1
        # If the view is slow and hasn't created the Order by the time the
        # webhook is returned from Stripe - wait for 5 sec/5 attempts
        # before creating the Order.
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    stripe_pid=pid,
                )
                order_exists = True
                logger.info(f"Order {pid} found in the database.")
                break
            except Order.DoesNotExist:
                attempt += 1
                logger.info(
                    f"Attempt {attempt} to find Order {pid} in the database"
                )
                time.sleep(1)
        if order_exists:
            # Check if the customer was a logged in site member
            if username != "AnonymousUser":
                profile = UserProfile.objects.get(user__username=username)
                # If a discount code was used, deactivate it
                if order.discount_code:
                    discount = order.discount_code
                    discount_code_object = get_object_or_404(
                        DiscountCode, discount_code=discount.discount_code
                    )
                    discount_code_2_user = DiscountCode2User.objects.get(
                        user=profile, discount_code=discount_code_object
                    )
                    discount_code_2_user.active = False
                    discount_code_2_user.save()
            # Send the confirmation email
            self._send_confirmation_email(order)
            logger.info(f"Confirmation email sent for database Order {pid}.")
            return HttpResponse(
                content=f"Webhook received: {event['type']} | \
                    SUCCESS: Verified order already in database",
                status=200,
            )
        else:
            # If the Order does not exist
            # Create an Order using the data from the paymentIntent
            order = None
            logger.info(f"Order {pid} not found in database.")
            discount = json.loads(discount)
            # If there was no discount code in the metadata
            # Set the discount_code_object variable to None
            # So that an exception is not raised
            if not discount:
                discount_code_object = None
            else:
                discount_code_object = DiscountCode.objects.get(
                    pk=discount["discount_code_id"]
                )
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    # Attach the profile which will be full if they were
                    # logged in or set to None if they are an anonymous user.
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    discount_code=discount_code_object,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                logger.info(f"Order {pid} created in the webhook_handler.")
                # Iterate through the cart items in the JSON version
                # in the paymentIntent
                for item_id, quantity in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f"Webhook received: {event['type']} | \
                        ERROR: {e}",
                    status=500,
                )

        # If it gets to this point the Order has been created
        # Check to see whether the user was logged in
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            # If a discount code was used, deactivate it
            if order.discount_code:
                discount = order.discount_code
                discount_code_object = get_object_or_404(
                    DiscountCode, discount_code=discount.discount_code
                )
                discount_code_2_user = DiscountCode2User.objects.get(
                    user=profile, discount_code=discount_code_object
                )
                discount_code_2_user.active = False
                discount_code_2_user.save()
        # Send the confirmation email and send a response to Stripe.
        self._send_confirmation_email(order)
        logger.info(f"Confirmation email sent for webhook Order {pid}.")
        return HttpResponse(
            content=f"Webhook received: {event['type']} | \
                SUCCESS: Created the order in the webhook",
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        which is sent in the event of the user's payment failing.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )
