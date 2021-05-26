from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from ..models import Order


class TestCheckoutSuccessView(TestCase):
    """
    Test checkout_success view status response
    and template used.
    """

    def test_checkout_success_view(self):
        order = Order.objects.create(
            full_name="Testy Test",
            email="testytest@example.com",
            phone_number="01555555",
            street_address1="No. 1 Some Street",
            town_or_city="Some Town",
            country="IE",
            date=timezone.now(),
            delivery_cost=0.00,
            order_total=50,
            grand_total=50,
            original_cart="",
            stripe_pid="0987654321",
        )
        order.save()
        response = self.client.get(
            reverse(("checkout_success"), args=(order.order_number,))
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
