from django.test import TestCase
from ..forms import OrderForm


class TestOrderForm(TestCase):
    def test_valid_form(self):
        """
        Test OrderForm validation.
        """
        form = OrderForm(
            {
                "full_name": "Testy Test",
                "email": "testytest@example.com",
                "street_address1": "No. 1 Some Street",
                "town_or_city": "Some Town",
                "country": "IE",
                "phone_number": "01555555",
            }
        )
        self.assertTrue(form.is_valid())

    def test_required_fields(self):
        """
        Test OrderForm required fields.
        """
        form = OrderForm(
            {
                "full_name": "",
                "email": "",
                "street_address1": "",
                "town_or_city": "",
                "country": "",
                "phone_number": "",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["full_name"][0], "This field is required."
        )
        self.assertEqual(form.errors["email"][0], "This field is required.")
        self.assertEqual(
            form.errors["town_or_city"][0], "This field is required."
        )
        self.assertEqual(form.errors["country"][0], "This field is required.")
        self.assertEqual(
            form.errors["phone_number"][0], "This field is required."
        )
