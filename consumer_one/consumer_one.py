import pika, sys, os
import pika
import json
import psutil

def main():
# Establish connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

# Declare the same queue as the producer
    channel.queue_declare(queue='health_check_queue')

# Define a callback function to process incoming messages
    def callback(ch, method, properties, body):
        print("Received message:", body.decode())
        print("Consumer One received health check message:", body.decode())
        # Implement health check functionality here
        # For example, perform system health checks and log the results
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        health_data = {
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "disk_usage": disk_usage
        }

        print("Health check results:", health_data)

# Set up a consumer to receive messages
    channel.basic_consume(queue='health_check_queue', on_message_callback=callback, auto_ack=True)
    #print("Consumer waiting for messages. To exit press CTRL+C")
    print("Consumer One waiting for health check messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    main()





