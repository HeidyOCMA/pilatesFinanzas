show databases
CREATE DATABASE pilates_finanzas
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE pilates_finanzas;

CREATE TABLE sucursales (

    id_sucursal INT AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(80) NOT NULL,

    direccion VARCHAR(200),

    telefono VARCHAR(20),

    fecha_apertura DATE,

    activo BOOLEAN DEFAULT TRUE

);

CREATE TABLE sucursales (

    id_sucursal INT AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(80) NOT NULL,

    direccion VARCHAR(200),

    telefono VARCHAR(20),

    fecha_apertura DATE,

    activo BOOLEAN DEFAULT TRUE

);