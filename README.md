# Middleware Asincrono per l'Integrazione dei Sistemi nel Settore Agricolo

Progetto realizzato per il Project Work del corso di Laurea in Informatica per le Aziende Digitali (L-31).

## Obiettivo

Realizzare un middleware orientato allo scambio di messaggi asincroni per l'integrazione di sistemi eterogenei in ambito agricolo.

## Tecnologie utilizzate

- Python
- RabbitMQ
- JSON
- Pika

## Architettura

Producer → RabbitMQ → Consumer

Il producer simula un sensore di umidità del terreno.

RabbitMQ riceve e gestisce i messaggi.

Il consumer elabora i dati e simula l'attivazione dell'irrigazione.

## File del progetto

- producer.py
- consumer.py

## Caso d'uso

Irrigazione intelligente tramite sensori IoT e comunicazione asincrona.

## Autore

Dario Salemi
