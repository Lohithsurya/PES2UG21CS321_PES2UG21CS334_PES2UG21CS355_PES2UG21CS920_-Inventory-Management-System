import pika
import json
import psutil

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='inventory_queue')

    def callback(ch, method, properties, body):
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

    channel.basic_consume(queue='inventory_queue', on_message_callback=callback, auto_ack=True)

    print("Consumer One waiting for health check messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    main()
