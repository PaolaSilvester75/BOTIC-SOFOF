CREATE DATABASE empresa;

CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ubicacion VARCHAR(100)
);


CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    puesto VARCHAR(100),
    salario DECIMAL(10, 2),
    fecha_contratacion DATE,
    departamento_id INT,
    CONSTRAINT fk_departamento FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

ALTER TABLE empleados
ADD COLUMN email VARCHAR(100);

ALTER TABLE empleados
RENAME TO trabajadores;

DROP TABLE departamentos;
