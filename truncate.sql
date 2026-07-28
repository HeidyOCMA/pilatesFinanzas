USE pilatesFinanzas;
CREATE INDEX idx_ingresos_fecha
ON ingresos(fecha);
commit;
CREATE INDEX idx_gastos_fecha
ON gastos(fecha);

CREATE INDEX idx_asistencias_fecha
ON asistencias(fecha);

CREATE INDEX idx_cliente
ON clientes(id_cliente);

CREATE INDEX idx_instructor
ON instructores(id);
-- 1. Asegurar el motor InnoDB
ALTER TABLE clientes ENGINE = InnoDB;

-- 2. Limpiar la tabla
TRUNCATE TABLE clientes;
TRUNCATE TABLE instructores;
TRUNCATE TABLE ingresos;
TRUNCATE TABLE gastos;

-- 3. Optimizar la tabla para liberar espacio retenido en disco
OPTIMIZE TABLE clientes;CREATE INDEX idx_ventas_fecha
ON ventas(fecha);
CREATE INDEX idx_ventas_fecha
ON ventas(fecha);
CREATE INDEX idx_ventas_fecha
ON ventas(fecha);

ALTER TABLE ingresos MODIFY COLUMN fecha DATE;

-- 2. Cambiar también el tipo de dato en 'gastos' (si aplica)
ALTER TABLE gastos MODIFY COLUMN fecha DATE;

-- 3. Ahora sí, crear el índice sin ningún problema:
CREATE INDEX idx_ingresos_fecha ON ingresos(fecha);
CREATE INDEX idx_gastos_fecha ON gastos(fecha);
