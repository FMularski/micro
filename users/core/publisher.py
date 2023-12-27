import json

import pika
from django.conf import settings

params = pika.URLParameters(settings.MQ_URL)
connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body, routing_key, queue="", exchange="", exchange_type="direct"):
    channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)
    channel.queue_declare(queue=queue)
    channel.queue_bind(queue, exchange, routing_key=routing_key)

    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange=exchange, routing_key=routing_key, body=json.dumps(body), properties=properties
    )
