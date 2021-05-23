from django.test import TestCase
from django.utils import timezone
from ..models import Order, OrderLineItem
from products.models import Product


class TestOrderModels(TestCase):
    def create_product(self):
        """
        Function to create a Product for testing purposes.
        """
        return Product.objects.create(
            name="test_product",
            price=9.99,
            sku="test_sku"
        )

    def create_order(self):
        """
        Function to create an Order for testing purposes.
        """
        return Order.objects.create(
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

    def test_order_creation(self):
        """
        Test the creation of an Order model.
        """
        o = self.create_order()
        self.assertTrue(isinstance(o, Order))
        self.assertEqual("testytest@example.com", o.email)

    def test_order_string_method(self):
        """
        Test that Order models return the correct string.
        """
        o = self.create_order()
        self.assertEqual(str(o), o.order_number)

    def test_orderlineitem_creation(self):
        """
        Test the creation of an OrderLineItem object.
        """
        p = self.create_product()
        o = self.create_order()

        orderlineitem = OrderLineItem.objects.create(
            order=o,
            product=p,
            product_price_paid=9.99,
            quantity=1,
            lineitem_total=9.99,
        )
        orderlineitem.save()
        self.assertTrue(isinstance(orderlineitem, OrderLineItem))

    def test_orderlineitem_string_method(self):
        """
        Test that OrderLineItems return the correct string.
        """
        p = self.create_product()
        o = self.create_order()

        orderlineitem = OrderLineItem.objects.create(
            order=o,
            product=p,
            product_price_paid=9.99,
            quantity=1,
            lineitem_total=9.99,
        )
        orderlineitem.save()
        self.assertEqual(
            str(orderlineitem),
            f"SKU {p.sku} on order {o.order_number}")

    def test_orderlineitem_get_total_lineitem_price_method(self):
        """
        Test that the OrderLineItem method get_total_lineitem_price
        returns the correct price.
        """
        p = self.create_product()
        o = self.create_order()

        oli = OrderLineItem.objects.create(
            order=o,
            product=p,
            product_price_paid=9.99,
            quantity=1,
            lineitem_total=9.99,
        )
        oli.save()
        self.assertEqual(oli.get_total_lineitem_price(), 9.99)
