import pika
import json
import random
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='sensor_data')

while True:
    data = {
        "umidita": random.randint(20, 80)
    }

    channel.basic_publish(
        exchange='',
        routing_key='sensor_data',
        body=json.dumps(data)
    )

    print("Dato inviato:", data)

    time.sleep(5)
