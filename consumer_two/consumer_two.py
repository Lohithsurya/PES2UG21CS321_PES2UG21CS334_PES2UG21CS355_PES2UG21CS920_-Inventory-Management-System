import pika, sys, os
import pika
import json

def main():
# Establish connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

# Declare the same queue as the producer
    channel.queue_declare(queue='item_creation_queue')

# Define a callback function to process incoming messages
    def callback(ch, method, properties, body):
        print("Received message:", body.decode())
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
        
    channel.basic_consume(queue='item_creation_queue', on_message_callback=callback, auto_ack=True)

    # Start consuming (blocking call)
    #print("Consumer waiting for messages. To exit press CTRL+C")
    print("Consumer Two waiting for item creation messages. To exit press CTRL+C")
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



#                              Do not modify the code above this line. 
# --------------------------------------------------------------------------------------------------------------
#                                 Modify the code below this line


