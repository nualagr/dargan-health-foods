from django.test import TestCase


class TestCartView(TestCase):
    def test_cart_view(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the cart page.
        """
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")
