CREATE TABLE editoriales (
    codigo INT PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE libros (
    codigo INT PRIMARY KEY,
    titulo VARCHAR(150),
    codigoeditorial INT,
    autor VARCHAR(100),
    precio DECIMAL(10, 2),
    CONSTRAINT fk_editorial FOREIGN KEY (codigoeditorial) REFERENCES editoriales(codigo)
);

INSERT INTO editoriales (codigo, nombre) 
VALUES (1, 'Anaya'), 
       (2, 'Andina'), 
       (3, 'S.M.');

INSERT INTO libros (codigo, titulo, codigoeditorial, autor, precio) 
VALUES (1, 'Don Quijote de La Mancha I', 1, 'Miguel de Cervantes', 150),
       (2, 'El principito', 2, 'Antoine SaintExupery', 120),
       (3, 'El príncipe', 3, 'Maquiavelo', 180),
       (4, 'Diplomacia', 3, 'Henry Kissinger', 170),
       (5, 'Don Quijote de La Mancha II', 1, 'Miguel de Cervantes', 140);


INSERT INTO libros (codigo, titulo, codigoeditorial, autor, precio) 
VALUES (6, 'Cien años de soledad', 2, 'Gabriel García Márquez', 130),
       (7, '1984', 1, 'George Orwell', 110);

BEGIN;
DELETE FROM libros WHERE codigoeditorial = 1;

ROLLBACK;
UPDATE editoriales SET nombre = 'Iberlibro' WHERE nombre = 'Andina';
SAVEPOINT actualizacion_nombre;
UPDATE editoriales SET nombre = 'Mountain' WHERE nombre = 'S.M.';
ROLLBACK TO actualizacion_nombre;
COMMIT;

