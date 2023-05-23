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

SELECT * FROM customer_review -- the row which referes to deleted row in new_film (due to film_id) also was deleted.







