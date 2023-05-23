-- Exercise 1: DVD Rental

-- Instructions

-- Get a list of all film languages.

-- SELECT name FROM language


-- Get a list of all films joined with their languages – select the following details : film title, description, and language name. 
-- Try your query with different joins:

-- SELECT title, description, name FROM film
-- INNER JOIN language ON film.language_id = language.language_id


-- Get all films, even if they don’t have languages.

-- SELECT title, description, name FROM film
-- LEFT JOIN language ON film.language_id = language.language_id


-- Get all languages, even if there are no films in those languages.

-- SELECT title, description, name FROM film
-- RIGHT JOIN language ON film.language_id = language.language_id

-- CREATE TABLE new_film (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(100)
-- );

-- CREATE TABLE customer_review (
-- 	review_id SERIAL PRIMARY KEY,
-- 	film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
-- 	language_id INTEGER REFERENCES language(language_id) ON DELETE CASCADE,
-- 	title VARCHAR(20) NOT NULL,
-- 	score INTEGER NOT NULL,
-- 	review_text TEXT NOT NULL,
-- 	last_update DATE NOT NULL
-- );

-- INSERT INTO new_film (name)
-- VALUES 
-- ('Men in black'),
-- ('Batman'),
-- ('Iron man'),
-- ('Forrest Gump'),
-- ('Social network');

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
-- VALUES
-- (4, 1, 'Some review 1', 10, 'Some review text 1....', '2023-05-23'),
-- (2, 1, 'Some review 2', 8, 'Some review text 2....', '2023-05-23')

-- DELETE FROM new_film
-- WHERE id = 2

-- SELECT * FROM customer_review -- the row which referes to deleted row in new_film (due to film_id) also was deleted.

-- Exercise 2

-- UPDATE film
-- SET language_id = 2
-- WHERE title IN ('Angels Life', 'Academy Dinosaur');

-- SELECT * FROM film
-- ORDER BY title ASC

-- Which foreign keys (references) are defined for the customer table?
-- How does this affect the way in which we INSERT into the customer table?
-- 			When inserting data into a table with foreign keys, you need to ensure 
-- 			that the values you insert in the foreign key column(s) exist in the referenced 
-- 			table's primary key column(s). If you attempt to insert a value 
-- 			that doesn't exist in the referenced table, the database will raise an 
-- 			error, preventing the insertion.



-- SELECT COUNT(*) FROM rental
-- WHERE return_date is NULL

-- SELECT film.film_id, title, rental_rate, return_date FROM film
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
-- WHERE return_date is NULL
-- ORDER BY rental_rate DESC LIMIT 30

-- SELECT title FROM film
-- INNER JOIN film_actor ON film.film_id = film_actor.film_id 
-- INNER JOIN actor ON actor.actor_id = film_actor.actor_id
-- WHERE film.description ILIKE '%sumo%' AND actor.first_name ='Penelope' AND actor.last_name = 'Monroe'

-- SELECT title FROM film
-- INNER JOIN film_category ON film.film_id = film_category.film_id
-- INNER JOIN category ON film_category.category_id = category.category_id
-- WHERE length < 60 AND rating = 'R' AND category.name ILIKE '%document%'

-- SELECT title FROM film
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
-- INNER JOIN customer ON customer.customer_id = rental.customer_id
-- INNER JOIN payment ON payment.rental_id = rental.rental_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND payment.amount > 4 
-- AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'

-- SELECT title, replacement_cost FROM film
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
-- INNER JOIN customer ON customer.customer_id = rental.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
-- ORDER BY replacement_cost DESC LIMIT 1













