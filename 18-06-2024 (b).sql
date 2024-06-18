SELECT DISTINCT locations FROM products;

SELECT customer_id, customer_name, LENGTH(address) AS address_length FROM customer;

SELECT o.order_id, c.customer_name, p.product_name, 
CONCAT('Order for ', p.product_name, ' by ', c.customer_name) AS order_description
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;

SELECT product_id, product_name, price, CASE WHEN price < 10000 THEN 'Low' 
WHEN price BETWEEN 10000 AND 50000 THEN 'Medium' ELSE 'High' END AS price_category
FROM products;

SELECT c.customer_id, c.customer_name, (SELECT SUM(o.order_amount) 
FROM orders o WHERE o.customer_id = c.customer_id) AS total_order_amount
FROM customer c;
