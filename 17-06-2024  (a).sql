CREATE  database mydb;
use mydb;
drop database mydb;
create database mydb;
alter database mydb READ only=0;
use mydb;

create table employees(
employee_id INT,
first_name VARCHAR(50),
last_name VARCHAR(50),
hourly_pay DECIMAL(5,2),
hire_date DATE
);

SELECT * FROM employees;
RENAME TABLE employees to workers;
rename table workers to employees;

alter table employees
add phone_number VARCHAR(50);
select *from employees;

alter table employees 
rename column phone_number to email;

alter table employees
modify column email  varchar(100);

select * from employees;

alter table employees
modify email varchar(100)
after last_name;
use mydb;
select * from employees;

insert into employees
values(1,"eugene","lyngdoh","hstgh#gmail.com",0.2,"2023-01-02"),
(2, "alice", "smith", "alice.smith@email.com", 0.5, "2023-03-15"),
(3, "john", "doe", "johndoe@email.com", 0.7, "2022-12-10"),
(4, "sarah", "jones", "sarahjones@email.com", 0.3, "2024-05-20"),
(5, "michael", "brown", "mbrown@email.com", 0.9, "2023-08-27")
;

insert into employees(employee_id,first_name,last_name)
values(6,"gym","bro");


select first_name,last_name,email
from employees;

select * 
from employees
where employee_id =1;

select *from
employees
where hourly_pay >0.5;

select *
from employees
where hire_date is null;


update employees
set hourly_pay=1.2

where employee_id=6;

SET SQL_SAFE_UPDATES = 0;

update employees
set email ="gufukvui@gmail.com",
hire_date="2023-01-12"
where employee_id=6;

delete from employees
where employee_id =1;

insert into employees
values(1,"eugene","lyndoh","hjvuvbiv@hotmail.com",0.6,"2022-03-18");



set autocommit=off;
commit;
select * from employees;
insert into employees
values(1,"eugene","lyngdoh","hstgh#gmail.com",0.2,"2023-01-02"),
(2, "alice", "smith", "alice.smith@email.com", 0.5, "2023-03-15"),
(3, "john", "doe", "johndoe@email.com", 0.7, "2022-12-10"),
(4, "sarah", "jones", "sarahjones@email.com", 0.3, "2024-05-20"),
(5, "michael", "brown", "mbrown@email.com", 0.9, "2023-08-27");



delete from employees;
rollback;


create table test(
	my_date date,
    my_time time,
    my_datetime datetime
    );
    
    
select *from test;

insert into test
values(current_date(), current_time(),now());
select *from test;

drop table test; 

create table products(
	product_id int,
    product_name VARCHAR(25),
    price decimal(4,2)
);

alter table products
add constraint
unique(product_name);