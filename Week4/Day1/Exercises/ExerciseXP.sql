-- Database: public

-- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;
	
-- Exercise 1 : Items And Customers

-- Create a database called public.
-- Add two tables:
-- items
-- customers.

-- Follow the instructions below to determine which columns and data types to add to the two tables:

-- Add the following items to the items table:
-- 1 - Small Desk – 100 (ie. price)
-- 2 - Large desk – 300
-- 3 - Fan – 80

-- Add 5 new customers to the customers table:
-- 1 - Greg - Jones
-- 2 - Sandra - Jones
-- 3 - Scott - Scott
-- 4 - Trevor - Green
-- 5 - Melanie - Johnson

-- Use SQL to fetch the following data from the database:
-- All the items.
-- All the items with a price above 80 (80 not included).
-- All the items with a price below 300. (300 included)
-- All customers whose last name is ‘Smith’ (What will be your outcome?).
-- All customers whose last name is ‘Jones’.
-- All customers whose firstname is not ‘Scott’.

-- CREATE TABLE items (
-- 	item_id SERIAL PRIMARY KEY,
-- 	items VARCHAR(100) NOT NULL,
-- 	price INT NOT NULL
-- );

-- CREATE TABLE customers (
-- 	customer_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(100) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL
-- )

-- INSERT INTO items (items, price)
-- VALUES
-- ('Small Desk', 100),
-- ('Large Desk', 300),
-- ('Fan', 80)

-- INSERT INTO customers (first_name, last_name)
-- VALUES
-- ('Greg', 'Jones' ),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson')

-- SELECT * FROM items
-- SELECT * FROM customers

-- SELECT * FROM items
-- WHERE price > 80

-- SELECT * FROM items
-- WHERE price <= 300

-- SELECT * FROM customers
-- WHERE last_name = 'Smith'

-- SELECT * FROM customers
-- WHERE last_name = 'Jones'

-- SELECT * FROM customers
-- WHERE first_name != 'Scott'