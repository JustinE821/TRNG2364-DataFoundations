



CREATE TABLE salesman (
	salesman_id INT PRIMARY KEY,
	salesman_name VARCHAR(60) NOT NULL,
	city VARCHAR(30) NOT NULL,
	comission DECIMAL(3,2)
)

CREATE TABLE customer (
	customer_id INT PRIMARY KEY,
	cust_name VARCHAR(60) NOT NULL,
	city VARCHAR(30) NOT NULL,
	grade INT,
	salesman_id INT REFERENCES salesman (salesman_id)
)

CREATE TABLE orders (
	order_no INT PRIMARY KEY,
	purchase_amt DECIMAL(10,2) DEFAULT 0,
	order_date DATE DEFAULT now(),
	cust_id INT REFERENCES customer (customer_id),
	salesman_id INT REFERENCES salesman (salesman_id)
);


INSERT INTO salesman (salesman_id, salesman_name, city, commission)
VALUES (5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5007, 'Paul Adam', 'Rome', 0.13),
(5003, 'Randy Joe', 'Berlin', 0.12);


INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id)
VALUES ( 3002, 'Nick Fury', 'New York', 100, 5001),
( 3007, 'Brad Davis', 'New York', 200, 5001),
( 3005, 'Graham Zusi', 'Sacramento', 200, 5002),
( 3008, 'Julian Green', 'Paris', 300, 5007);

INSERT INTO orders (order_no, purchase_amt, order_date, cust_id, salesman_id)
VALUES (70001, 150.5, '2013-10-05', 3005, 5002),
(70009, 270.65, '2013-06-16', 3002, 5005),
(70014, 65.26, '2013-06-22', 3008, 5001),
(70019, 110.5, '2013-07-01', 3007, 5003),
(70020, 948.81, '2013-07-09', 3008, 5007);


SELECT 
	c.customer_id,
	c.cust_name,
	c.city,
	c.grade,
	s.salesman_id,
	s.salesman_name,
	s.city,
	s.commission,
	o.order_no,
	o.purchase_amt,
	o.order_date
FROM customer c
INNER JOIN orders o ON c.customer_id = o.cust_id
INNER JOIN salesman s ON o.salesman_id = s.salesman_id;


ALTER TABLE salesman RENAME COLUMN comission TO commission;
