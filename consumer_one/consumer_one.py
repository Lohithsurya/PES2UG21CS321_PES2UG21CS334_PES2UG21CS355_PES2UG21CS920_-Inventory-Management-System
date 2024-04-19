import pika

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
