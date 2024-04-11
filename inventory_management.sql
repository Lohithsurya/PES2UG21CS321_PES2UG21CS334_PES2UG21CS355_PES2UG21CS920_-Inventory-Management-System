-- Create database
CREATE DATABASE inventory_management;

USE inventory_management;
-- Create table for inventory items
CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    -- description TEXT,
    quantity INTEGER NOT NULL,
    -- price NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for orders
/*CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    total_amount NUMERIC(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);*/

-- Create table for order items
/*CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    inventory_id INTEGER REFERENCES inventory(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);*/
