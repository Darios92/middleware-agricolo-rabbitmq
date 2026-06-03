# Middleware agricolo RabbitMQ

Progetto sviluppato per il Project Work:

"Middleware asincrono per l'integrazione dei sistemi nel settore agricolo"

## Tecnologie utilizzate

- Python 3
- RabbitMQ
- Pika

## File presenti

- producer.py
- consumer.py

## Descrizione

Il producer simula un sensore di umidità del terreno e invia dati JSON ad una coda RabbitMQ.

Il consumer riceve i dati e simula l'attivazione dell'irrigazione quando il valore di umidità scende sotto una soglia prestabilita.
