CREATE TABLE resident (
	resident_id SERIAL PRIMARY KEY,
	first_name VARCHAR(40),
	last_name VARCHAR(40),
	apartment_id INT REFERENCES apartment (apartment_id)
);

INSERT INTO resident (first_name, last_name, apartment_id)
VALUES ('Todd', 'Chillen', 1),
('Mary', 'Berry', 2),
('Leslie', 'Linkin', 3);



CREATE TABLE car_owner (
	owner_id  SERIAL PRIMARY KEY,
	resident_id INT REFERENCES resident (resident_id)
)

INSERT INTO car_owner(resident_id)
VALUES (1),
(2),
(3);


CREATE TABLE car (
	car_id SERIAL PRIMARY KEY,
	make VARCHAR(30),
	model VARCHAR(30),
	year_made INT,
	CHECK(year_made > 1900),
	CHECK(year_made < 2030),
	license_plate VARCHAR(12),
	owner_id INT REFERENCES car_owner (owner_id)
)

INSERT INTO car (make, model, year_made, license_plate, owner_id)
VALUES ('Honda', 'Civic', 2009, 'HOFS-WD3D', 1),
('Honda', 'Accord', 2020, 'HWSS-WQAD', 2),
('Nissan', 'Ultima', 1998, 'S35Y-BEESD', 3);



CREATE TABLE apartment (
	apartment_id SERIAL PRIMARY KEY,
	building_letter CHAR(1),
	room_number INT,
	monthly_rent DECIMAL(5,2)
)

INSERT INTO apartment (building_letter, room_number, monthly_rent)
VALUES ('B', 214, 130.00),
('C', 404, 200.00),
('C', 405, 400.00);


CREATE TABLE pet (
	pet_id SERIAL PRIMARY KEY,
	breed VARCHAR(40),
	pet_name VARCHAR(70),
	apartment_id INT REFERENCES apartment (apartment_id),
	is_service_animal BOOLEAN DEFAULT FALSE
)

INSERT INTO pet (breed, pet_name, apartment_id, is_service_animal)
VALUES ('Maine Coone', 'Trisco', 1, FALSE),
('German Sheppard', 'John', 2, TRUE),
('Dachshund', 'Willy', 3, FALSE);


SELECT *
FROM resident;

SELECT *
FROM resident
INNER JOIN apartment ON apartment.apartment_id=resident.apartment_id
WHERE building_letter='B';

SELECT building_letter, AVG(monthly_rent) as average_rent
FROM apartment
WHERE building_letter='C'
GROUP BY building_letter;

SELECT COUNT(pet_id) AS number_of_pets
FROM pet;




