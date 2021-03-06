import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile
from cart.models import DiscountCode

# Order and OrderLineItem Models taken from the
# Code Institute Boutique Ado walkthrough project:
# https://github.com/nualagr/boutique-ado-v1 - and then modified


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    # A User's orders can be accessed by calling user.userprofile.orders
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    discount_code = models.ForeignKey(
        DiscountCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    discount_amount = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_cart = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=""
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added.
        Check if discount code has been entered and if so, apply the discount.
        Check to see if order is over the free delivery threshold.
        """
        # if all the line items from an order are deleted
        # the order will be set to zero instead of None.
        # This prevents errors when comparing the total
        # to the free delivery threshold.
        self.order_total = (
            self.lineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"
            ] or 0
        )
        if self.discount_code:
            self.discount_amount = (
                self.order_total * self.discount_code.percentage_discount
            )
            self.order_total -= self.discount_amount

        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = round(
                (
                    self.order_total *
                    settings.STANDARD_DELIVERY_PERCENTAGE / 100
                ), 2,
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    product_price_paid = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False,
        default=0,
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def get_total_lineitem_price(self):
        return self.quantity * self.product.price

    def get_total_discount_lineitem_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return (
            self.get_total_lineitem_price() -
            self.get_total_discount_lineitem_price()
        )

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_discount_lineitem_price()
        return self.get_total_lineitem_price()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        if self.product.discount_price and self.product.on_offer:
            self.product_price_paid = self.product.discount_price
            self.lineitem_total = self.product.discount_price * self.quantity
        else:
            self.product_price_paid = self.product.price
            self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU {self.product.sku} on order {self.order.order_number}"
