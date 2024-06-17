SELECT 5565+33656;
select 797097-5638653;
select 34535*1674;
select 40/5;
select 40%5;

select 10=10;
select 10>345;
select 348<769769;
select 354>=87098;
select 798679<=797;
select 10<>6708;

select 59&47;
select 59|5643;
select 59^ 97;

select 4=4 and 5<10;
select not 5=5;
select "hello" like 4;
select 5 between 1 and 10;

create database hi;
use  hi;
create table product
( product_id INT,
 price INT);
 
 insert into product values
(1,100),(2,250),(3,267),(4,150),(5,230);
 select* from product
 
 //questions
 
 select sum(price) as total from product;
 select avg(price) as average from product;
 select * from product
 where price %3=0;
 select * from product
 where price <=10000;
 
 
alter table product
add column place varchar(50),
add column stocklevel  int;
 
 
 insert into product(product_id,place,stocklevel) 
 values (1,"mumbai",9),(2,'Delhi', 11),(3,'Bangalore', 7),(4,'Chennai', 5),(5,'Chennai', 5);
alter table product
drop column place,
drop column stocklevel;
 select * from product;
 
ALTER TABLE product
ADD COLUMN place VARCHAR(50),
ADD COLUMN stocklevel INT;
SET SQL_SAFE_UPDATES = 0;
delete from product
where product_id is null;

UPDATE product
SET 
    place = CASE 
               WHEN product_id = 1 THEN 'Mumbai'
               WHEN product_id = 2 THEN 'kochi'
               WHEN product_id = 3 THEN 'Delhi'
               WHEN product_id = 4 THEN 'Bangalore'
               WHEN product_id = 5 THEN 'Mumbai'
               ELSE place  -- keep current value if product_id is not in the list
           END,
    stocklevel = CASE 
                    WHEN product_id = 1 THEN 10
                    WHEN product_id = 2 THEN 20
                    WHEN product_id = 3 THEN 30
                    WHEN product_id = 4 THEN 40
                    WHEN product_id = 5 THEN 50
                    ELSE stocklevel  -- keep current value if product_id is not in the list
                 END
WHERE product_id IN (1, 2, 3, 4, 5);


select * from product where 
place="mumbai" & stocklevel <30;

select * from product where 
place="mumbai" | price <200;

