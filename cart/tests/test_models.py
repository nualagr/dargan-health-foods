from django.test import TestCase
from ..models import DiscountCode


class TestDiscountCodeModel(TestCase):
    def create_discount_code(
        self,
        discount_code="TESTCODE",
        percentage_discount=25,
    ):
        """
        Function to create a DiscountCode for testing purposes.
        """
        return DiscountCode.objects.create(
            discount_code=discount_code,
            percentage_discount=percentage_discount
        )

    def test_discount_code_creation(self):
        """
        Test that DiscountCodes are created using the
        DiscountCode model.
        """
        dc = self.create_discount_code()
        self.assertTrue(isinstance(dc, DiscountCode))

    def test_discount_code_string_method(self):
        """
        Test that DiscountCodes return the correct string.
        """
        dc = self.create_discount_code()
        self.assertEqual(str(dc), "PromoCode: TESTCODE, 25% Discount")
