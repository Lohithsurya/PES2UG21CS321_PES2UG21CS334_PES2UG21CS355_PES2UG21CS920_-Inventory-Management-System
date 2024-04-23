# from flask import Flask, jsonify, request, render_template
# import mysql.connector
# import pika
# import json

# app = Flask(__name__)

# # RabbitMQ connection parameters
# RABBITMQ_HOST = 'localhost'
# RABBITMQ_PORT = 5672
# RABBITMQ_USER = 'guest'
# RABBITMQ_PASS = 'guest'

# # Function to publish a message to RabbitMQ
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT,credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)))
# channel = connection.channel()

# # Declare queues
# channel.queue_declare(queue='health_check_queue')
# channel.queue_declare(queue='item_creation_queue')
# channel.queue_declare(queue='stock_management_queue')
# channel.queue_declare(queue='order_processing_queue')



# # Function to fetch inventory data from the database
# def fetch_inventory_data():
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="rhtx@sql",
#         database="inventory_management"
#     )
#     cursor = db.cursor(dictionary=True)
#     sql = "SELECT * FROM inventory"
#     cursor.execute(sql)
#     inventory = cursor.fetchall()
#     cursor.close()
#     db.close()
#     return inventory

# def fetch_order_data():
#     db = mysql.connector.connect(
#         host="localhost",
#         user = "root",
#         password = "rhtx@sql",
#         database = "inventory_management",
#     )
#     cursor = db.cursor(dictionary=True)
#     sql = "SELECT * FROM orders"
#     cursor.execute(sql)
#     orders = cursor.fetchall()
#     cursor.close()
#     db.close()
#     return orders



# @app.route('/health')
# def health_check():
#     channel.basic_publish(exchange='', routing_key='health_check_queue', body=json.dumps({'message': 'Health Check'}))
#     return jsonify({'status': 'ok'})

# # Inventory endpoint
# @app.route('/')
# def index():
#     inventory = fetch_inventory_data()
#     return render_template('index.html',inventory=inventory)


# @app.route('/add-item')
# def add_item():
#     return render_template('additem.html')

# @app.route('/delete-item')
# def delete_item():
#     return render_template('delete.html')

# @app.route('/update-item')
# def update_item():
#     return render_template('updateitem.html')

# @app.route('/orderitem')
# def order_item():
#     orders = fetch_order_data()
#     return render_template('orderitem.html', orders=orders)

# @app.route('/additem', methods=['POST'])
# def create_inventory_item():
#     data = request.form
#     if 'name' not in data or 'quantity' not in data:
#         return jsonify({'error': 'Missing name, quantity'}), 400
    
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="rhtx@sql",
#         database="inventory_management"
#     )
#     cursor = db.cursor(dictionary=True)
    
#     sql = "INSERT INTO inventory (name, quantity) VALUES (%s, %s)"
#     values = (data['name'], data['quantity'])
#     cursor.execute(sql, values)
#     db.commit()
    
#     cursor.close()
#     db.close()
    
#     # Define the content of the message to be published to RabbitMQ
#     item = {'action': 'create', 'name': data['name'], 'quantity': data['quantity']}
    
#     # Publish the message to RabbitMQ
#     send_message('item_creation_queue', item)
    
#     # Reload inventory data
#     inventory = fetch_inventory_data()
    
#     return render_template('additem.html', inventory=inventory, message='Inventory item created successfully')

# # Route for updating an existing inventory item by ID
# @app.route('/updateitem', methods=['POST'])
# def update_inventory_item():
#     data = request.form
#     name = data['name']
#     item_id = data['item_id']
#     quantity = data['quantity']
#     if not name or not item_id or not quantity:
#         return jsonify({'error': 'Missing name, quantity, or item ID'}), 400
    
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="rhtx@sql",
#         database="inventory_management"
#     )
#     cursor = db.cursor(dictionary=True)
    
#     sql = "SELECT * FROM inventory WHERE id = %s"
#     cursor.execute(sql, (item_id,))
#     item = cursor.fetchone()
#     if not item:
#         cursor.close()
#         db.close()
#         return jsonify({'error': 'Inventory item not found'}), 404

#     update_values = []
#     if 'name' in data:
#         update_values.append(f"name = '{data['name']}'")
#     if 'quantity' in data:
#         update_values.append(f"quantity = {data['quantity']}")
    
#     if update_values:
#         sql = f"UPDATE inventory SET {', '.join(update_values)} WHERE id = {item_id}"
#         cursor.execute(sql)
#         db.commit()
    
#     cursor.close()
#     db.close()
    
#     # Reload inventory data
#     inventory = fetch_inventory_data()
    
#     # Define the content of the message to be published to RabbitMQ
#     item = {'action': 'update', 'id': item_id, 'name': name, 'quantity': quantity}
    
#     # Publish the message to RabbitMQ
#     send_message('item_management_queue', item)
    
#     # Render success message template
#     return render_template('updateitem.html', inventory=inventory, message='Inventory item updated successfully')

# # Route for deleting an inventory item by ID
# @app.route('/deleteitem', methods=["GET"])
# def delete_inventory_item():
#     item_id = request.args.get("item_id")
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Virgo_129",
#         database="inventory_management"
#     )
#     cursor = db.cursor(dictionary=True)
    
#     sql = "DELETE FROM inventory WHERE id = %s"
#     cursor.execute(sql, (item_id,))
#     db.commit()
    
#     cursor.close()
#     db.close()
    
#     # Reload inventory data
#     inventory = fetch_inventory_data()

#     # Define the content of the message to be published to RabbitMQ
#     item = {'action': 'delete', 'id': item_id}
    
#     # Publish the message to RabbitMQ
#     send_message('item_management_queue', item)
    
#     return render_template('delete.html', inventory=inventory, message='Inventory item deleted successfully')


    
# # Route for processing an order
# @app.route('/orderitem', methods=['POST'])
# def order_inventory_item():
#     try:
#         data = request.form
#         name = data.get('customer_name')
#         item_id = data.get('item_id')
#         quantity = data.get('quantity')

#         if not name or not item_id or not quantity:
#             return jsonify({'error': 'Incorrect name, quantity, or item ID'}), 400
        
#         db = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Virgo_129",
#             database="inventory_management"
#         )

#         cursor = db.cursor(dictionary=True)
        
#         sql1 = "SELECT * FROM inventory WHERE id = %s"
#         cursor.execute(sql1, (item_id,))
#         item = cursor.fetchone()
#         if not item:
#             return jsonify({'error': 'Inventory item not found'}), 404
        
#         sql = "INSERT INTO orders (item_id, customer_name, order_quantity) VALUES (%s, %s, %s)"
        
#         values = (item_id, name, quantity)
#         cursor.execute(sql, values)
#         db.commit()
        
#         # Define the content of the message to be published to RabbitMQ
#         order = {'action': 'create', 'item_id': item_id, 'customer_name': name, 'order_quantity': quantity}
        
#         # Publish the message to RabbitMQ
#         send_message('order_management_queue', order)
        
#         orders = fetch_inventory_data()
        
#         return render_template('orderitem.html', orders=orders,  message='Inventory item ordered successfully')

#     except mysql.connector.Error as e:
#         return jsonify({'error': f'Database error: {str(e)}'}), 500
    
#     finally:
#         cursor.close()
#         db.close()

    
# if __name__ == '__main__':
#     app.run(debug=True,host = '0.0.0.0')
