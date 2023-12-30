from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Creates an admin user."

    def handle(self, *args, **options):
        if User.objects.filter(username="admin").exists():
            return

        User.objects.create_superuser(username="admin", password="admin")
        self.stdout.write("Admin user created.", self.style.SUCCESS)
