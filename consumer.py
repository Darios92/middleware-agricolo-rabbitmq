import pika
import json

def callback(ch, method, properties, body):

    data = json.loads(body)

    print("Dato ricevuto:", data)

    if data["valore"] < 30:
        print(">>> Attivazione irrigazione")
    else:
        print(">>> Irrigazione non necessaria")

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='sensor_data')

channel.basic_consume(
    queue='sensor_data',
    on_message_callback=callback,
    auto_ack=True
)

print("Consumer avviato. In attesa di messaggi...")

channel.start_consuming()
