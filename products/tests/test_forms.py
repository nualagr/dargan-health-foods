from django.test import TestCase
from ..models import Product
from ..forms import ProductForm, ProductReviewForm


class TestProductForm(TestCase):
    def create_product(
        self,
        name="test_product",
        friendly_name="Test Product",
        abbreviated_friendly_name="Product",
        price=0.00,
    ):
        """
        Function to create a Product for testing purposes.
        """
        return Product.objects.create(
            name=name,
            friendly_name=friendly_name,
            abbreviated_friendly_name=abbreviated_friendly_name,
            price=price,
        )

    def test_valid_form(self):
        """
        Test ProductForm validation.
        """
        form = ProductForm({
            "name": "test_product",
            "friendly_name": "Test Product",
            "price": 0.00,
        })
        self.assertTrue(form.is_valid())

    def test_price_is_required(self):
        """
        Test that the Price field within the
        ProductForm is required.
        """
        form = ProductForm({"price": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("price", form.errors.keys())
        self.assertEqual(
            form.errors["price"][0],
            "This field is required.")


class TestProductReviewForm(TestCase):
    def test_valid_productreviewform(self):
        """
        Test ProductReviewForm validation.
        """
        form = ProductReviewForm({
            "review_rating": int(5),
            "review_title": "Wonderful Product",
            "review_content": "I will definitely buy this again.",
        })
        self.assertTrue(form.is_valid())

    def test_productreviewform_required_fields(self):
        """
        Test ProductReviewForm required fields.
        """
        form = ProductReviewForm({
            "review_rating": "",
            "review_title": "",
            "review_content": "",
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["review_rating"][0], "This field is required.")
        self.assertEqual(
            form.errors["review_title"][0], "This field is required.")
        self.assertEqual(
            form.errors["review_content"][0], "This field is required.")
