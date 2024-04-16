import pika
import json

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='inventory_queue')

    def callback(ch, method, properties, body):
        print("Consumer Three received stock management message:", body.decode())
        # Implement stock management functionality here
        # For example, parse the message to determine stock update actions and update database accordingly
        try:
            # Assuming the message format is JSON
            stock_update_data = json.loads(body.decode())
            # Placeholder: Update stock in database
            print("Stock management operation performed successfully:", stock_update_data)
        except Exception as e:
            print("Error processing stock management message:", e)

    channel.basic_consume(queue='inventory_queue', on_message_callback=callback, auto_ack=True)

    print("Consumer Three waiting for stock management messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    main()
