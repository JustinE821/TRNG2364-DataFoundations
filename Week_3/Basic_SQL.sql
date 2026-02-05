
-- DDL language
CREATE TABLE student (
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(40),
	last_name VARCHAR(40),
	email VARCHAR(100),
	phone INT

)

CREATE TABLE instructor(
	instructor_id SERIAL PRIMARY KEY,
	first_name VARCHAR(40),
	last_name VARCHAR(40),
	degree VARCHAR(4)
)

CREATE TABLE course (
	course_id SERIAL PRIMARY KEY,
	course_name VARCHAR(50),
	credits INT CHECK (CREDITS > 0),
	instructor_id INT REFERENCES instructor(instructor_id)
)

-- our many to many table aka junction table
CREATE TABLE enrollment(
	enrollment_id SERIAL PRIMARY KEY,
	student_id INT REFERENCES student(student_id),
	course_id INT REFERENCES course(course_id),
	grade CHAR(2)
)

--DML to work with data inside the tables
INSERT INTO student (first_name, last_name, email, phone, major) 
VALUES ('Jasne', 'Dolette', 'jand@email.com', 3473948, 'CS')
('Jane', 'Doe', 'jdoe@email.com', 1231234),
('Peter', 'Parker', 'spidey@email.com', 7897894),
('Tony', 'Stark', 'ironman@email.com', 1234567);

INSERT INTO instructor (first_name, last_name, degree)
VALUES ('Cave', 'Johnson', 'BS'),
('John', 'Doe', 'BB'),
('Amanda', 'Dixie', 'ME');

INSERT INTO course (course_name, credits, instructor_id)
VALUES ('Algebra', 3, 1),
('International Foods', 2, 1),
('Biology', 4, 2),
('Database Systems', 3, 1);

INSERT INTO enrollment (student_id, course_id, grade)
VALUES (1, 1, 'A-'),
(1, 2, 'B'),
(2, 1, 'C');

-- DQL Data Query Language 
SELECT *
FROM student;


UPDATE enrollment
SET grade = 'B'
WHERE student_id = 1 AND course_id = 1;

DELETE FROM enrollment
WHERE grade = 'C';


--DDL changes structure, NOT data
ALTER TABLE student
ADD COLUMN major VARCHAR(50);

UPDATE student
SET major='CS' 
WHERE student_id = 1;

UPDATE student
SET major = 'MB'
WHERE student_id = 2;

UPDATE student
SET major = 'CS'
WHERE student_id = 3

--DQL
SELECT first_name, last_name, major 
FROM student
WHERE major = 'CS' AND last_name LIKE 'D%'
ORDER BY last_name ASC;--search for names starting with D %D is names that end with D

SELECT student_id,
	UPPER(last_name) AS last_name_upper,
	LOWER(first_name) AS first_name_lower,
	LENGTH(email) AS email_length
FROM student;

--Aggregate function
SELECT major,
	COUNT(*) AS total_students
FROM student 
GROUP BY major;


--Joins
--Inner Join - students who are enrolled in a course
SELECT 
	student.first_name,
	student.last_name,
	course.course_name
FROM enrollment
INNER JOIN student ON enrollment.student_id=student.student_id
INNER JOIN course ON enrollment.course_id=course.course_id;

--Left join nshow all students and their courses
SELECT 
	student.first_name,
	student.last_name,
	enrollment.course_id,
	course.course_name
FROM student
LEFT JOIN enrollment ON student.student_id=enrollment.student_id
LEFT JOIN course ON enrollment.course_id=course.course_id;

--Right join - shows all rows from the right table even if there is no match
SELECT
	student.first_name,
	student.last_name,
	enrollment.course_id,
	course.course_name
FROM enrollment
RIGHT JOIN course ON enrollment.course_id = course.course_id
RIGHT JOIN student ON enrollment.student_id = student.student_id;

SELECT
	student.first_name,
	student.last_name,
	enrollment.course_id,
	course.course_name
FROM student
RIGHT JOIN enrollment ON student.student_id = enrollment.student_id
RIGHT JOIN course ON enrollment.course_id = course.course_id;

--Full outer join - show all students and courses 
SELECT
	student.first_name,
	student.last_name,
	enrollment.course_id,
	course.course_name
FROM student
FULL JOIN enrollment ON student.student_id = enrollment.student_id
FULL JOIN course ON enrollment.course_id = course.course_id;

-- cross join - show all possible combinations between joined tables
-- not super useful, but possibly used in statistics
-- show all possible student-course combinations
SELECT
	student.first_name,
	student.last_name,
	course.course_name
FROM student
CROSS JOIN course;


-- Subqueries

-- Students in one or more course
SELECT * FROM student 
WHERE student_id IN(
	SELECT student_id
	FROM enrollment
	GROUP BY student_id
	HAVING COUNT(course_id) > 1
	ORDER BY student_id DESC
);


-- Courses that no students are enrolled in
SELECT * FROM course
WHERE course_id NOT IN (
	SELECT course_id FROM enrollment
);

-- Students who are not enrolled in any courses
SELECT * FROM student
WHERE student_id NOT IN (
	SELECT student_id FROM enrollment
);


-- stored Procedures
--are prepared SQL code that you can save and reuse
--good for if you have a sql query that gets used over and over again
--we can call our stored procedures to execute them
--Could call this from python instead of making a function

CREATE PROCEDURE selectAllStudents(OUT)
LANGUAGE plpgsql
AS $$
BEGIN
UPDATE student
SET major = p_major
WHERE student_id = 2;
END
$$;


CALL selectAllStudents();

--we can also give our stored procedures params
CREATE PROCEDURE selectmajorstudents(p_major varchar(2))
LANGUAGE plpgsql
AS $$
BEGIN
SELECT * FROM student WHERE major = p_major;
END $$;

CALL selectmajorstudents('CS');

--PUT P INFRONT TO SHOW ITS A PARAM
--Functions return a value, while a stored procedure does not
--functions are mainly used for calculations or building operations into a single DB call
--$$ marks the beginning and end of executable block
--DECLARE lets us declare variables for the function


CREATE OR REPLACE FUNCTION get_course_count(p_student_id INT)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
	total_courses INT;
BEGIN
	SELECT COUNT(*)
	INTO total_courses
	FROM enrollment
	WHERE student_id = p_student_id;
	RETURN total_courses;
END;
$$;

SELECT 
	first_name, 
	last_name, 
	get_course_count(student_id) AS course_count
FROM student;


SELECT *
FROM student;


