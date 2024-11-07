-- Tabla Empresa
CREATE TABLE Empresa (
    RUT VARCHAR2(10) PRIMARY KEY,
    Nombre VARCHAR2(120),
    Direccion VARCHAR2(120),
    Telefono VARCHAR2(15),
    Correo VARCHAR2(80),
    Web VARCHAR2(50)
);

-- Tabla Cliente
CREATE TABLE Cliente (
    RUT VARCHAR2(10) PRIMARY KEY,
    Nombre VARCHAR2(120),
    Correo VARCHAR2(80),
    Direccion VARCHAR2(120),
    Celular VARCHAR2(15),
    Alta CHAR(1)
);

-- Tabla TipoVehiculo
CREATE TABLE TipoVehiculo (
    IDTipoVehiculo NUMBER(12) PRIMARY KEY,
    Nombre VARCHAR2(120)
);

-- Tabla Marca
CREATE TABLE Marca (
    IDMarca NUMBER(12) PRIMARY KEY,
    Nombre VARCHAR2(120)
);

-- Tabla Vehiculo
CREATE TABLE Vehiculo (
    IDVehiculo NUMBER(12) PRIMARY KEY,
    Patente VARCHAR2(10),
    Marca VARCHAR2(20),
    Modelo VARCHAR2(20),
    Color VARCHAR2(15),
    Precio NUMBER(12),
    FrecuenciaMantenimiento NUMBER(5),
    Marca_IDMarca NUMBER(12),
    TipoVehiculo_IDTipoVehiculo NUMBER(12),
    CONSTRAINT Vehiculo_Marca_FK FOREIGN KEY (Marca_IDMarca) REFERENCES Marca(IDMarca),
    CONSTRAINT Vehiculo_TipoVehiculo_FK FOREIGN KEY (TipoVehiculo_IDTipoVehiculo) REFERENCES TipoVehiculo(IDTipoVehiculo)
);

-- Tabla Venta
CREATE TABLE Venta (
    Folio NUMBER(12) PRIMARY KEY,
    Fecha DATE,
    Monto NUMBER(12),
    Vehiculo_IDVehiculo NUMBER(12),
    Cliente_RUT VARCHAR2(10),
    CONSTRAINT Venta_Cliente_FK FOREIGN KEY (Cliente_RUT) REFERENCES Cliente(RUT),
    CONSTRAINT Venta_Vehiculo_FK FOREIGN KEY (Vehiculo_IDVehiculo) REFERENCES Vehiculo(IDVehiculo)
);

-- Tabla Mantencion
CREATE TABLE Mantencion (
    IDMantencion NUMBER(12) PRIMARY KEY,
    Fecha DATE,
    TrabajosRealizados VARCHAR2(1000),
    Venta_Folio NUMBER(12),
    CONSTRAINT Mantencion_Venta_FK FOREIGN KEY (Venta_Folio) REFERENCES Venta(Folio)
);

