import pika
import json

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='inventory_queue')

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

    channel.basic_consume(queue='inventory_queue', on_message_callback=callback, auto_ack=True)

    print("Consumer Two waiting for item creation messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    main()
