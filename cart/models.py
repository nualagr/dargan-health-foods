from django.db import models


class DiscountCode(models.Model):
    code = models.CharField(max_length=30)
    discount_amount = models.FloatField()

    def __str__(self):
        return f"Code:{self.code}, {self.discount_amount}% discount"
