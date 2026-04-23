from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.graficas import (
    fig_scatter,
    fig_heatmap_correlacion,
    fig_conteo_agrupado,
    fig_boxplot_filtrado,
    fig_multivariado
)
from utilidades.ui import apply_global_styles, render_page_header

apply_global_styles()

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    return limpiar_dataframe_penguins(df)

df = cargar_datos()

render_page_header("Relaciones entre variables", "Análisis bivariado y multivariado con filtros interactivos.")

with st.sidebar:
    st.markdown("## Filtros de página")
    species_opts = sorted(df["species"].dropna().unique().tolist())
    island_opts = sorted(df["island"].dropna().unique().tolist())
    sex_opts = sorted(df["sex"].dropna().unique().tolist())

    species_sel = st.multiselect("Especie", species_opts, default=species_opts)
    island_sel = st.multiselect("Isla", island_opts, default=island_opts)
    sex_sel = st.multiselect("Sexo", sex_opts, default=sex_opts)

df_filtrado = df[
    df["species"].isin(species_sel) &
    df["island"].isin(island_sel) &
    df["sex"].isin(sex_sel)
].copy()

if df_filtrado.empty:
    st.warning("No hay datos con esos filtros.")
    st.stop()

tipo = st.radio(
    "Selecciona visualización",
    ["Scatterplot", "Heatmap", "Conteo agrupado", "Boxplot filtrado", "Multivariado"],
    horizontal=True
)

if tipo == "Scatterplot":
    c1, c2 = st.columns(2)
    opciones = ['bill_length_mm', 'bill_depth_mm', 'body_mass_g', 'flipper_length_mm']
    with c1:
        x_var = st.selectbox("Eje X", opciones, index=0, key="rel_x")
    with c2:
        y_var = st.selectbox("Eje Y", opciones, index=1, key="rel_y")
    st.pyplot(fig_scatter(df_filtrado, x=x_var, y=y_var, hue="species"), use_container_width=True)

elif tipo == "Heatmap":
    st.dataframe(df_filtrado.select_dtypes(include="number").corr(), use_container_width=True)
    st.pyplot(fig_heatmap_correlacion(df_filtrado), use_container_width=True)

elif tipo == "Conteo agrupado":
    st.pyplot(fig_conteo_agrupado(df_filtrado), use_container_width=True)

elif tipo == "Boxplot filtrado":
    c1, c2 = st.columns(2)
    with c1:
        especie = st.selectbox("Especie", sorted(df_filtrado["species"].unique().tolist()), key="rel_especie")
    with c2:
        variable = st.selectbox("Variable", ['bill_length_mm', 'bill_depth_mm', 'body_mass_g', 'flipper_length_mm'], key="rel_var")
    st.pyplot(fig_boxplot_filtrado(df_filtrado, especie=especie, variable=variable, grupo="island"), use_container_width=True)

elif tipo == "Multivariado":
    x_var = st.selectbox("Variable eje X", ['body_mass_g', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm'], index=0, key="rel_multi_x")
    st.pyplot(
        fig_multivariado(
            df_filtrado,
            x_var=x_var,
            y_vars=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm'],
            y_labels=['Longitud del pico [mm]', 'Altura del pico [mm]', 'Longitud de la aleta [mm]'],
            hue='species'
        ),
        use_container_width=True
    )
