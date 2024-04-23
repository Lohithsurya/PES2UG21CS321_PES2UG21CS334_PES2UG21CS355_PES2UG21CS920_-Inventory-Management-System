import pika, sys, os
import pika
import json

def main():
# Establish connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

# Declare the same queue as the producer
    channel.queue_declare(queue='item_management_queue')

# Define a callback function to process incoming messages
    def callback(ch, method, properties, body):
        print("Received message:", body.decode())
        print("Consumer Three received item management message:", body.decode())
        # Implement stock management functionality here
        # For example, parse the message to determine stock update actions and update database accordingly
        try:
            # Assuming the message format is JSON
            stock_update_data = json.loads(body.decode())
            # Placeholder: Update stock in database
            print("Item management operation performed successfully:", stock_update_data)
        except Exception as e:
            print("Error processing item management message:", e)

    channel.basic_consume(queue='item_management_queue', on_message_callback=callback, auto_ack=True)
    #print("Consumer waiting for messages. To exit press CTRL+C")
    print("Consumer Three waiting for item management messages. To exit press CTRL+C")
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