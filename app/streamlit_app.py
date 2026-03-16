import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Dashboard Mesas de Ayuda",
    layout="wide"
)

@st.cache_data
def cargar_datos():
    base_dir = Path("/content")

    dim_path = base_dir / "dim_tipo_solicitud.csv"
    fact_path = base_dir / "fact_mesas_ayuda.csv"

    dim_tipo = pd.read_csv(dim_path)
    fact_mesas_ayuda = pd.read_csv(fact_path)

    df = fact_mesas_ayuda.merge(dim_tipo, on="tipo_id", how="left")
    return df, dim_tipo, fact_mesas_ayuda

def formatear_segundos(segundos):
    if pd.isna(segundos):
        return "N/A"

    segundos = int(round(segundos))
    dias = segundos // 86400
    resto = segundos % 86400
    horas = resto // 3600
    resto = resto % 3600
    minutos = resto // 60
    seg = resto % 60

    partes = []
    if dias > 0:
        partes.append(f"{dias}d")
    if horas > 0:
        partes.append(f"{horas}h")
    if minutos > 0:
        partes.append(f"{minutos}m")
    if seg > 0 or not partes:
        partes.append(f"{seg}s")

    return " ".join(partes)

df, dim_tipo, fact_mesas_ayuda = cargar_datos()

st.title("Dashboard de Mesas de Ayuda")
st.markdown(
    """
    Visualización analítica construida a partir de registros agregados de mesas de ayuda.
    Cada fila representa una categoría de solicitud con métricas como casos abiertos,
    resueltos, cerrados y tiempo promedio de solución.
    """
)

st.sidebar.header("Filtros")

tipos_principales = ["Todos"] + sorted(df["tipo_principal"].dropna().unique().tolist())
tipo_seleccionado = st.sidebar.selectbox("Tipo principal", tipos_principales)

# Si no existe la columna anio, no rompemos la app
if "anio" in df.columns:
    anios = sorted(df["anio"].dropna().unique().tolist())
    anios_seleccionados = st.sidebar.multiselect(
        "Año",
        options=anios,
        default=anios
    )
else:
    anios = []
    anios_seleccionados = []

df_filtrado = df.copy()

if tipo_seleccionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo_principal"] == tipo_seleccionado]

if "anio" in df_filtrado.columns and anios:
    if anios_seleccionados:
        df_filtrado = df_filtrado[df_filtrado["anio"].isin(anios_seleccionados)]
    else:
        df_filtrado = df_filtrado.iloc[0:0]

total_abiertos = int(df_filtrado["casos_abiertos"].sum())
total_resueltos = int(df_filtrado["casos_resueltos"].sum())
total_cerrados = int(df_filtrado["casos_cerrados"].sum())
promedio_tiempo = float(df_filtrado["tiempo_promedio_segundos"].mean()) if not df_filtrado.empty else 0
tasa_resolucion = round((total_resueltos / total_abiertos) * 100, 2) if total_abiertos > 0 else 0

st.subheader("Resumen general")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Casos abiertos", f"{total_abiertos:,}")
col2.metric("Casos resueltos", f"{total_resueltos:,}")
col3.metric("Casos cerrados", f"{total_cerrados:,}")
col4.metric("Tasa de resolución", f"{tasa_resolucion}%")

col5, col6 = st.columns(2)
col5.metric("Tiempo promedio", formatear_segundos(promedio_tiempo))
col6.metric("Registros analizados", len(df_filtrado))

st.subheader("Casos abiertos por tipo principal")
resumen_tipo_principal = (
    df_filtrado.groupby("tipo_principal", as_index=False)["casos_abiertos"]
    .sum()
    .sort_values("casos_abiertos", ascending=False)
)

if resumen_tipo_principal.empty:
    st.warning("No hay datos para los filtros seleccionados.")
else:
    st.dataframe(resumen_tipo_principal, use_container_width=True)
    st.bar_chart(
        resumen_tipo_principal.set_index("tipo_principal")["casos_abiertos"],
        use_container_width=True
    )

st.subheader("Top 10 tipos de solicitud con más casos abiertos")
top_tipos = (
    df_filtrado.groupby("tipo_completo", as_index=False)["casos_abiertos"]
    .sum()
    .sort_values("casos_abiertos", ascending=False)
    .head(10)
)

if not top_tipos.empty:
    st.dataframe(top_tipos, use_container_width=True)
    st.bar_chart(
        top_tipos.set_index("tipo_completo")["casos_abiertos"],
        use_container_width=True
    )

st.subheader("Top 10 tipos con mayor tiempo promedio de solución")
top_tiempos = (
    df_filtrado.groupby("tipo_completo", as_index=False)["tiempo_promedio_segundos"]
    .mean()
    .sort_values("tiempo_promedio_segundos", ascending=False)
    .head(10)
)

if not top_tiempos.empty:
    top_tiempos["tiempo_promedio_legible"] = top_tiempos["tiempo_promedio_segundos"].apply(formatear_segundos)
    st.dataframe(
        top_tiempos[["tipo_completo", "tiempo_promedio_segundos", "tiempo_promedio_legible"]],
        use_container_width=True
    )
    st.bar_chart(
        top_tiempos.set_index("tipo_completo")["tiempo_promedio_segundos"],
        use_container_width=True
    )

st.subheader("Observaciones analíticas")
observaciones = (
    df_filtrado.groupby("tipo_completo", as_index=False)
    .agg(
        casos_abiertos=("casos_abiertos", "sum"),
        casos_resueltos=("casos_resueltos", "sum"),
        casos_cerrados=("casos_cerrados", "sum")
    )
)

if not observaciones.empty:
    observaciones["tasa_resolucion_pct"] = (
        observaciones["casos_resueltos"] / observaciones["casos_abiertos"] * 100
    ).round(2)

    observaciones["diferencia_abiertos_cerrados"] = (
        observaciones["casos_abiertos"] - observaciones["casos_cerrados"]
    )

    anomalias = observaciones[
        (observaciones["tasa_resolucion_pct"] > 100) |
        (observaciones["diferencia_abiertos_cerrados"] != 0)
    ].sort_values(
        by=["tasa_resolucion_pct", "diferencia_abiertos_cerrados"],
        ascending=[False, False]
    )

    if anomalias.empty:
        st.info("No se detectaron anomalías con los filtros actuales.")
    else:
        st.dataframe(anomalias, use_container_width=True)

st.subheader("Tabla detallada")

columnas_base = [
    "tipo_principal",
    "subtipo",
    "tipo_completo",
    "casos_abiertos",
    "casos_resueltos",
    "casos_atrasados",
    "casos_cerrados",
    "tiempo_promedio_segundos",
]

columnas_tabla = [c for c in ["anio"] + columnas_base if c in df_filtrado.columns]

st.dataframe(
    df_filtrado[columnas_tabla].sort_values(
        by=["casos_abiertos", "tiempo_promedio_segundos"],
        ascending=[False, False]
    ),
    use_container_width=True
)

st.success("Dashboard cargado correctamente.")
