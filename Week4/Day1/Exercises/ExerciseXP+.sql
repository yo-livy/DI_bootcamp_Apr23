-- CREATE TABLE students (
-- 	id SERIAL PRIMARY KEY,
-- 	last_name VARCHAR(100) NOT NULL,
-- 	first_name VARCHAR NOT NULL,
-- 	birth_date DATE NOT NULL
-- )
-- INSERT INTO students (last_name, first_name, birth_date)
-- VALUES 
-- ('Marc', 'Benichou', '1998-11-02'),
-- ('Yoan', 'Cohen', '2010-12-03'),
-- ('Lea', 'Benichou', '1987-07-27'),
-- ('Amelia', 'Dux', '1996-04-07'),
-- ('David', 'Grez', '2003-06-14'),
-- ('Omer', 'Simpson', '1980-10-03')

-- SELECT * FROM students
-- INSERT INTO students (last_name, first_name, birth_date)
-- VALUES ('Eugene', 'Livschitz', '1985-07-03')

-- SELECT * FROM students

-- SELECT first_name, last_name FROM students

-- SELECT first_name, last_name FROM students
-- WHERE id = 2

-- ALTER TABLE students
-- 	RENAME COLUMN first_name TO last_name1
-- ALTER TABLE students
-- 	RENAME COLUMN last_name TO first_name
-- ALTER TABLE students
-- 	RENAME COLUMN last_name1 TO last_name

-- SELECT first_name, last_name FROM students
-- WHERE last_name = 'Benichou' AND first_name = 'Marc'

-- SELECT first_name, last_name FROM students
-- WHERE last_name = 'Benichou' OR first_name = 'Marc'

-- SELECT first_name, last_name FROM students
-- WHERE first_name ILIKE '%a%'

-- SELECT first_name, last_name FROM students
-- WHERE first_name ILIKE 'a%'

-- SELECT first_name, last_name FROM students
-- WHERE first_name ILIKE '%a'

-- SELECT first_name, last_name FROM students
-- WHERE first_name ILIKE '%a_'

-- SELECT first_name, last_name FROM students
-- WHERE id = 3 OR id = 5

-- SELECT * FROM students
-- WHERE birth_date >= '2000-01-01'





