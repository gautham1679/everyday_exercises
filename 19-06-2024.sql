-- Creating database
CREATE DATABASE ecommerce;

-- Using database
USE ecommerce;

-- Creating table Products - pid, pname, price, stock, location (Mumbai or Delhi)
CREATE TABLE products (
    pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(5),
    location VARCHAR(30) CHECK(location IN ('Mumbai','Delhi'))
);

-- Creating table Customer - cid, cname, age, addr
CREATE TABLE customer (
    cid INT(3) PRIMARY KEY,
    cname VARCHAR(30) NOT NULL,
    age INT(3),
    addr VARCHAR(50)
);

-- Creating table Orders - oid, cid, pid, amt
CREATE TABLE orders (
    oid INT(3) PRIMARY KEY,
    cid INT(3),
    pid INT(3),
    amt INT(10) NOT NULL,
    FOREIGN KEY(cid) REFERENCES customer(cid),
    FOREIGN KEY(pid) REFERENCES products(pid)
);

-- Creating table Payment - pay_id, oid, amount, mode(upi, credit, debit), status
CREATE TABLE payment (
    pay_id INT(3) PRIMARY KEY,
    oid INT(3),
    amount INT(10) NOT NULL,
    mode VARCHAR(30) CHECK(mode IN ('upi','credit','debit')),
    status VARCHAR(30),
    FOREIGN KEY(oid) REFERENCES orders(oid)
);

-- Creating table Employee - eid, ename, phone_no, department, manager_id
CREATE TABLE employee (
    eid INT(4) PRIMARY KEY,
    ename VARCHAR(40) NOT NULL,
    phone_no INT(10) NOT NULL,
    department VARCHAR(40) NOT NULL,
    manager_id INT(4)
);

-- Inserting values into products table
INSERT INTO products VALUES (1, 'HP Laptop', 50000, 15, 'Mumbai');
INSERT INTO products VALUES (2, 'Realme Mobile', 20000, 30, 'Delhi');
INSERT INTO products VALUES (3, 'Boat Earpods', 3000, 50, 'Delhi');
INSERT INTO products VALUES (4, 'Lenovo Laptop', 40000, 15, 'Mumbai');
INSERT INTO products VALUES (5, 'Charger', 1000, 0, 'Mumbai');
INSERT INTO products VALUES (6, 'MacBook', 78000, 6, 'Delhi');
INSERT INTO products VALUES (7, 'JBL Speaker', 6000, 2, 'Delhi');

-- Inserting values into customer table
INSERT INTO customer VALUES (101, 'Ravi', 30, 'fdslfjl');
INSERT INTO customer VALUES (102, 'Rahul', 25, 'fdslfjl');
INSERT INTO customer VALUES (103, 'Simran', 32, 'fdslfjl');
INSERT INTO customer VALUES (104, 'Purvesh', 28, 'fdslfjl');
INSERT INTO customer VALUES (105, 'Sanjana', 22, 'fdslfjl');

-- Inserting values into orders table
INSERT INTO orders VALUES (10001, 102, 3, 2700);
INSERT INTO orders VALUES (10002, 104, 2, 18000);
INSERT INTO orders VALUES (10003, 105, 5, 900);
INSERT INTO orders VALUES (10004, 101, 1, 46000);

-- Inserting values into payment table
INSERT INTO payment VALUES (1, 10001, 2700, 'upi', 'completed');
INSERT INTO payment VALUES (2, 10002, 18000, 'credit', 'completed');
INSERT INTO payment VALUES (3, 10003, 900, 'debit', 'in process');

-- Inserting values into employee table
INSERT INTO employee VALUES (401, 'Rohan', 364832549, 'Analysis', 404);
INSERT INTO employee VALUES (402, 'Rahul', 782654123, 'Delivery', 406);
INSERT INTO employee VALUES (403, 'Shyam', 856471235, 'Delivery', 402);
INSERT INTO employee VALUES (404, 'Neha', 724863287, 'Sales', 402);
INSERT INTO employee VALUES (405, 'Sanjana', 125478954, 'HR', 404);
INSERT INTO employee VALUES (406, 'Sanjay', 956478535, 'Tech', NULL);


SELecT * FROM customer;
select *from orders;
select *from products;
select customer.cid,cname,orders.oid from orders
inner join customer on orders.cid = customer.cid;

select customer.cid, cname ,products.pid,pname,orders.oid from orders
inner join products on orders.pid = products.pid
inner join customer on orders.cid= customer.cid;


select customer.cid ,cname ,orders.oid from orders
left join customer on orders.cid=customer.cid;

select customer.cid ,cname ,orders.oid from orders
right join customer on orders.cid=customer.cid;

select orders.oid,products.pid, amt,stock from orders
left join products on orders.pid=products.pid
union
select orders.oid,products.pid, amt,stock from orders
right join products on  orders.pid=products.pid;

select e1.ename as employee, e2.ename as manager from employee e1
inner join employee e2 on e1.manager_id = e2.eid;


select customer.cid, cname, orders.oid, amt from customer
cross join orders on customer.cid = orders.cid
where amt > 3000;

