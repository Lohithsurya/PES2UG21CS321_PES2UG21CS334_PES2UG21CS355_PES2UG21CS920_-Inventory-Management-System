# from flask import Flask, jsonify, request

# # Create a Flask application
# app = Flask(__name__)

# # Define a route for the root URL
# @app.route('/')
# def index():
#     return 'Welcome to the Inventory Management System!'

# # Health check endpoint
# @app.route('/health')
# def health_check():
#     return jsonify({'status': 'ok'})

# # Sample data for inventory (initially empty)
# inventory = []

# # Helper function to find an item by ID
# def find_item_by_id(item_id):
#     for item in inventory:
#         if item['id'] == item_id:
#             return item
#     return None

# # Route for creating a new item
# @app.route('/inventory', methods=['POST'])
# def create_item():
#     data = request.json
#     if 'name' not in data or 'quantity' not in data:
#         return jsonify({'error': 'Missing name or quantity'}), 400
    
#     item = {
#         'id': len(inventory) + 1,
#         'name': data['name'],
#         'quantity': data['quantity']
#     }
#     inventory.append(item)
#     return jsonify({'message': 'Item added successfully', 'item': item}), 201

# # Route for retrieving all items in inventory
# @app.route('/inventory', methods=['GET'])
# def get_inventory():
#     return jsonify({'inventory': inventory})

# # Route for retrieving a specific item by ID
# @app.route('/inventory/<int:item_id>', methods=['GET'])
# def get_item(item_id):
#     item = find_item_by_id(item_id)
#     if item:
#         return jsonify({'item': item})
#     else:
#         return jsonify({'error': 'Item not found'}), 404

# # Route for updating an existing item by ID
# @app.route('/inventory/<int:item_id>', methods=['PUT', 'PATCH'])
# def update_item(item_id):
#     item = find_item_by_id(item_id)
#     if not item:
#         return jsonify({'error': 'Item not found'}), 404

#     data = request.json
#     if 'name' in data:
#         item['name'] = data['name']
#     if 'quantity' in data:
#         item['quantity'] = data['quantity']
    
#     return jsonify({'message': 'Item updated successfully', 'item': item})

# # Route for deleting an item by ID
# @app.route('/inventory/<int:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     item = find_item_by_id(item_id)
#     if not item:
#         return jsonify({'error': 'Item not found'}), 404
    
#     inventory.remove(item)
#     return jsonify({'message': 'Item deleted successfully'})

# if __name__ == '__main__':
#     # Run the Flask application
#     app.run(debug=True)














# from flask import Flask, jsonify, request, render_template

# # Create a Flask application
# app = Flask(__name__)

# # Sample data for inventory (initially empty)
# inventory = []

# # Helper function to find an item by ID
# def find_item_by_id(item_id):
#     for item in inventory:
#         if item['id'] == item_id:
#             return item
#     return None

# # Define a route for the root URL
# @app.route('/')
# def index():
#     return render_template('index.html', inventory=inventory)

# # Health check endpoint
# @app.route('/health')
# def health_check():
#     return jsonify({'status': 'ok'})

# # Route for creating a new item
# @app.route('/inventory', methods=['POST'])
# def create_item():
#     data = request.form
#     if 'name' not in data or 'quantity' not in data:
#         return jsonify({'error': 'Missing name or quantity'}), 400
    
#     item = {
#         'id': len(inventory) + 1,
#         'name': data['name'],
#         'quantity': int(data['quantity'])  # Ensure quantity is converted to integer
#     }
#     inventory.append(item)
#     return render_template('index.html', inventory=inventory)

# # Route for updating an existing item by ID
# @app.route('/inventory/<int:item_id>', methods=['POST'])
# def update_item(item_id):
#     item = find_item_by_id(item_id)
#     if not item:
#         return jsonify({'error': 'Item not found'}), 404

#     data = request.form
#     if 'name' in data:
#         item['name'] = data['name']
#     if 'quantity' in data:
#         item['quantity'] = int(data['quantity'])  # Ensure quantity is converted to integer
    
#     return render_template('index.html', inventory=inventory)

# # Route for deleting an item by ID
# @app.route('/inventory/<int:item_id>', methods=['POST'])
# def delete_item(item_id):
#     item = find_item_by_id(item_id)
#     if not item:
#         return jsonify({'error': 'Item not found'}), 404
    
#     inventory.remove(item)
#     return render_template('index.html', inventory=inventory)

# if __name__ == '__main__':
#     # Run the Flask application
#     app.run(debug=True)










# from flask import Flask, jsonify, request, render_template
# import mysql.connector

# # Create a Flask application
# app = Flask(__name__)

# # Configure MySQL connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="rhtx@sql",
#     database="inventory_management"
# )
# cursor = db.cursor(dictionary=True)

# # Define routes

# # Health check endpoint
# @app.route('/health')
# def health_check():
#     return jsonify({'status': 'ok'})

# # Route for rendering the index page with inventory data
# @app.route('/')
# def index():
#     sql = "SELECT * FROM inventory"
#     cursor.execute(sql)
#     inventory = cursor.fetchall()
#     return render_template('index.html', inventory=inventory)

# # Route for creating a new inventory item
# @app.route('/inventory', methods=['POST'])
# def create_inventory_item():
#     data = request.form
#     if 'name' not in data or 'quantity' not in data:
#         return jsonify({'error': 'Missing name, quantity'}), 400
    
#     sql = "INSERT INTO inventory (name, quantity) VALUES (%s, %s)"
#     values = (data['name'], data['quantity'])
#     cursor.execute(sql, values)
#     db.commit()
    
#     return jsonify({'message': 'Inventory item created successfully'})

# # Route for updating an existing inventory item by ID
# @app.route('/inventory/<int:item_id>', methods=['PUT'])
# def update_inventory_item(item_id):
#     data = request.form
#     sql = "SELECT * FROM inventory WHERE id = %s"
#     cursor.execute(sql, (item_id,))
#     item = cursor.fetchone()
#     if not item:
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
    
#     return jsonify({'message': 'Inventory item updated successfully'})

# # Route for deleting an inventory item by ID
# @app.route('/inventory/<int:item_id>', methods=['DELETE'])
# def delete_inventory_item(item_id):
#     sql = "DELETE FROM inventory WHERE id = %s"
#     cursor.execute(sql, (item_id,))
#     db.commit()
#     return jsonify({'message': 'Inventory item deleted successfully'})

# # # Route for creating a new order
# # @app.route('/order', methods=['POST'])
# # def create_order():
# #     data = request.form
# #     if 'customer_name' not in data or 'total_amount' not in data:
# #         return jsonify({'error': 'Missing customer_name or total_amount'}), 400
    
# #     sql = "INSERT INTO orders (customer_name, total_amount, status) VALUES (%s, %s, %s)"
# #     values = (data['customer_name'], data['total_amount'], 'Pending')
# #     cursor.execute(sql, values)
# #     db.commit()
    
# #     return jsonify({'message': 'Order created successfully'})

# # # Route for updating an existing order by ID
# # @app.route('/order/<int:order_id>', methods=['PUT'])
# # def update_order(order_id):
# #     data = request.form
# #     sql = "SELECT * FROM orders WHERE id = %s"
# #     cursor.execute(sql, (order_id,))
# #     order = cursor.fetchone()
# #     if not order:
# #         return jsonify({'error': 'Order not found'}), 404

# #     if 'status' in data:
# #         sql = "UPDATE orders SET status = %s WHERE id = %s"
# #         cursor.execute(sql, (data['status'], order_id))
# #         db.commit()
    
# #     return jsonify({'message': 'Order updated successfully'})

# if __name__ == '__main__':
#     app.run(debug=True)






# from flask import Flask, jsonify, request, render_template
# import mysql.connector

# # Create a Flask application
# app = Flask(__name__)

# # Configure MySQL connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="rhtx@sql",
#     database="inventory_management"
# )
# cursor = db.cursor(dictionary=True)

# # Define routes

# # Health check endpoint
# @app.route('/health')
# def health_check():
#     return jsonify({'status': 'ok'})

# # Route for rendering the index page with inventory data
# @app.route('/')
# def index():
#     sql = "SELECT * FROM inventory"
#     cursor.execute(sql)
#     inventory = cursor.fetchall()
#     return render_template('index.html')

#     inventory = fetch_inventory_data()

# # Route for creating a new inventory item
# @app.route('/', methods=['POST'])
# def create_inventory_item():
#     data = request.form
#     if 'name' not in data or 'quantity' not in data:
#         return jsonify({'error': 'Missing name, quantity'}), 400
    
#     sql = "INSERT INTO inventory (name, quantity) VALUES (%s, %s)"
#     values = (data['name'], data['quantity'])
#     cursor.execute(sql, values)
#     db.commit()
    
#     inventory = fetch_inventory_data()
#     # Render success message template
#     return render_template('index.html', message='Inventory item created successfully')

# # Route for updating an existing inventory item by ID
# @app.route('/', methods=['PUT'])
# def update_inventory_item(item_id):
#     data = request.form
#     sql = "SELECT * FROM inventory WHERE id = %s"
#     cursor.execute(sql, (item_id))
#     item = cursor.fetchone()
#     if not item:
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

#         inventory = fetch_inventory_data()
#         # In the create_inventory_item() and update_inventory_item() functions
#         return render_template('index.html', message='Inventory item updated successfully')

# # Route for deleting an inventory item by ID
# @app.route('/<int:item_id>', methods=["DELETE"])
# def delete_inventory_item(item_id):
#     sql = "DELETE FROM inventory WHERE id = %s"
#     cursor.execute(sql, (item_id))
#     db.commit()

#     inventory = fetch_inventory_data()
#     return jsonify({'message': 'Inventory item deleted successfully'})

# if __name__ == '__main__':
#     app.run(debug=True)


 






from flask import Flask, jsonify, request, render_template
import mysql.connector

# Create a Flask application
app = Flask(__name__)

# Function to fetch inventory data from the database
def fetch_inventory_data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rhtx@sql",
        database="inventory_management"
    )
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM inventory"
    cursor.execute(sql)
    inventory = cursor.fetchall()
    cursor.close()
    db.close()
    return inventory

# Define routes

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({'status': 'ok'})

# Route for rendering the index page with inventory data
@app.route('/')
def index():
    inventory = fetch_inventory_data()
    return render_template('index.html', inventory=inventory)

# Route for creating a new inventory item
@app.route('/additem', methods=['POST'])
def create_inventory_item():
    data = request.form
    if 'name' not in data or 'quantity' not in data:
        return jsonify({'error': 'Missing name, quantity'}), 400
    
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rhtx@sql",
        database="inventory_management"
    )
    cursor = db.cursor(dictionary=True)
    
    sql = "INSERT INTO inventory (name, quantity) VALUES (%s, %s)"
    values = (data['name'], data['quantity'])
    cursor.execute(sql, values)
    db.commit()
    
    cursor.close()
    db.close()
    
    # Reload inventory data
    inventory = fetch_inventory_data()
    
    # Render success message template
    return render_template('index.html', inventory=inventory, message='Inventory item created successfully')

# Route for updating an existing inventory item by ID
@app.route('/updateitem', methods=['PUT'])
def update_inventory_item():
    data = request.form
    item_id = request.args.get('id')
    if 'name' not in data or 'quantity' not in data or not item_id:
        return jsonify({'error': 'Missing name, quantity, or item ID'}), 400
    
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rhtx@sql",
        database="inventory_management"
    )
    cursor = db.cursor(dictionary=True)
    
    sql = "SELECT * FROM inventory WHERE id = %s"
    cursor.execute(sql, (item_id,))
    item = cursor.fetchone()
    if not item:
        cursor.close()
        db.close()
        return jsonify({'error': 'Inventory item not found'}), 404

    update_values = []
    if 'name' in data:
        update_values.append(f"name = '{data['name']}'")
    if 'quantity' in data:
        update_values.append(f"quantity = {data['quantity']}")
    
    if update_values:
        sql = f"UPDATE inventory SET {', '.join(update_values)} WHERE id = {item_id}"
        cursor.execute(sql)
        db.commit()
    
    cursor.close()
    db.close()
    
    # Reload inventory data
    inventory = fetch_inventory_data()
    
    # Render success message template
    return render_template('index.html', inventory=inventory, message='Inventory item updated successfully')

# Route for deleting an inventory item by ID
@app.route('/deleteitem/1', methods=["GET"])
def delete_inventory_item(item_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rhtx@sql",
        database="inventory_management"
    )
    cursor = db.cursor(dictionary=True)
    
    sql = "DELETE FROM inventory WHERE id = %s"
    cursor.execute(sql, (item_id,))
    db.commit()
    
    cursor.close()
    db.close()
    
    # Reload inventory data
    inventory = fetch_inventory_data()
    
    return jsonify({'message': 'Inventory item deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
