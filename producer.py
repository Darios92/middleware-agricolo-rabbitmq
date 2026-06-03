import pika
import json
import random
import time
from datetime import datetime

# Connessione a RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# Creazione della coda
channel.queue_declare(queue='sensor_data')

print("Producer avviato. Invio dati del sensore...")

while True:

    # Simulazione sensore di umidità
    data = {
        "sensore": "umidita",
        "valore": random.randint(20, 80),
        "timestamp": datetime.now().isoformat()
    }

    # Invio messaggio JSON
    channel.basic_publish(
        exchange='',
        routing_key='sensor_data',
        body=json.dumps(data)
    )

    print("Dato inviato:", data)

    time.sleep(5)
