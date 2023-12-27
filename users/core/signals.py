from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


@receiver(post_save, sender=User)
def queue_user_created(instance, created, **kwargs):
    if created:
        print("user created")
