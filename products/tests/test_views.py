from django.test import TestCase
from django.urls import reverse
from ..models import Product


class TestProductsView(TestCase):

    def test_all_products_view(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the products page.
        """
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_get_product_detail_view(self):
        """
        Test for status code 200 response and correct
        template rendered when getting an individual
        product_detail page.
        """
        p = Product.objects.create(price=0.00)
        p.save()
        response = self.client.get(reverse(("product_detail"), args=(p.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")
