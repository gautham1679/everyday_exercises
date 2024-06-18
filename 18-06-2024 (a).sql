create database study;
use  study;

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    location_id INT,
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

CREATE TABLE locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL
);


CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    order_amount DECIMAL(10, 2) NOT NULL,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


INSERT INTO locations (location_name) VALUES
('New York'),
('Los Angeles'),
('Chicago'),
('Mumbai');

INSERT INTO products (product_name, price, stock, location_id) VALUES
('Laptop', 1500.00, 15, 1),  -- New York
('Smartphone', 800.00, 25, 2),  -- Los Angeles
('Tablet', 500.00, 30, 3),  -- Chicago
('Headphones', 100.00, 10, 4);  -- Mumbai


INSERT INTO orders (customer_name, order_amount, product_id) VALUES
('John Doe', 2000.00, 1),  -- Laptop
('Jane Smith', 1600.00, 2),  -- Smartphone
('Michael Johnson', 150.00, 4),  -- Headphones
('Emily Brown', 300.00, 3),  -- Tablet
('Robert Davis', 5000.00, 1),  -- Laptop
('Emma Wilson', 100.00, 4);  -- Headphones


SELECT l.location_name, SUM(p.stock) AS total_stock
FROM locations l
JOIN products p ON l.location_id = p.location_id
GROUP BY l.location_name;


SELECT 
    CASE 
        WHEN price BETWEEN 0 AND 10000 THEN '0-10000'
        WHEN price BETWEEN 10000 AND 20000 THEN '10000-20000'
        WHEN price BETWEEN 20000 AND 50000 THEN '20000-50000'
        ELSE '50000+'
    END AS price_range,
    COUNT(*) AS number_of_products
FROM products
GROUP BY price_range;


SELECT c.location_id, AVG(c.age) AS avg_age
FROM customers c
GROUP BY c.location_id;



SELECT * 
FROM products
ORDER BY price DESC;


SELECT * 
FROM customers
ORDER BY age ASC;


SELECT o.*, p.product_name
FROM orders o
JOIN products p ON o.product_id = p.product_id
ORDER BY o.order_amount DESC, o.customer_name ASC;


SELECT l.location_name, SUM(p.stock) AS total_stock
FROM locations l
JOIN products p ON l.location_id = p.location_id
GROUP BY l.location_name
HAVING total_stock > 20;


SELECT o.customer_name, SUM(o.order_amount) AS total_amount
FROM orders o
GROUP BY o.customer_name
HAVING total_amount > 10000;


SELECT p.product_name, p.stock, l.location_name
FROM products p
JOIN locations l ON p.location_id = l.location_id
WHERE p.stock BETWEEN 10 AND 20 AND l.location_name = 'Mumbai';
