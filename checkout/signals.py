from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# Code taken from Code Institute Boutique Ado walkthrough project


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the Order Total every time an OrderLineItem
    is created or updated.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the Order Total every time an OrderLineItem
    is deleted.
    """
    instance.order.update_total()
