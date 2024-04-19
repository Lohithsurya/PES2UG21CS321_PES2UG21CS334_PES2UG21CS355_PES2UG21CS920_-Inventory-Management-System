import pika
<<<<<<< HEAD
import json

RABBITMQ_HOST = 'rabbitmq'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'

def main():
    def callback(ch, method, properties, body):
        print("Consumer Two received item creation message:", body.decode())
        # Implement item creation functionality here
        # For example, parse the message to extract item details and save them to database
        try:
            # Assuming the message format is JSON
            item_data = json.loads(body.decode())
            # Placeholder: Save item data to database
            print("Item created successfully:", item_data)
        except Exception as e:
            print("Error processing item creation message:", e)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=5672, credentials=pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()  
    channel.queue_declare(queue='item_creation_queue')

    channel.basic_consume(queue='item_creation_queue', on_message_callback=callback, auto_ack=True)

    print("Consumer Two waiting for item creation messages. To exit press CTRL+C")
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
