INSERT INTO Cliente (RUT, Nombre, Correo, Direccion, Celular)
VALUES
('888888888', 'Fake Cliente 91', 'fake@gmail.com', 'Dirección 91', '45353454353'),
('999999999', 'Fake Cliente 92', 'fakes2@gmail.com', 'Dirección 92', '757457453');


INSERT INTO Herramienta (IDHerramienta, Nombre, PrecioDia)
VALUES
(1, 'Fake Herramienta 93', 93.00),
(2, 'Fake Herramienta 94', 94.00);

INSERT INTO Arriendo (Folio, Fecha, Dias, ValorDia, Garantia, Herramienta_IDHerramienta, Cliente_RUT)
VALUES
(1, '2020-05-01', 3, 95.00, '500', 1, '333333333'),
(2, '2020-05-05', 5, 96.00, '300', 2, '444444444');


SELECT A.Folio, A.Fecha, A.Dias, A.ValorDia, C.Nombre AS NombreCliente, C.RUT AS RutCliente
FROM Arriendo A
JOIN Cliente C ON A.Cliente_RUT = C.RUT;

SELECT C.*
FROM Cliente C
WHERE NOT EXISTS (
    SELECT 1
    FROM Arriendo A
    WHERE A.Cliente_RUT = C.RUT
);

SELECT RUT, Nombre
FROM Empresa
UNION ALL
SELECT RUT, Nombre
FROM Cliente;

SELECT EXTRACT(MONTH FROM A.Fecha) AS Mes, COUNT(*) AS CantidadArriendos
FROM Arriendo A
GROUP BY EXTRACT(MONTH FROM A.Fecha)
ORDER BY Mes;


