INSERT INTO Empresa (RUT, Nombre, Direccion, Telefono, Correo, Web)
VALUES ('12345678-9', 'Empresas techs.', 'Av. Principal 123', '123456789', 'fake@empresa.cl', 'www.fakeempresa.com');

INSERT INTO Herramienta (IDHerramienta, Nombre, PrecioDia)
VALUES (1, 'Martillo', 10.00),
       (2, 'Taladro', 20.00),
       (3, 'Sierra', 15.00),
       (4, 'Llave Inglesa', 12.00),
       (5, 'Destornillador', 8.00);

INSERT INTO Cliente (RUT, Nombre, Correo, Direccion, Celular)
VALUES ('11111111-1', 'Juan Perez', 'juan@correo.com', 'Calle Falsa 123', '987654321'),
       ('22222222-2', 'Ana Gomez', 'ana@correo.com', 'Calle Real 456', '876543210'),
       ('33333333-3', 'Pedro Lopez', 'pedro@correo.com', 'Avenida Norte 789', '765432109');

DELETE FROM Cliente
WHERE RUT = '33333333-3';

DELETE FROM Herramienta
WHERE IDHerramienta = 1;

INSERT INTO Arriendo (Folio, Fecha, Dias, ValorDia, Garantia, Herramienta_IDHerramienta, Cliente_RUT)
VALUES 
(1, '2023-10-01', 3, 10.00, 'Sin daños', 2, '11111111-1'),
(2, '2023-10-05', 5, 20.00, 'Garantía completa', 3, '11111111-1'),
(3, '2023-10-02', 2, 12.00, 'Sin daños', 4, '22222222-2'),
(4, '2023-10-06', 7, 8.00, 'Garantía parcial', 5, '22222222-2');

UPDATE Cliente
SET Correo = 'nuevojuan@correo.com'
WHERE RUT = '11111111-1';

SELECT * FROM Herramienta;

SELECT * FROM Arriendo
WHERE Cliente_RUT = '22222222-2';

SELECT * FROM Cliente
WHERE Nombre LIKE '%a%';

SELECT Nombre FROM Herramienta
WHERE IDHerramienta = 2;

UPDATE Arriendo
SET Fecha = '2020-01-15'
WHERE Folio IN (1, 2);

SELECT Folio, Fecha, ValorDia
FROM Arriendo
WHERE Fecha BETWEEN '2020-01-01' AND '2020-01-31';

