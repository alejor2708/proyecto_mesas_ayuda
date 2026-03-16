# Proyecto Mesas de Ayuda

Proyecto de base de datos relacional y dashboard analítico construido a partir de un dataset abierto de **Mesas de Ayuda**, trabajado mediante un flujo de limpieza en Python, modelado relacional en MySQL y visualización posterior en Streamlit.

---

## 1. Descripción del proyecto

Este proyecto tiene como objetivo transformar un archivo CSV de origen abierto en una solución estructurada de análisis de datos compuesta por:

- modelo entidad-relación (MER),
- modelo relacional,
- scripts SQL de creación y carga,
- consultas analíticas,
- dashboard interactivo en Streamlit,
- documentación final publicada en GitHub.

El proyecto fue desarrollado en un entorno con:

- Ubuntu
- MySQL Workbench
- MySQL Server
- VS Code
- Google Colab / Jupyter

---

## 2. Contexto del dataset

El dataset trabajado corresponde a registros de **Mesas de Ayuda** obtenidos desde una fuente abierta en formato CSV.

Una aclaración importante del proyecto es que el archivo original **no contiene tickets individuales**, sino **registros agregados por tipo de solicitud**.  
Cada fila resume métricas como:

- casos abiertos,
- casos resueltos,
- casos atrasados,
- casos cerrados,
- tiempo promedio de solución.

Por esta razón, el archivo no se importó directamente “tal cual” a MySQL.  
Primero se realizó un proceso de limpieza, transformación y modelado en Python/pandas para estructurar correctamente la información antes de implementarla como una base de datos relacional.

---

## 3. Proceso general de trabajo

El flujo del proyecto fue el siguiente:

1. Carga del CSV original en Google Colab / Jupyter.
2. Limpieza y renombrado de columnas.
3. Transformación de la columna `tipo_solicitud` en:
   - `tipo_principal`
   - `subtipo`
   - `tipo_completo`
4. Conversión de `tiempo_promedio` a `tiempo_promedio_segundos`.
5. Construcción de dos tablas derivadas:
   - `dim_tipo_solicitud`
   - `fact_mesas_ayuda`
6. Exportación de archivos CSV listos para MySQL.
7. Creación de la base de datos `proyecto_mesas_ayuda`.
8. Carga de tablas y definición de claves primarias y foránea.
9. Ejecución de validaciones y consultas analíticas.
10. Preparación del repositorio GitHub para la entrega final.

---

## 4. Modelo de datos

La base de datos implementada en MySQL es **relacional**.

### Base de datos
`proyecto_mesas_ayuda`

### Tablas principales

#### `dim_tipo_solicitud`
Tabla dimensional que contiene la clasificación de los tipos de solicitud.

Campos principales:
- `tipo_id` (PK)
- `tipo_principal`
- `subtipo`
- `tipo_completo`

#### `fact_mesas_ayuda`
Tabla de hechos con las métricas agregadas del dataset.

Campos principales:
- `registro_id` (PK)
- `tipo_id` (FK)
- `casos_abiertos`
- `casos_resueltos`
- `casos_atrasados`
- `casos_cerrados`
- `tiempo_promedio_segundos`

### Relación
- `dim_tipo_solicitud (1) -> (N) fact_mesas_ayuda`

---

## 5. Validaciones realizadas

Después de la carga en MySQL, se validó la coherencia de la información con los siguientes resultados:

- filas en `dim_tipo_solicitud`: **63**
- filas en `fact_mesas_ayuda`: **63**
- total casos abiertos: **2109**
- total casos resueltos: **2106**
- total casos atrasados: **0**
- total casos cerrados: **2106**

Estas validaciones confirmaron que la carga y transformación quedaron consistentes respecto a los archivos procesados.

---

## 6. Hallazgos principales

Entre los principales hallazgos identificados hasta esta etapa del proyecto se encuentran:

- La categoría con mayor carga de casos es **Acceso**.
- El tipo completo con mayor número de casos es **Acceso > SICAU**, con **663 casos abiertos**.
- Existe una anomalía reportable en **Acompañamiento**, que presenta una tasa de resolución superior al 100%, lo que sugiere una posible particularidad o inconsistencia en la fuente de datos.
- También se observan pequeñas diferencias entre casos abiertos y cerrados en categorías como **Software** y **Redes**.

---

## 7. Estructura del repositorio

```text
proyecto_mesas_ayuda/
├── app/                  # Dashboard en Streamlit
├── assets/
│   └── img/              # Imágenes y recursos visuales
├── data/
│   ├── raw/              # Datos originales
│   └── processed/        # Datos limpios y transformados
├── docs/                 # Documentación del proyecto y evidencias
├── notebooks/            # Notebook de trabajo y exploración
├── sql/                  # Scripts SQL de creación, carga y consultas
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 8. Archivos principales del proyecto

### Datos
- `data/raw/Mesas_de_ayuda.csv`
- `data/processed/mesas_ayuda_limpio.csv`
- `data/processed/dim_tipo_solicitud.csv`
- `data/processed/fact_mesas_ayuda.csv`

### SQL
- `sql/01_modelo_y_carga.sql`
- `sql/02_consultas_analiticas.sql`

### Documentación
- `docs/proceso_proyecto_mesas_ayuda.pdf`

### Notebook
- `notebooks/primera_entrega.ipynb`

---

## 9. Tecnologías utilizadas

- Python
- pandas
- MySQL
- MySQL Workbench
- Streamlit
- Git
- GitHub

---

## 10. Estado actual del proyecto

Actualmente el proyecto tiene completadas las siguientes fases:

- limpieza y transformación del dataset,
- modelado relacional,
- creación y carga de la base de datos en MySQL,
- validaciones SQL,
- consultas analíticas iniciales,
- organización del repositorio en GitHub.

Fases pendientes o en desarrollo:

- construcción del dashboard en Streamlit,
- definición de la landing page,
- exportación y publicación del MER,
- documentación final de entrega.

---

## 11. Cómo ejecutar el proyecto

### SQL
1. Crear la base de datos `proyecto_mesas_ayuda` en MySQL.
2. Ejecutar el script `sql/01_modelo_y_carga.sql`.
3. Ejecutar el script `sql/02_consultas_analiticas.sql`.

### Notebook
Abrir el archivo `notebooks/primera_entrega.ipynb` para revisar el proceso de limpieza y transformación de datos.

### Dashboard
El dashboard en Streamlit será agregado en la carpeta `app/` en la siguiente fase del proyecto.

---

## 12. Próximos pasos

Los siguientes pasos del proyecto son:

1. construir el dashboard en Streamlit,
2. diseñar la landing page,
3. exportar el MER desde MySQL Workbench,
4. completar la narrativa final de entrega,
5. revisar la coherencia entre modelo relacional, SQL, visualizaciones y documentación.
