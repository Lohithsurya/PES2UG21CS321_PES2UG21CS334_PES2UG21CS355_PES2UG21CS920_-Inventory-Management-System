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

from flask import Flask, jsonify, request, render_template

# Create a Flask application
app = Flask(__name__)

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
    return render_template('index.html', inventory=inventory)

# Route for updating an existing item by ID
@app.route('/inventory/<int:item_id>', methods=['UPDATE'])
def update_item(item_id):
    item = find_item_by_id(item_id)
    if not item:
        cursor.close()
        db.close()
        return jsonify({'error': 'Inventory item not found'}), 404

    data = request.form
    if 'name' in data:
        update_values.append(f"name = '{data['name']}'")
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
    return render_template('index.html', inventory=inventory)

if __name__ == '__main__':
    app.run(debug=True)
