CREATE TABLE Empresa (
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Direccion VARCHAR(120),
    Telefono VARCHAR(20),
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
    IDTipoVehiculo NUMBER(12) PRIMARY KEY,
    Nombre VARCHAR(120)
);

CREATE TABLE Marca (
    IDMarca NUMBER(12) PRIMARY KEY,
    Nombre VARCHAR(120)
);

CREATE TABLE Vehiculo (
    IDVehiculo NUMBER(12) PRIMARY KEY,
    Patente VARCHAR(10),
    Marca_IDMarca NUMBER(12),
    Modelo VARCHAR(20),
    Color VARCHAR(15),
    Precio NUMBER,
    FrecuenciaMantenimiento NUMBER,
    TipoVehiculo_IDTipoVehiculo NUMBER(12),
    FOREIGN KEY (Marca_IDMarca) REFERENCES Marca(IDMarca),
    FOREIGN KEY (TipoVehiculo_IDTipoVehiculo) REFERENCES TipoVehiculo(IDTipoVehiculo)
);

CREATE TABLE Venta (
    Folio NUMBER(12) PRIMARY KEY,
    Fecha DATE,
    Monto NUMBER,
    Vehiculo_IDVehiculo NUMBER(12),
    Cliente_RUT VARCHAR(10),
    FOREIGN KEY (Vehiculo_IDVehiculo) REFERENCES Vehiculo(IDVehiculo),
    FOREIGN KEY (Cliente_RUT) REFERENCES Cliente(RUT)
);

CREATE TABLE Mantenimiento (
    IDMantenimiento NUMBER(12) PRIMARY KEY,
    Fecha DATE,
    TrabajosRealizados VARCHAR(1000),
    Venta_Folio NUMBER(12),
    FOREIGN KEY (Venta_Folio) REFERENCES Venta(Folio)
);


----------------------------

SELECT *
FROM Vehiculo V
WHERE NOT EXISTS (
    SELECT 1
    FROM Venta VE
    WHERE VE.Vehiculo_IDVehiculo = V.IDVehiculo
);

SELECT VE.Folio, VE.Fecha, VE.Monto, C.Nombre AS NombreCliente, C.RUT AS RutCliente,
       V.Patente, M.Nombre AS NombreMarca, V.Modelo
FROM Venta VE
JOIN Cliente C ON VE.Cliente_RUT = C.RUT
JOIN Vehiculo V ON VE.Vehiculo_IDVehiculo = V.IDVehiculo
JOIN Marca M ON V.Marca_IDMarca = M.IDMarca
WHERE EXTRACT(YEAR FROM VE.Fecha) = 2020
  AND EXTRACT(MONTH FROM VE.Fecha) = 1;

SELECT EXTRACT(MONTH FROM VE.Fecha) AS Mes, M.Nombre AS NombreMarca, SUM(VE.Monto) AS TotalVentas
FROM Venta VE
JOIN Vehiculo V ON VE.Vehiculo_IDVehiculo = V.IDVehiculo
JOIN Marca M ON V.Marca_IDMarca = M.IDMarca
WHERE EXTRACT(YEAR FROM VE.Fecha) = 2020
GROUP BY EXTRACT(MONTH FROM VE.Fecha), M.Nombre
ORDER BY Mes, NombreMarca;

SELECT RUT, Nombre
FROM Cliente
UNION ALL
SELECT RUT, Nombre
FROM Empresa;



