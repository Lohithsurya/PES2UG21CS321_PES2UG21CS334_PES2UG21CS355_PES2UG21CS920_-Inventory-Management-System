# import pika, sys, os
# import pika
# import json

# def main():
# # Establish connection to RabbitMQ server
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()

# # Declare the same queue as the producer
#     channel.queue_declare(queue='order_management_queue')

# # Define a callback function to process incoming messages
#     def callback(ch, method, properties, body):
#         print("Received message:", body.decode())
#         print("Consumer Four received order processing message:", body.decode())
#         # Implement order processing functionality here
#         # For example, parse the message to extract order details and process the order
#         try:
#             # Assuming the message format is JSON
#             order_data = json.loads(body.decode())
#             # Process the order based on order_data
#             process_order(order_data)
#             print("Order processed successfully:", order_data)
#         except Exception as e:
#                 print("Error processing order:", e)
#         def process_order(order_data):
#             # Placeholder function to simulate order processing
#             # In a real scenario, this function would perform actions such as updating inventory, generating invoices, etc.
#             # Here, we simply print the order data
#             print("Processing order:", order_data)

#         # Example: Update inventory
#         for item in order_data['item_id']:
#             print(f"Updating inventory for item {item['id']}. Quantity: {item['quantity']}")

#         # Example: Generate invoice
#         generate_invoice(order_data)

#     def generate_invoice(order_data):
#         # Placeholder function to simulate invoice generation
#         # In a real scenario, this function would generate an invoice and send it to the customer
#         # Here, we simply print the invoice details
#         print("Generating invoice for order:")
#         print("Order ID:", order_data['id'])
#         print("Customer:", order_data['customer_name'])
#         print("Total amount:", order_data['order_quantity'])


#     channel.basic_consume(queue='order_management_queue', on_message_callback=callback, auto_ack=True)

# # Start consuming (blocking call)
#     #print("Consumer waiting for messages. To exit press CTRL+C")
#     print("Consumer Four waiting for order processing messages. To exit press CTRL+C")
#     channel.start_consuming()

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
#     main()


import pika
import json

def main():
    # Establish connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the same queue as the producer
    channel.queue_declare(queue='order_management_queue')

    # Define a callback function to process incoming messages
    def callback(ch, method, properties, body):
        print("Received message:", body.decode())
        print("Consumer Four received order processing message:", body.decode())
        # Implement order processing functionality here
        # For example, parse the message to extract order details and process the order
        try:
            # Assuming the message format is JSON
            order_data = json.loads(body.decode())
            # Process the order based on order_data
            process_order(order_data)
            print("Order processed successfully:", order_data)
        except Exception as e:
            print("Error processing order:", e)

    def process_order(order_data):
        # Placeholder function to simulate order processing
        # In a real scenario, this function would perform actions such as updating inventory, generating invoices, etc.
        # Here, we simply print the order data
        print("Processing order:", order_data)


    channel.basic_consume(queue='order_management_queue', on_message_callback=callback, auto_ack=True)

    # Start consuming (blocking call)
    print("Consumer Four waiting for order processing messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    main()





