from flask import Flask, jsonify, request, render_template
import pika
import json

app = Flask(__name__)

# RabbitMQ connection parameters
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT,
                                                               credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)))
channel = connection.channel()

# Declare queues
channel.queue_declare(queue='health_check_queue')
channel.queue_declare(queue='item_creation_queue')
channel.queue_declare(queue='stock_management_queue')
channel.queue_declare(queue='order_processing_queue')

# Sample data for inventory (initially empty)
inventory = []

# Helper function to find an item by ID
def find_item_by_id(item_id):
    for item in inventory:
        if item['id'] == item_id:
            return item
    return None

# Define a route for the root URL
@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

# Health check endpoint
@app.route('/health')
def health_check():
    # Send health check message to RabbitMQ
    channel.basic_publish(exchange='', routing_key='health_check_queue', body=json.dumps({'message': 'Health Check'}))
    return jsonify({'status': 'ok'})

# Route for creating a new item
@app.route('/inventory', methods=['POST'])
def create_item():
    data = request.form
    if 'name' not in data or 'quantity' not in data:
        return jsonify({'error': 'Missing name or quantity'}), 400
    
    item = {
        'id': len(inventory) + 1,
        'name': data['name'],
        'quantity': int(data['quantity'])  # Ensure quantity is converted to integer
    }
    inventory.append(item)

    # Send item creation message to RabbitMQ
    channel.basic_publish(exchange='', routing_key='item_creation_queue', body=json.dumps(item))

    return render_template('index.html', inventory=inventory)

# Route for updating an existing item by ID
@app.route('/inventory/<int:item_id>', methods=['UPDATE'])
def update_item(item_id):
    item = find_item_by_id(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    data = request.form
    if 'name' in data:
        item['name'] = data['name']
    if 'quantity' in data:
        item['quantity'] = int(data['quantity'])  # Ensure quantity is converted to integer
    
    return render_template('index.html', inventory=inventory)

# Route for deleting an item by ID
@app.route('/inventory', methods=['DELETE'])
def delete_item(item_id):
    item = find_item_by_id(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    inventory.remove(item)

    # Send item deletion message to RabbitMQ
    channel.basic_publish(exchange='', routing_key='item_deletion_queue', body=json.dumps({'item_id': item_id}))

    return render_template('index.html', inventory=inventory)

# Consumer for health checks
def health_check_consumer():
    def callback(ch, method, properties, body):
        print("Received health check message:", json.loads(body))
        # Implement health check functionality

    channel.basic_consume(queue='health_check_queue', on_message_callback=callback, auto_ack=True)
    print("Consumer for health checks waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

# Consumer for item creation
def item_creation_consumer():
    def callback(ch, method, properties, body):
        print("Received item creation message:", json.loads(body))
        # Implement item creation functionality

    channel.basic_consume(queue='item_creation_queue', on_message_callback=callback, auto_ack=True)
    print("Consumer for item creation waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

# Consumer for stock management
def stock_management_consumer():
    def callback(ch, method, properties, body):
        print("Received stock management message:", json.loads(body))
        # Implement stock management functionality

    channel.basic_consume(queue='stock_management_queue', on_message_callback=callback, auto_ack=True)
    print("Consumer for stock management waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

# Consumer for order processing
def order_processing_consumer():
    def callback(ch, method, properties, body):
        print("Received order processing message:", json.loads(body))
        # Implement order processing functionality

    channel.basic_consume(queue='order_processing_queue', on_message_callback=callback, auto_ack=True)
    print("Consumer for order processing waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0')

    # Start consumers
    health_check_consumer()
    item_creation_consumer()
    stock_management_consumer()
    order_processing_consumer()