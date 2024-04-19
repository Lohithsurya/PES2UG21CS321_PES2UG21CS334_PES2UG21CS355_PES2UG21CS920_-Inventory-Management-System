import pika
import json

RABBITMQ_HOST = 'rabbitmq'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'

def main():
    def callback(ch, method, properties, body):
        print("Consumer Four received order creation message:", body.decode())
        # Implement order creation functionality here
        # For example, parse the message to extract order details and save them to database
        try:
            # Assuming the message format is JSON
            order_data = json.loads(body.decode())
            # Placeholder: Save order data to database
            print("Order created successfully:", order_data)
        except Exception as e:
            print("Error processing order creation message:", e)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=5672, credentials=pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()  
    channel.queue_declare(queue='order_management_queue')

    channel.basic_consume(queue='order_management_queue', on_message_callback=callback, auto_ack=True)

    print("Consumer Four waiting for order creation messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    main()
