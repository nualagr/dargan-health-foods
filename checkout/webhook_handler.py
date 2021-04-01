from django.http import HttpResponse


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
        Handle the payment_intent.succeeded webhook from Stripe.
        This will be send each time a user completes the payment process.
        """
        intent = event.data.object
        print(intent)
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
