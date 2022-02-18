from django.db.models.signals import post_save, post_delete
# post_save means signals are sent after an instance is saved, and deleted respectively
from django.dispatch import receiver

from .models import OrderItem

# signals create a way to call the update method from the OrderItem
# this way the total can be update along the way


@receiver(post_save, sender=OrderItem)  # this tells us we're getting signals from OrderItem
def update_on_save(sender, instance, created, **kwargs):
    """
    Handles signals from the post_save event
    Update order total on orderitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on orderitem delete
    """
    instance.order.update_total()
