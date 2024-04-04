import pika

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='inventory_queue')

# Publish a message to the queue
channel.basic_publish(exchange='', routing_key='inventory_queue', body='Message from producer')
print(" [x] Sent 'Hello World!'")
# Close connection
connection.close()
