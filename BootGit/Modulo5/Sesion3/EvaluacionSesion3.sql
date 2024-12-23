-- Tabla Empresa
CREATE TABLE Empresa (
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Direccion VARCHAR(120),
    Telefono VARCHAR(15),
    Correo VARCHAR(80),
    Web VARCHAR(50)
);

-- Tabla Cliente
CREATE TABLE Cliente (
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Correo VARCHAR(80),
    Direccion VARCHAR(120),
    Celular VARCHAR(15)
);

-- Tabla Herramienta
CREATE TABLE Herramienta (
    IDHerramienta NUMBER(12) PRIMARY KEY,
    Nombre VARCHAR(120),
    PrecioDia NUMBER(12)
);

-- Tabla Arriendo
CREATE TABLE Arriendo (
    Folio NUMBER(12) PRIMARY KEY,
    Fecha DATE,
    Dias NUMBER(5),
    ValorDia NUMBER(12),
    Garantia VARCHAR(30),
    Herramienta_IDHerramienta NUMBER(12),
    Cliente_RUT VARCHAR(10),
    CONSTRAINT Arriendo_Herramienta_FK FOREIGN KEY (Herramienta_IDHerramienta) REFERENCES Herramienta(IDHerramienta),
    CONSTRAINT Arriendo_Cliente_FK FOREIGN KEY (Cliente_RUT) REFERENCES Cliente(RUT)
);

