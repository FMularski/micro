from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .publisher import Publisher

User = get_user_model()
publisher = Publisher()


@receiver(post_save, sender=User)
def queue_user_created(instance, created, **kwargs):
    if not created or not instance.email:
        return

    body = {
        "username": instance.username,
        "email": instance.email,
    }

    publisher.publish(
        msg=body,
        exchange="email",
        queue="user-created",
        routing_key="user-created",
    )
