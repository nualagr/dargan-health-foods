from django.test import TestCase
from ..forms import DiscountCodeForm


class TestDiscountCodeForm(TestCase):
    def test_valid_form(self):
        """
        Test DiscountCodeForm validation.
        """
        form = DiscountCodeForm({
            "discount_code": "TESTCODE",
            "percentage_discount": 25,
        })
        self.assertTrue(form.is_valid())
