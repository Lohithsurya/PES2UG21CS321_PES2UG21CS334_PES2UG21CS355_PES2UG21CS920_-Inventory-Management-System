import pika
<<<<<<< HEAD
import json

RABBITMQ_HOST = 'rabbitmq'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'

def main():
    def callback(ch, method, properties, body):
        # Decode the message from bytes to string
        message = json.loads(body.decode())
        # Print the received message
        print("Received message from producer.py:", message)

    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=5672, credentials=pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()

    # Declare the queue to consume messages from
    channel.queue_declare(queue='health_check_queue')

    # Set up a consumer to receive messages
    channel.basic_consume(queue='health_check_queue', on_message_callback=callback, auto_ack=True)

    print("Consumer One waiting for health check messages. To exit press CTRL+C")
    # Start consuming messages
    channel.start_consuming()

if __name__ == '__main__':
    main()
=======

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
channel = connection.channel()

# Declare the same queue as the producer
channel.queue_declare(queue='inventory_queue')

# Define a callback function to process incoming messages
def callback(ch, method, properties, body):
    print("Received message:", body.decode())

# Start consuming messages from the queue
channel.basic_consume(queue='inventory_queue', on_message_callback=callback, auto_ack=True)

# Start consuming (blocking call)
print("Consumer waiting for messages. To exit press CTRL+C")
channel.start_consuming()
>>>>>>> 4e1c931086771419fea6341f07ef7b792a45991c
