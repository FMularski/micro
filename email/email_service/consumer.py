import pika
from django.conf import settings


class Consumer:
    def __init__(self):
        self._params = pika.URLParameters(settings.MQ_URL)
        self._conn = None
        self._channel = None

    def connect(self):
        self._conn = pika.BlockingConnection(self._params)
        self._channel = self._conn.channel()

    def send_welcome_email(self, channel, method, properties, body):
        print("CONSUMER: sending email...")

    def consume(self):
        self._channel.basic_consume("user-created", self.send_welcome_email, auto_ack=True)
        self._channel.start_consuming()
