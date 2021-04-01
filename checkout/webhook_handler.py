from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""
    # Assign the request as an attribute of the class
    # So attributes of the request coming from Stripe
    # can be accessed.
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        # Return a response indicating that it was received.
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe which will
        be sent each time a user successfully completes the payment process.
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Replace any empty strings from Stripe in Shipping Details with 'None'
        # this ensures the data is in the form necessary for the database -Null
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Assume the order does not exist
        order_exists = False
        attempt = 1
        # If the view is slow and hasn't created the Order by the time the
        # webhook is returned from Stripe - wait for 5 sec/5 attempts
        # before creating the Order.
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    # Use the iexact look-up field to make it an exact
                    # but case-insensitive match
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200,
            )
        else:
            # If the Order does not exist
            # Create an Order using the data from the paymentIntent
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
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
                    return HttpReponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500,
                    )
        print(intent)
        # If it gets to this point the Order must have been created
        # Send a response to Stripe indicating this.
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        which is sent in the event of the user's payment failing.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )