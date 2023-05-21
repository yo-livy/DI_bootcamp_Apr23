-- CREATE TABLE actor (
-- 	actor_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(100) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL,
-- 	date_birth DATE NOT NULL,
-- 	number_oscars SMALLINT NOT NULL DEFAULT 0
-- )

-- SELECT * FROM actor

-- SELECT first_name, last_name FROM actor

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES ('George', 'Clooney', '1976-03-12', 2)

-- SELECT * FROM actor


-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES 
-- ('Brad', 'Pitt', '1974-02-10', 3),
-- ('Matt', 'Damon', '1972-07-08', 1)

-- SELECT first_name, last_name FROM actor

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES ('Julia', 'Roberts', '1975-04-16', 2);

-- SELECT * FROM actor

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES
-- ('Kathrin Zeta', 'Johnes', '1976-03-01', DEFAULT),
-- ('Monica', 'Belucci', '1976-11-11', 2);

-- SELECT * FROM actor

-- SELECT first_name, last_name FROM actor WHERE first_name = 'Monica' AND last_name = 'Clooney'

-- SELECT * FROM actor ORDER BY date_birth ASC LIMIT 1

-- SELECT * FROM actor WHERE EXTRACT(YEAR from date_birth) >= 1975

-- SELECT * FROM actor WHERE first_name ILIKE '%g%'

-- UPDATE actor
-- SET last_name = 'Clooneys'
-- WHERE actor_id = 1
-- RETURNING *

-- DELETE FROM actor
-- WHERE actor_id = 5

-- SELECT * FROM actor

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES ('Emma', 'Stone', '1985-01-01', DEFAULT)
-- ALTER TABLE actor ADD COLUMN nationality2 VARCHAR(100)

-- SELECT * FROM actor

-- UPDATE actor
-- SET salary = 1000000 * number_oscars
-- RETURNING *

-- UPDATE actor
-- SET nationality2 = 'American'
-- WHERE actor_id IN (1, 2, 3)
-- RETURNING *

-- Exercise

-- Use the table actors to retrieve :

-- The first 4 actors
-- The first 4 actors ordered in descending order of the last_name (ie. sorted DESCENDING by the "last_name" column))
-- The actors that have the letter 'e' in their first_name
-- The actors that got at least 5 oscars


-- SELECT * FROM actor LIMIT 4
-- SELECT * FROM actor ORDER BY last_name DESC LIMIT 4
-- SELECT * FROM actor WHERE first_name ILIKE '%e%' 
-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES ('Johnny', 'Depp', '1975-01-01', 7)
-- SELECT * FROM actor WHERE number_oscars >= 5

-- ALTER TABLE actor DROP COLUMN nationality
-- SELECT * FROM actor
-- ALTER TABLE actor RENAME COLUMN nationality2 TO nationality
-- SELECT * FROM actor

-- Exercise

-- In the table actors, write the following commands:

-- Update the first name of Matt Damon to "Maty"
-- Update the number of oscars of George Clooney to 4, and return the updated record
-- Rename the 'age' column by 'birthdate'
-- Delete one actor and return it

-- UPDATE actor
-- SET first_name = 'Maty' WHERE last_name = 'Damon'
-- RETURNING *

-- UPDATE actor
-- SET number_oscars = 4 WHERE first_name = 'George'
-- RETURNING *

-- ALTER TABLE actor RENAME COLUMN date_birth TO age
-- SELECT * FROM actor

-- DELETE FROM actor
-- WHERE actor_id = 7
-- RETURNING *

-- DAILY CHALLENGE --------------------------------------------------


-- SELECT COUNT(*) AS row_count
-- FROM actor

-- SELECT * FROM actor

-- INSERT INTO actor (first_name, last_name, age,number_oscars, salary, nationality)
-- VALUES ('Hoakin', 'Pheonix', '1980-03-02', 3 , 10000000 , 'American')

-- SELECT * FROM actor

-- INSERT INTO actor (first_name, last_name, age,number_oscars, salary, nationality)
-- VALUES ('Hoakin', '', '1980-03-02', 3 , 10000000 , '')

-- SELECT * FROM actor


-- INSERT INTO actor (first_name, last_name, age,number_oscars, salary, nationality)
-- VALUES ('Hoakin','','',0,0,'' )

SELECT * FROM actor


