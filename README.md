**Proyecto Mesas de Ayuda**  

Proyecto de base de datos relacional y dashboard analítico construido a partir de un dataset abierto de **Mesas de Ayuda**, desarrollado mediante un flujo de limpieza en Python, modelado relacional en MySQL, consultas SQL, visualización en Streamlit y documentación final en GitHub.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OQQmAABRAsSeYxZy/lHd7GMACBrCCNxG2BFtmZquOAAD4i3Ot7mr/egIAwGvXA7GTBde8bLBeAAAAAElFTkSuQmCC)  
**1. Descripción general**  
El objetivo de este proyecto fue transformar un archivo CSV de origen abierto en una solución estructurada de análisis de datos compuesta por:  
- preparación y transformación de datos en Python/pandas,  
- modelo entidad-relación (MER),  
- modelo relacional implementado en MySQL,  
- scripts SQL de creación, carga y consulta,  
- dashboard interactivo en Streamlit,  
- landing page de presentación,  
- documentación final publicada en GitHub.  
El proyecto integra varias capas de trabajo: preparación del dato, modelado, validación analítica, visualización y presentación final.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAM0lEQVR4nO3OMQ0AIAwAwdIgBKl1gjacsGCAiZDcTT9+q6oRETMAAPjF6ify6QYAADdyA9Y0AypN+bdfAAAAAElFTkSuQmCC)  
**2. Contexto del dataset**  
El dataset trabajado corresponde a registros de **Mesas de Ayuda** obtenidos desde una fuente abierta en formato CSV.  
Una aclaración fundamental del proyecto es que el archivo original **no contiene tickets individuales**, sino  **registros agregados por tipo de solicitud**.  
   
Cada fila resume métricas como:  
- casos abiertos,  
- casos resueltos,  
- casos atrasados,  
- casos cerrados,  
- tiempo promedio de solución.  
Por esta razón, el archivo original no se importó directamente “tal cual” a MySQL.  
   
Primero fue necesario realizar un proceso de comprensión, limpieza y transformación en Python/pandas para reorganizar la información y convertirla en una estructura adecuada para un modelo relacional y una capa de visualización posterior.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OMQ2AABAAsSNBACMC0cD8NpGACyywEZJWQZeZ2aszAAD+4l6rrTq+ngAA8Nr1AL+yBEpU09MiAAAAAElFTkSuQmCC)  
**3. Flujo general del proyecto**  
El flujo de trabajo desarrollado fue el siguiente:  
1. Carga del CSV original en Python.  
2. Exploración inicial del dataset.  
3. Limpieza y renombrado de columnas.  
4. Transformación de la variable tipo_solicitud.  
5. Conversión de tiempo_promedio a tiempo_promedio_segundos.  
6. Construcción de tablas derivadas para el modelo relacional.  
7. Exportación de archivos CSV procesados.  
8. Implementación de la base de datos en MySQL.  
9. Definición de claves primarias y clave foránea.  
10. Validación mediante consultas SQL.  
11. Construcción de un dashboard en Streamlit.  
12. Organización de la entrega final en GitHub, incluyendo README, MER y landing page.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OMQ2AABAAsSNBCUrfDqrYGVDAgAU2QtIq6DIzW7UHAMBfHGt1V+fXEwAAXrseHCQGBEuErVgAAAAASUVORK5CYII=)  
**4. Preparación de datos**  
Durante la fase de transformación se realizaron las siguientes operaciones principales:  
- estandarización de nombres de columnas,  
- revisión de estructura y tipos de datos,  
- separación de la columna tipo_solicitud en:  
- tipo_principal,  
- subtipo,  
- tipo_completo,  
- conversión del tiempo promedio a una métrica numérica homogénea en segundos,  
- construcción de dos tablas derivadas que alimentan el modelo relacional:  
- dim_tipo_solicitud,  
- fact_mesas_ayuda.  
Los archivos procesados generados al final de esta fase fueron:  
- mesas_ayuda_limpio.csv  
- dim_tipo_solicitud.csv  
- fact_mesas_ayuda.csv  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OMQ2AABAAsSNBACPiUML0NpGACyywEZJWQZeZ2aszAAD+4l6rrTq+ngAA8Nr1AL/SBEZwuCSwAAAAAElFTkSuQmCC)  
**5. Modelo de datos**  
La base de datos implementada en MySQL es **relacional** y se definió con el nombre:  
proyecto_mesas_ayuda  
**Tablas principales**  
*dim_tipo_solicitud*  
Tabla dimensional que almacena la clasificación de los tipos de solicitud.  
Campos principales:  
- tipo_id (PK)  
- tipo_principal  
- subtipo  
- tipo_completo  
*fact_mesas_ayuda*  
Tabla de hechos que contiene las métricas agregadas del dataset.  
Campos principales:  
- registro_id (PK)  
- anio  
- tipo_id (FK)  
- casos_abiertos  
- casos_resueltos  
- casos_atrasados  
- casos_cerrados  
- tiempo_promedio_segundos  
**Relación principal**  
- dim_tipo_solicitud (1) -> (N) fact_mesas_ayuda  
El diagrama exportado del modelo se encuentra en:  
- docs/mer_modelo_relacional.png  
y el archivo editable de Workbench en:  
- docs/proyecto_mesas_ayuda.mwb  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OMQ2AABAAsSNhZ0YbTpjeJg6QgQU2QtIq6DIze3UGAMBf3Gu1VcfXEwAAXrsethQERN6FFS4AAAAASUVORK5CYII=)  
**6. Validaciones realizadas**  
Después de la carga en MySQL se verificó la consistencia de la información con los siguientes resultados:  
- filas en dim_tipo_solicitud: **63**  
- filas en fact_mesas_ayuda: **63**  
- total casos abiertos: **2109**  
- total casos resueltos: **2106**  
- total casos atrasados: **0**  
- total casos cerrados: **2106**  
Estas validaciones confirmaron que la carga quedó coherente con los archivos procesados y con el flujo de transformación realizado en Python.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OMQ2AABAAsSPBCUZfEnoYmFDBhAU2QtIq6DIzW7UHAMBfnGt1V8fXEwAAXrse/wcF74lXkIsAAAAASUVORK5CYII=)  
**7. Hallazgos principales**  
Entre los hallazgos más importantes del proyecto se encuentran:  
- La categoría con mayor carga de casos es **Acceso**.  
- El tipo completo con mayor número de casos es **Acceso > SICAU**.  
- Se identificó una anomalía reportable en **Acompañamiento**, con una tasa de resolución superior al 100%.  
- También se observaron pequeñas diferencias entre casos abiertos y cerrados en categorías como **Software** y  **Redes**.  
Estos hallazgos se reflejan tanto en las consultas SQL como en el dashboard de visualización.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANElEQVR4nO3OQQmAUBBAwSf8GGLWDWFDY3ixgjcRZhLMNjNHdQYAwF9cq1rV/vUEAIDX7gcRXAQ2s/16gwAAAABJRU5ErkJggg==)  
**8. Dashboard en Streamlit**  
Como capa de visualización se construyó un dashboard analítico en Streamlit que permite:  
- explorar los datos por tipo principal,  
- visualizar indicadores clave (KPIs),  
- revisar distribución de casos abiertos por categoría,  
- consultar los tipos de solicitud con mayor carga,  
- analizar tiempos promedio de solución,  
- identificar anomalías y diferencias entre métricas.  
El archivo principal del dashboard se encuentra en:  
- app/streamlit_app.py  
El dashboard fue probado tanto en entorno de desarrollo como en ejecución local desde el repositorio.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OQQmAABRAsScYxpg/i2XMYARvRrCCNxG2BFtmZquOAAD4i3Ot7mr/egIAwGvXA22YBcnkstSpAAAAAElFTkSuQmCC)  
**9. Landing page**  
Como parte de la presentación final del proyecto se construyó una landing page estática que resume:  
- el propósito del proyecto,  
- el flujo general de trabajo,  
- el MER,  
- los hallazgos principales,  
- las tecnologías utilizadas,  
- los archivos más importantes del repositorio.  
La landing page se encuentra en:  
- landing/index.html  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OMQ2AABAAsSNBCUpfDq4wwIAABiywEZJWQZeZ2ao9AAD+4liruzq/ngAA8Nr1ABweBgdur/QFAAAAAElFTkSuQmCC)  
**10. Estructura del repositorio**  
proyecto_mesas_ayuda/  
 ├── app/  
 │   └── streamlit_app.py  
 ├── assets/  
 │   └── img/  
 ├── data/  
 │   ├── raw/  
 │   │   └── Mesas_de_ayuda.csv  
 │   └── processed/  
 │       ├── mesas_ayuda_limpio.csv  
 │       ├── dim_tipo_solicitud.csv  
 │       └── fact_mesas_ayuda.csv  
 ├── docs/  
 │   ├── proceso_proyecto_mesas_ayuda.pdf  
 │   ├── mer_modelo_relacional.png  
 │   └── proyecto_mesas_ayuda.mwb  
 ├── landing/  
 │   └── index.html  
 ├── notebooks/  
 │   ├── primera_entrega.ipynb  
 │   └── dashboard_mesas_ayuda_colab.ipynb  
 ├── sql/  
 │   ├── 01_modelo_y_carga.sql  
 │   └── 02_consultas_analiticas.sql  
 ├── .gitignore  
 ├── README.md  
 └── requirements.txt  
   
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OQQmAABRAsSfYxZo/jVEMYQLPJrCCNxG2BFtmZquOAAD4i3Ot7mr/egIAwGvXA4rLBc059ysnAAAAAElFTkSuQmCC)  
**11. Archivos principales**  
**Datos**  
- data/raw/Mesas_de_ayuda.csv  
- data/processed/mesas_ayuda_limpio.csv  
- data/processed/dim_tipo_solicitud.csv  
- data/processed/fact_mesas_ayuda.csv  
**SQL**  
- sql/01_modelo_y_carga.sql  
- sql/02_consultas_analiticas.sql  
**Notebook**  
- notebooks/base_datos.ipynb  
- notebooks/dashboard_mesas_ayuda_colab.ipynb  
**App y presentación**  
- app/streamlit_app.py  
- landing/index.html  
**Documentación**  
- docs/proceso_proyecto_mesas_ayuda.pdf  
- docs/mer_modelo_relacional.png  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OQQmAABRAsSd4EKxgBjP+Asa0hxW8ibAl2DIzR3UFAMBf3Gu1VefXEwAAXtsfSqwDVbgKngwAAAAASUVORK5CYII=)  
**12. Tecnologías utilizadas**  
- Python  
- pandas  
- MySQL  
- MySQL Workbench  
- Streamlit  
- Git  
- GitHub  
- Google Colab  
- VS Code  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OQQmAABRAsScYxpg/i2XMYARvRrCCNxG2BFtmZquOAAD4i3Ot7mr/egIAwGvXA22YBcnkstSpAAAAAElFTkSuQmCC)  
**13. Entorno de trabajo recomendado**  
Para la entrega final se recomienda trabajar principalmente en **Windows**, ya que es el entorno sugerido en el curso.  
Durante el desarrollo también se utilizó **Ubuntu** como entorno alterno para:  
- ejecución local de Git y GitHub,  
- pruebas del dashboard en Streamlit,  
- organización de archivos del repositorio.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OMQ2AABAAsSPBCUZfEnoYmFDBhAU2QtIq6DIzW7UHAMBfnGt1V8fXEwAAXrse/wcF74lXkIsAAAAASUVORK5CYII=)  
**14. Cómo ejecutar el proyecto**  
**A. Scripts SQL**  
1. Crear la base de datos proyecto_mesas_ayuda en MySQL.  
2. Ejecutar el archivo sql/01_modelo_y_carga.sql.  
3. Ejecutar el archivo sql/02_consultas_analiticas.sql.  
**B. Notebook principal**  
Abrir notebooks/base_datos.ipynb para revisar la fase de preparación y exportación de datos.  
**C. Dashboard en Streamlit**  
1. Crear y activar un entorno virtual de Python.  
2. Instalar dependencias con:  
python -m pip install -r requirements.txt  
   
1. Ejecutar la aplicación:  
python -m streamlit run app/streamlit_app.py  
   
**D. Landing page**  
Abrir landing/index.html en el navegador o servir el proyecto localmente con un servidor HTTP simple.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OMQ2AABAAsSNBACMC0cD8NpGACyywEZJWQZeZ2aszAAD+4l6rrTq+ngAA8Nr1AL+yBEpU09MiAAAAAElFTkSuQmCC)  
**15. Estado actual del proyecto**  
Actualmente el proyecto cuenta con:  
- preparación y transformación de datos,  
- archivos CSV procesados,  
- modelo relacional implementado en MySQL,  
- validaciones y consultas SQL,  
- MER exportado desde MySQL Workbench,  
- dashboard funcional en Streamlit,  
- landing page de presentación,  
- documentación y organización final en GitHub.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OMQ2AABAAsSNBCkJfE1pYGfHAiAU2QtIq6DIzW7UHAMBfnGt1V8fXEwAAXrse4dwF6o2O55YAAAAASUVORK5CYII=)  
**16. Observaciones finales**  
Este proyecto muestra un flujo completo de trabajo desde un archivo plano de datos hasta una solución organizada de base de datos y visualización.  
Aunque el dataset original no fue diseñado como una base relacional, el proceso de limpieza y modelado permitió convertirlo en una estructura coherente, analizable y presentable como entrega académica final.  
