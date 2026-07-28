--CREATE DATABASE pilatesFinanzas
--CHARACTER SET utf8mb4
--COLLATE utf8mb4_unicode_ci;

USE pilatesFinanzas;
-- ----------------------------------------------------
-- Tabla 1: Clientes
-- ----------------------------------------------------
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    sexo ENUM('F', 'M') NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(150),
    fecha_registro DATE NOT NULL,
    sucursal_preferida VARCHAR(50) NOT NULL
);

-- ----------------------------------------------------
-- Tabla 2: Instructores
-- ----------------------------------------------------
CREATE TABLE IF NOT EXISTS instructores (
    id_instructor VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    especialidad VARCHAR(50) NOT NULL,
    fecha_ingreso DATE NOT NULL
);

-- ----------------------------------------------------
-- Tabla 3: Ingresos (Estructura para la Premisa 1)
-- ----------------------------------------------------
CREATE TABLE IF NOT EXISTS ingresos (
    id_transaccion INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    cliente VARCHAR(150) NOT NULL,
    tipo_venta VARCHAR(50) NOT NULL,
    clase VARCHAR(50) NOT NULL,
    aparato VARCHAR(50) NOT NULL,
    paquete INT DEFAULT 0,
    fitpass VARCHAR(5) NOT NULL,
    sucursal VARCHAR(50) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    INDEX idx_fecha (fecha),
    INDEX idx_sucursal (sucursal),
    INDEX idx_cliente (cliente)
);

-- ----------------------------------------------------
-- Tabla 4: Gastos
-- ----------------------------------------------------
CREATE TABLE IF NOT EXISTS gastos (
    id_gasto INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    tipo_gasto VARCHAR(100) NOT NULL,
    costo DECIMAL(10, 2) NOT NULL,
    sucursal VARCHAR(50) NOT NULL,
    INDEX idx_fecha_gasto (fecha),
    INDEX idx_sucursal_gasto (sucursal)
);
2. Script para cargar los datos desde los archivos CSV
Asegúrate de reemplazar /ruta/hacia/tu/archivo/ por la ruta absoluta donde guardaste los archivos en tu equipo (utilizando diagonales normales /).

Nota importante: Si tu servidor MySQL tiene activa la variable local_infile, asegúrate de incluir LOCAL en la instrucción LOAD DATA LOCAL INFILE.

SQL
USE pilates_finanzas;

-- 1. Cargar Clientes
LOAD DATA INFILE '/ruta/hacia/tu/archivo/clientes.csv'
INTO TABLE clientes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id_cliente, nombre, sexo, telefono, email, fecha_registro, sucursal_preferida);

-- 2. Cargar Instructores
LOAD DATA INFILE '/ruta/hacia/tu/archivo/instructores.csv'
INTO TABLE instructores
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id_instructor, nombre, especialidad, fecha_ingreso);

-- 3. Cargar Ingresos
LOAD DATA INFILE '/ruta/hacia/tu/archivo/ingresos.csv'
INTO TABLE ingresos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(fecha, cliente, tipo_venta, clase, aparato, paquete, fitpass, sucursal, total);

-- 4. Cargar Gastos
LOAD DATA INFILE '/ruta/hacia/tu/archivo/gastos.csv'
INTO TABLE gastos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(fecha, tipo_gasto, costo, sucursal);