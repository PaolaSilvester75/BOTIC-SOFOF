CREATE TABLE Empresa (
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Direccion VARCHAR(120),
    Telefono VARCHAR(15),
    Correo VARCHAR(80),
    Web VARCHAR(50)
);

CREATE TABLE Cliente (
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Correo VARCHAR(80),
    Direccion VARCHAR(120),
    Celular VARCHAR(15),
    Alta CHAR(1)
);

CREATE TABLE TipoVehiculo (
    IDTipoVehiculo SERIAL PRIMARY KEY,
    Nombre VARCHAR(120)
);

CREATE TABLE Marca (
    IDMarca SERIAL PRIMARY KEY,
    Nombre VARCHAR(120)
);

CREATE TABLE Vehiculo (
    IDVehiculo SERIAL PRIMARY KEY,
    Patente VARCHAR(10),
    Marca VARCHAR(20),
    Modelo VARCHAR(20),
    Color VARCHAR(15),
    Precio NUMERIC(12,2),
    FrecuenciaMantenimiento INT,
    Marca_IDMarca INT REFERENCES Marca(IDMarca),
    TipoVehiculo_IDTipoVehiculo INT REFERENCES TipoVehiculo(IDTipoVehiculo)
);

CREATE TABLE Venta (
    Folio SERIAL PRIMARY KEY,
    Fecha DATE,
    Monto NUMERIC(12,2),
    Vehiculo_IDVehiculo INT REFERENCES Vehiculo(IDVehiculo),
    Cliente_RUT VARCHAR(10) REFERENCES Cliente(RUT)
);

CREATE TABLE Mantencion (
    IDMantencion SERIAL PRIMARY KEY,
    Fecha DATE,
    TrabajosRealizados VARCHAR(1000),
    Venta_Folio INT REFERENCES Venta(Folio)
);




--1 quest

SELECT Nombre, RUT
FROM Cliente
WHERE RUT NOT IN (
    SELECT Cliente_RUT
    FROM Venta
);

--2 quest
SELECT V.Folio, V.Fecha, V.Monto, C.Nombre AS NombreCliente, C.RUT AS RutCliente
FROM Venta V
JOIN Cliente C ON V.Cliente_RUT = C.RUT;

--3 quest
SELECT C.Nombre, C.RUT,
       CASE 
           WHEN SUM(V.Monto) BETWEEN 0 AND 1000000 THEN 'Standar'
           WHEN SUM(V.Monto) BETWEEN 1000001 AND 3000000 THEN 'Gold'
           WHEN SUM(V.Monto) > 3000000 THEN 'Premium'
       END AS Clasificacion
FROM Cliente C
LEFT JOIN Venta V ON C.RUT = V.Cliente_RUT
GROUP BY C.Nombre, C.RUT;

--4 quesat

SELECT V.Folio, V.Fecha, V.Monto, MA.Nombre AS Marca
FROM Venta V
JOIN Vehiculo VE ON V.Vehiculo_IDVehiculo = VE.IDVehiculo
JOIN Marca MA ON VE.Marca_IDMarca = MA.IDMarca
WHERE MA.Nombre = (
    SELECT MA2.Nombre
    FROM Vehiculo VE2
    JOIN Marca MA2 ON VE2.Marca_IDMarca = MA2.IDMarca
    GROUP BY MA2.Nombre
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

