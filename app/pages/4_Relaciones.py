from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import plotly.express as px
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
from utilidades.ui import apply_arctic_theme, render_page_header, open_card, close_card, render_story, render_sidebar_branding
from utilidades.content import load_markdown
from utilidades.nombres import COLUMNAS_BONITAS
from utilidades.export import descargar_grafico_matplotlib, descargar_grafico_plotly


apply_arctic_theme()

@st.cache_data
def cargar_datos():
    return limpiar_dataframe_penguins(cargar_dataset_penguins())

df = cargar_datos()
render_page_header("Relaciones entre variables", "Explora relaciones bivariadas y multivariadas con filtros.")
render_sidebar_branding("4_Relaciones")


st.sidebar.markdown("## Filtros")
species_opts = sorted(df["species"].dropna().unique().tolist())
island_opts = sorted(df["island"].dropna().unique().tolist())
sex_opts = sorted(df["sex"].dropna().unique().tolist())

species_sel = st.sidebar.multiselect("Especie", species_opts, default=species_opts)
island_sel = st.sidebar.multiselect("Isla", island_opts, default=island_opts)
sex_sel = st.sidebar.multiselect("Sexo", sex_opts, default=sex_opts)

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

opciones_columnas = ['bill_length_mm', 'bill_depth_mm', 'body_mass_g', 'flipper_length_mm']

open_card()

fig = None

if tipo == "Scatterplot":
    c1, c2 = st.columns(2)
    with c1:
        x_var = st.selectbox(
            "Eje X",
            opciones_columnas,
            index=0,
            format_func=lambda x: COLUMNAS_BONITAS.get(x, x),
            key="scatter_x"
        )
    with c2:
        y_var = st.selectbox(
            "Eje Y",
            opciones_columnas,
            index=1,
            format_func=lambda x: COLUMNAS_BONITAS.get(x, x),
            key="scatter_y"
        )

    fig = fig_scatter(df_filtrado, x=x_var, y=y_var, hue="species")

    st.plotly_chart(fig, use_container_width=True)

    

elif tipo == "Heatmap":
    fig = fig_heatmap_correlacion(df_filtrado)
    st.pyplot(fig, use_container_width=True)

    with st.expander("Ver matriz de correlación"):
        st.dataframe(
            df_filtrado.select_dtypes(include="number")
            .drop(columns=["year"], errors="ignore")
            .corr(),
            use_container_width=True
        )

elif tipo == "Conteo agrupado":
    fig = fig_conteo_agrupado(df_filtrado)
    st.pyplot(fig, use_container_width=True)

elif tipo == "Boxplot filtrado":
    c1, c2 = st.columns(2)
    with c1:
        especie = st.selectbox(
            "Especie",
            sorted(df_filtrado["species"].unique().tolist()),
            key="box_especie"
        )
    with c2:
        variable = st.selectbox(
            "Variable",
            opciones_columnas,
            format_func=lambda x: COLUMNAS_BONITAS.get(x, x),
            key="box_variable"
        )

    fig = fig_boxplot_filtrado(df_filtrado, especie=especie, variable=variable, grupo="island")
    st.pyplot(fig, use_container_width=True)
    

elif tipo == "Multivariado":
    x_var = st.selectbox(
        "Variable eje X",
        opciones_columnas,
        index=2,
        format_func=lambda x: COLUMNAS_BONITAS.get(x, x),
        key="multi_x"
    )

    fig = fig_multivariado(
            df_filtrado,
            x_var=x_var,
            y_vars=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm'],
            y_labels=[
                'Longitud del pico [mm]',
                'Altura del pico [mm]',
                'Longitud de la aleta [mm]'
            ],
            hue='species'
        )
        
    st.pyplot(fig, use_container_width=True)

close_card()

open_card()

st.subheader("📥 Exportar datos y gráfico")



# Exportar gráfico según tipo
if fig is not None:
    if tipo == "Scatterplot":
        descargar_grafico_plotly(fig, "scatter_penguins.html")
    else:
        descargar_grafico_matplotlib(fig, f"{tipo.lower()}.png")

close_card()

render_story(load_markdown("04_relaciones.md"))