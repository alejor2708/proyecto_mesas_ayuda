-- ============================================
-- 02_consultas_analiticas
-- Proyecto: Mesas de Ayuda
-- Objetivo: validar y analizar la información
-- ============================================

-- 1) Usar la base de datos
USE proyecto_mesas_ayuda;

-- ============================================
-- A. VALIDACIONES BÁSICAS
-- ============================================

-- A1. Contar filas en la dimensión
SELECT COUNT(*) AS filas_dim
FROM dim_tipo_solicitud;

-- A2. Contar filas en la tabla de hechos
SELECT COUNT(*) AS filas_fact
FROM fact_mesas_ayuda;

-- A3. Verificar totales generales del dataset
SELECT 
    SUM(casos_abiertos) AS total_abiertos,
    SUM(casos_resueltos) AS total_resueltos,
    SUM(casos_atrasados) AS total_atrasados,
    SUM(casos_cerrados) AS total_cerrados
FROM fact_mesas_ayuda;

-- ============================================
-- B. CONSULTAS ANALÍTICAS
-- ============================================

-- B1. Casos por tipo principal
SELECT 
    d.tipo_principal,
    SUM(f.casos_abiertos) AS total_abiertos,
    SUM(f.casos_resueltos) AS total_resueltos,
    SUM(f.casos_cerrados) AS total_cerrados
FROM fact_mesas_ayuda f
JOIN dim_tipo_solicitud d
    ON f.tipo_id = d.tipo_id
GROUP BY d.tipo_principal
ORDER BY total_abiertos DESC;

-- B2. Top 10 tipos completos con más casos abiertos
SELECT 
    d.tipo_completo,
    SUM(f.casos_abiertos) AS total_abiertos
FROM fact_mesas_ayuda f
JOIN dim_tipo_solicitud d
    ON f.tipo_id = d.tipo_id
GROUP BY d.tipo_completo
ORDER BY total_abiertos DESC
LIMIT 10;

-- B3. Top 10 tipos completos con mayor tiempo promedio
SELECT 
    d.tipo_completo,
    AVG(f.tiempo_promedio_segundos) AS promedio_segundos
FROM fact_mesas_ayuda f
JOIN dim_tipo_solicitud d
    ON f.tipo_id = d.tipo_id
GROUP BY d.tipo_completo
ORDER BY promedio_segundos DESC
LIMIT 10;

-- B4. Tasa de resolución por tipo principal
SELECT 
    d.tipo_principal,
    SUM(f.casos_abiertos) AS abiertos,
    SUM(f.casos_resueltos) AS resueltos,
    ROUND(SUM(f.casos_resueltos) * 100.0 / NULLIF(SUM(f.casos_abiertos), 0), 2) AS tasa_resolucion_pct
FROM fact_mesas_ayuda f
JOIN dim_tipo_solicitud d
    ON f.tipo_id = d.tipo_id
GROUP BY d.tipo_principal
ORDER BY tasa_resolucion_pct DESC;

-- B5. Diferencia entre casos abiertos y cerrados por tipo principal
SELECT 
    d.tipo_principal,
    SUM(f.casos_abiertos) AS abiertos,
    SUM(f.casos_cerrados) AS cerrados,
    SUM(f.casos_abiertos) - SUM(f.casos_cerrados) AS diferencia
FROM fact_mesas_ayuda f
JOIN dim_tipo_solicitud d
    ON f.tipo_id = d.tipo_id
GROUP BY d.tipo_principal
ORDER BY diferencia DESC;

-- B6. Categorías sin casos atrasados
SELECT 
    d.tipo_completo,
    SUM(f.casos_atrasados) AS total_atrasados
FROM fact_mesas_ayuda f
JOIN dim_tipo_solicitud d
    ON f.tipo_id = d.tipo_id
GROUP BY d.tipo_completo
HAVING SUM(f.casos_atrasados) = 0
ORDER BY d.tipo_completo;