from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

from cart.models import DiscountCode

import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


class UserProfile(models.Model):
    """
    A User Profile model for maintaining default
    shipping information and Order histories.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label="Country *", null=True, blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the User Profile
    On creation, create an associated DiscountCode2User
    so that user's can get 10% off their next order with the
    promo code NEW10.
    """
    if created:
        new_user = UserProfile.objects.create(user=instance)
        new_user_discount_code = DiscountCode.objects.get(
            discount_code="NEW10"
        )
        DiscountCode2User.objects.create(
            user=new_user, discount_code=new_user_discount_code
        )
        logger.info(
                f"{new_user}s profile created."
            )
    # Existing user - so save the profile to update it
    instance.userprofile.save()
    logger.info("Profile updated.")


class DiscountCode2User(models.Model):
    discount_code = models.ForeignKey(
        DiscountCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return f"{self.user}'s {self.discount_code}, Valid: {self.active}"
