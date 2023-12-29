from django.core.management.base import BaseCommand
from email_service.consumer import Consumer


class Command(BaseCommand):
    help = "Starts AMQP consumer."

    def handle(self, *args, **options):
        self.stdout.write("Starting AMQP consumer...", self.style.WARNING)

        consumer = Consumer()
        consumer.connect()
        consumer.consume()
