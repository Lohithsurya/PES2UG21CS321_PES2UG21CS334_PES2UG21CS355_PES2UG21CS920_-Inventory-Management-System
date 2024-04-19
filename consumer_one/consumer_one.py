import pika
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
