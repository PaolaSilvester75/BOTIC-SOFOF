CREATE TABLE Empresa (
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Direccion VARCHAR(120),
    Telefono VARCHAR(15),
    Correo VARCHAR(80),
    Web VARCHAR(50)
);

CREATE TABLE Herramienta (
    IDHerramienta BIGINT PRIMARY KEY,
    Nombre VARCHAR(120),
    PrecioDia NUMERIC(12, 2)
);

CREATE TABLE Cliente (
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Correo VARCHAR(80),
    Direccion VARCHAR(120),
    Celular VARCHAR(15)
);

CREATE TABLE Arriendo (
    Folio BIGINT PRIMARY KEY,
    Fecha DATE,
    Dias INTEGER,
    ValorDia NUMERIC(12, 2),
    Garantia VARCHAR(30),
    Herramienta_IDHerramienta BIGINT REFERENCES Herramienta(IDHerramienta),
    Cliente_RUT VARCHAR(10) REFERENCES Cliente(RUT)
);


SELECT Nombre, RUT
FROM Cliente
WHERE RUT NOT IN (
    SELECT DISTINCT Cliente_RUT
    FROM Arriendo
);

SELECT a.Folio, a.Fecha, a.Dias, a.ValorDia, c.Nombre AS NombreCliente, c.RUT AS RutCliente
FROM Arriendo a
JOIN Cliente c ON a.Cliente_RUT = c.RUT;

SELECT c.Nombre, c.RUT, COUNT(a.Folio) AS CantidadArriendosMensuales,
       CASE
           WHEN COUNT(a.Folio) BETWEEN 0 AND 1 THEN 'Bajo'
           WHEN COUNT(a.Folio) BETWEEN 2 AND 3 THEN 'Medio'
           ELSE 'Alto'
       END AS Clasificacion
FROM Cliente c
LEFT JOIN Arriendo a ON c.RUT = a.Cliente_RUT
GROUP BY c.RUT;

SELECT c.Nombre, c.RUT, h.Nombre AS HerramientaMasArrendada
FROM Cliente c
JOIN Arriendo a ON c.RUT = a.Cliente_RUT
JOIN Herramienta h ON a.Herramienta_IDHerramienta = h.IDHerramienta
WHERE h.IDHerramienta = (
    SELECT a.Herramienta_IDHerramienta
    FROM Arriendo a
    GROUP BY a.Herramienta_IDHerramienta
    ORDER BY COUNT(a.Herramienta_IDHerramienta) DESC
    LIMIT 1
);

