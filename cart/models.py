from django.db import models


class DiscountCode(models.Model):
    discount_code = models.CharField(max_length=30)
    percentage_discount = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return f"PromoCode: {self.discount_code}, {self.percentage_discount}% Discount"
