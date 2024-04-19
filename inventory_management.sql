-- Create database
CREATE DATABASE IF NOT EXISTS inventory_management;

USE inventory_management;
-- Create table for inventory items
CREATE TABLE IF NOT EXISTS inventory (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    -- description TEXT,
    quantity INTEGER NOT NULL,
    -- price NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for orders
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    item_id INTEGER REFERENCES inventory(id),
    customer_name VARCHAR(255) NOT NULL,
    order_quantity NUMERIC(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

