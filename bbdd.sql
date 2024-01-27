CREATE DATABASE empleados;

USE empleados;

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    telefono VARCHAR(15)
);

INSERT INTO empleados (nombre, apellido, email, telefono) VALUES ('Juan', 'Perez', 'juan.perez@example.com', '1234567890');

INSERT INTO empleados (nombre, apellido, email, telefono) VALUES ('Maria', 'Gomez', 'maria.gomez@example.com', '0987654321');