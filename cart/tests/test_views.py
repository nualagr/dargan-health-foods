from django.test import TestCase


class TestCartView(TestCase):
    """
    Tests for views.
    Renders templates in cart app
    """

    def test_view_cart(self):
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")
