-- CREATE TABLE customer (
-- 	id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(20) NOT NULL,
-- 	last_name VARCHAR(20) NOT NULL
-- );

-- CREATE TABLE customer_profile (
-- 	id SERIAL PRIMARY KEY,
-- 	isLoggedIn BOOLEAN DEFAULT false,
-- 	customer_id INTEGER UNIQUE REFERENCES customer(id)
-- )

-- INSERT INTO customer (first_name, last_name)
-- VALUES
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive')

-- INSERT INTO customer_profile(isLoggedIn, customer_id)
-- VALUES 
-- (true, (SELECT id FROM customer WHERE first_name = 'John')),
-- (false, (SELECT id FROM customer WHERE first_name = 'Jerome'))

-- SELECT first_name FROM customer
-- INNER JOIN customer_profile ON customer.id = customer_id
-- WHERE isloggedin = true

-- SELECT first_name, isloggedin FROM customer
-- LEFT JOIN customer_profile ON customer.id = customer_id

-- SELECT COUNT(*) FROM customer
-- INNER JOIN customer_profile ON customer.id = customer_id
-- WHERE isloggedin = false




