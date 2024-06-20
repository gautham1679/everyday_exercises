-- Create database
create database amazon;
use amazon;

-- Products - pid, pname, price, stock, location (Mumbai or Delhi)
create table products
(
	pid int(3) primary key,
    pname varchar(50) not null,
    price int(10) not null,
    stock int(5),
    location varchar(30) check(location in ('Mumbai','Delhi'))
);

-- Customer - cid, cname, age, addr
create table customer
(
	cid int(3) primary key,
    cname varchar(30) not null,
    age int(3),
    addr varchar(50)
);

-- Orders - oid, cid, pid, amt
create table orders
(
	oid int(3) primary key,
    cid int(3),
    pid int(3),
    amt int(10) not null,
    foreign key(cid) references customer(cid),
    foreign key(pid) references products(pid)
);


-- Payment - pay_id, oid,amount, mode(upi, cerdit, debit), status
create table payment
(
	pay_id int(3) primary key,
    oid int(3),
    amount int(10) not null,
    mode varchar(30) check(mode in('upi','credit','debit')),
    status varchar(30),
    foreign key(oid) references orders(oid)
);
ALTER TABLE payment
ADD COLUMN timestamp TIMESTAMP;

#Inserting values into products table
insert into products values(1,'HP Laptop',50000,15,'Mumbai');
insert into products values(2,'Realme Mobile',20000,30,'Delhi');
insert into products values(3,'Boat earpods',3000,50,'Delhi');
insert into products values(4,'Levono Laptop',40000,15,'Mumbai');
insert into products values(5,'Charger',1000,0,'Mumbai');
insert into products values(6, 'Mac Book', 78000, 6, 'Delhi');
insert into products values(7, 'JBL speaker', 6000, 2, 'Delhi');
insert into products values(8 , 'Asus Laptop',50000,15,'Delhi');

#Inserting values into customer table
insert into customer values(101,'Ravi',30,'fdslfjl');
insert into customer values(102,'Rahul',25,'fdslfjl');
insert into customer values(103,'Simran',32,'fdslfjl');
insert into customer values(104,'Purvesh',28,'fdslfjl');
insert into customer values(105,'Sanjana',22,'fdslfjl');

#Inserting values into orders table
insert into orders values(10001,102,3,2700);
insert into orders values(10002,104,2,18000);
insert into orders values(10003,105,5,900);
insert into orders values(10004,101,1,46000);


#inserting values into payments table
insert into payment values(1,10001,2700,'upi','completed','2024-05-01 08:00:00');
insert into payment values(2,10002,18000,'credit','completed','2024-05-01 08:10:00');
insert into payment values(3,10003,900,'debit','in process','2024-05-01 08:15:00');


SELECT c.cname
FROM customer c
JOIN (
    SELECT cid, SUM(amt) AS total_amount
    FROM orders
    GROUP BY cid
    ORDER BY total_amount DESC
    LIMIT 1
) AS highest_order ON c.cid = highest_order.cid;




SELECT DISTINCT c.cname
FROM customer c
JOIN orders o ON c.cid = o.cid
JOIN products p ON o.pid = p.pid
WHERE p.location = (
    SELECT location
    FROM customer
    WHERE cname = 'Rahul'
);



SELECT DISTINCT c.cname
FROM customer c
JOIN orders o ON c.cid = o.cid
JOIN products p ON o.pid = p.pid
WHERE p.price > (
    SELECT AVG(p2.price)
    FROM orders o2
    JOIN products p2 ON o2.pid = p2.pid
    WHERE o2.cid = c.cid
);



SELECT c.cname, SUM(o.amt) AS total_amount_spent
FROM customer c
JOIN orders o ON c.cid = o.cid
JOIN products p ON o.pid = p.pid
JOIN (
    SELECT location, AVG(price) AS avg_price
    FROM products
    GROUP BY location
) AS avg_prices ON p.location = avg_prices.location
WHERE p.price > avg_prices.avg_price
GROUP BY c.cname;



SELECT c.cname, COALESCE(SUM(o.amt), 0) AS total_amount_spent
FROM customer c
LEFT JOIN orders o ON c.cid = o.cid
GROUP BY c.cname;



SELECT c.cid,
       c.cname,
       c.age,
       c.addr,
       COALESCE(o.oid, 'No order') AS order_id,
       COALESCE(p.status, 'Out of stock') AS order_status
FROM customer c
LEFT JOIN orders o ON c.cid = o.cid
LEFT JOIN payment p ON o.oid = p.oid
ORDER BY c.cid;




SELECT pname, price, RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;


SELECT pname, price, DENSE_RANK() OVER (ORDER BY price DESC) AS dense_price_rank
FROM products;



SELECT pname, price, ROW_NUMBER() OVER (ORDER BY price DESC) AS row_num
FROM products;


SELECT pname, price, CUME_DIST() OVER (ORDER BY price) AS cumulative_distribution
FROM products;

SELECT pname, price, LAG(price) OVER (ORDER BY price) AS previous_price
FROM products;


SELECT pname, price, LEAD(price) OVER (ORDER BY price) AS next_price
FROM products;