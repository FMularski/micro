from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import publisher

User = get_user_model()


@receiver(post_save, sender=User)
def queue_user_created(instance, created, **kwargs):
    if not created:
        return

    body = {
        "username": instance.username,
        "email": instance.email,
    }

    publisher.publish(
        method="user_created",
        body=body,
        routing_key="user_created",
        exchange="email",
        queue="user-created",
    )
