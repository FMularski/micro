import json

import pika
from core import tasks
from django.conf import settings


class Consumer:
    """
    Class consuming messages from queues.
    """

    QUEUES_CALLBACKS = {
        "user-created": "send_welcome_email",
        # more queues
        # ...
    }

    def __init__(self):
        self._params = pika.URLParameters(settings.MQ_URL)
        self._conn = None
        self._channel = None

    def connect(self):
        if not self._conn or self._conn.is_closed:
            self._conn = pika.BlockingConnection(self._params)
            self._channel = self._conn.channel()

    def send_welcome_email(self, channel, method, properties, body):
        print("Consuming message from queue: user-created")
        print("Firing callback: send_welcome_email")

        decoded = body.decode()
        username, email = json.loads(decoded).values()

        tasks.queue_welcome_email.delay(username, email)

    def _bind_queues_to_callback(self):
        for queue, callback in self.QUEUES_CALLBACKS.items():
            self._channel.basic_consume(queue, getattr(self, callback), auto_ack=True)

    def consume(self):
        self._bind_queues_to_callback()
        self._channel.start_consuming()

    def close(self):
        if self._conn and self._conn.is_open:
            self._conn.close()
