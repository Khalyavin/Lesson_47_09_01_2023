CREATE TABLE employees
(
	employee_id serial PRIMARY KEY,
	first_name varchar(15),
	last_name varchar(15) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date char(10) NOT NULL,
	notes text
);

CREATE TABLE customers
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE orders
(
	order_id int,
	customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id int, 
	order_date char(10),
	ship_city varchar(25),
	FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
)