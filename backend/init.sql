CREATE TABLE usuarios_propietarios (
  id_propietario SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  correo VARCHAR(100),
  clave_hash VARCHAR(100)
);

CREATE TABLE cadenas (
  id_cadena SERIAL PRIMARY KEY,
  id_propietario INT REFERENCES usuarios_propietarios(id_propietario),
  nombre VARCHAR(100),
  descripcion TEXT
);

CREATE TABLE cliente (
  id_cliente SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  correo VARCHAR(100),
  clave_hash VARCHAR(100)
);

CREATE TABLE local (
  id_local SERIAL PRIMARY KEY,
  id_cadena INT REFERENCES cadenas(id_cadena),
  nombre VARCHAR(100),
  direccion VARCHAR(100)
);

CREATE TABLE mesas (
  id_mesa SERIAL PRIMARY KEY,
  numero INT,
  id_local INT REFERENCES local(id_local)
);

CREATE TABLE trabajadores (
  id_trabajador SERIAL PRIMARY KEY,
  id_local INT REFERENCES local(id_local),
  nombre VARCHAR(100),
  apellido VARCHAR(100),
  cargo VARCHAR(50),
  correo VARCHAR(100),
  clave_hash VARCHAR(100)
);

CREATE TABLE productos (
  id_producto SERIAL PRIMARY KEY,
  id_cadena INT REFERENCES cadenas(id_cadena),
  nombre VARCHAR(100),
  descripcion TEXT,
  precio FLOAT
);

CREATE TABLE ordenes (
  id_orden SERIAL PRIMARY KEY,
  fecha TIMESTAMP,
  id_cliente INT REFERENCES cliente(id_cliente),
  id_empleado INT REFERENCES trabajadores(id_trabajador),
  id_mesa INT REFERENCES mesas(id_mesa),
  estado VARCHAR(50)
);

CREATE TABLE ventas (
  id_venta SERIAL PRIMARY KEY,
  id_cliente INT REFERENCES cliente(id_cliente),
  id_orden INT REFERENCES ordenes(id_orden),
  fecha TIMESTAMP,
  valor FLOAT
);
