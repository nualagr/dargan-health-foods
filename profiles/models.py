from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A User Profile model for maintaining default
    shipping information and Order histories.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
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


# Since there is only going to be one signal it will be kept
# in the models.py file rather than in a separate signals file
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the User Profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing user - so save the profile to update it
    instance.userprofile.save()
