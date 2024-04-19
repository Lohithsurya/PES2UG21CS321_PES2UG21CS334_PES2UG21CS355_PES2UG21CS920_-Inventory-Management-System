# import pika

# # Establish connection to RabbitMQ server
# connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
# channel = connection.channel()

# # Declare a queue
# channel.queue_declare(queue='inventory_queue')

# # Publish a message to the queue
# channel.basic_publish(exchange='', routing_key='inventory_queue', body='Message from producer')

# # Close connection
# connection.close()

import pika

class ProducerService:
    def __init__(self, host='rabbitmq', port=5672):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
        self.channel = self.connection.channel()

    def create_queue(self, ):
        self.channel.queue_declare(queue='inventory_queue')

    def create_exchange(self, exchange_name, exchange_type='direct'):
        self.channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

    def publish_message(self, exchange_name, routing_key, message):
        self.channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)
        print(f"Sent message '{message}' to exchange '{exchange_name}' with routing key '{routing_key}'")

    def close_connection(self):
        self.connection.close()

# Example usage
if __name__ == "__main__":
    producer = ProducerService()
    producer.create_exchange('inventory_exchange', 'direct')
    producer.create_queue('inventory_queue')
    producer.channel.queue_bind(exchange='', queue='inventory_queue', routing_key='inventory_queue')

    # Publish message to the exchange
    producer.publish_message('', 'inventory_queue', 'Message from producer')

    producer.close_connection()
