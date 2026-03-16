-- ============================================
-- 01_estructura_bd
-- Proyecto: Mesas de Ayuda
-- Objetivo: crear la base de datos y las tablas
-- ============================================

-- 1) Crear la base de datos
CREATE DATABASE IF NOT EXISTS proyecto_mesas_ayuda;

-- 2) Usar la base de datos
USE proyecto_mesas_ayuda;

-- 3) Eliminar tablas si ya existían (para rehacer pruebas)
DROP TABLE IF EXISTS fact_mesas_ayuda;
DROP TABLE IF EXISTS dim_tipo_solicitud;

-- 4) Crear tabla dimensión
CREATE TABLE dim_tipo_solicitud (
    tipo_id INT PRIMARY KEY,
    tipo_principal VARCHAR(100) NOT NULL,
    subtipo VARCHAR(150),
    tipo_completo VARCHAR(200) NOT NULL
);

-- 5) Crear tabla de hechos
CREATE TABLE fact_mesas_ayuda (
    registro_id INT PRIMARY KEY,
    anio INT NOT NULL,
    tipo_id INT NOT NULL,
    casos_abiertos INT NOT NULL,
    casos_resueltos INT NOT NULL,
    casos_atrasados INT NOT NULL,
    casos_cerrados INT NOT NULL,
    tiempo_promedio_segundos INT NOT NULL,
    CONSTRAINT fk_tipo_solicitud
        FOREIGN KEY (tipo_id)
        REFERENCES dim_tipo_solicitud(tipo_id)
);

-- 6) Verificación básica de estructura
SHOW TABLES;

DESCRIBE dim_tipo_solicitud;
DESCRIBE fact_mesas_ayuda;