import pika
import json

RABBITMQ_HOST = 'rabbitmq'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=5672, credentials=pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()
    channel.queue_declare(queue='item_management_queue')

    def callback(ch, method, properties, body):
        print("Consumer Three received item management message:", body.decode())
        # Implement item management functionality here
        # For example, parse the message to determine CRUD actions and update database accordingly
        try:
            # Assuming the message format is JSON
            item_management_data = json.loads(body.decode())
            # Placeholder: Update inventory based on the action received
            print("Item management operation performed successfully:", item_management_data)
        except Exception as e:
            print("Error processing item management message:", e)

    channel.basic_consume(queue='item_management_queue', on_message_callback=callback, auto_ack=True)

    print("Consumer Three waiting for item management messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    main()
