--1
-- insertar
INSERT INTO customer (store_id, first_name, last_name, email, address_id, activebool, create_date)
VALUES (1, 'Paola', 'Silver', 'paola@gmail.com', 9, TRUE, NOW());

INSERT INTO staff (first_name, last_name, address_id, email, store_id, username, password, active)
VALUES ('Paolaas', 'Silver', 6, 'paolas@gmail.cl', 1, 'psilver', 'admin', TRUE);

INSERT INTO actor (first_name, last_name)
VALUES ('Ursula', 'Corbero');

--modificar
UPDATE customer
SET email = 'pa@gmail.cl'
WHERE customer_id = 1;

UPDATE staff
SET email = 'psilver@outlook.coom'
WHERE staff_id = 1;

UPDATE actor
SET last_name = 'PaolaAFK'
WHERE actor_id = 1;

--eliminar

DELETE FROM customer
WHERE customer_id = 601;

DELETE FROM staff
WHERE staff_id = 3;

DELETE FROM actor
WHERE actor_id = 201;

--2
SELECT rental.rental_id, rental.rental_date, customer.first_name, customer.last_name
FROM rental
JOIN customer ON rental.customer_id = customer.customer_id
WHERE EXTRACT(YEAR FROM rental.rental_date) = 2006
AND EXTRACT(MONTH FROM rental.rental_date) = 2;

--3
SELECT payment.payment_id, payment.payment_date, payment.amount
FROM payment;

--4

SELECT film.title, film.release_year, film.rental_rate
FROM film
WHERE film.release_year = 2006
AND film.rental_rate > 4.0;

