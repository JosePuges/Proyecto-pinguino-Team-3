import streamlit as st

from app.utilidades.carga_datos import cargar_dataset_penguins
from app.utilidades.limpieza import limpiar_dataframe_penguins
from app.utilidades.graficas import (
    plot_scatter_penguins,
    plot_boxplot_penguins,
    correlacion_heatmap,
    plot_conteo_penguins,
    plot_boxplot_adelie_island,
    plot_multivariado_penguins
)

st.title("Gráficos")

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    df_limpio = limpiar_dataframe_penguins(df, mode="none")
    return df_limpio

df_limpio = cargar_datos()

st.subheader("Scatterplot")
plot_scatter_penguins(df_limpio, mode="streamlit")

st.subheader("Boxplot de masa corporal por especie")
plot_boxplot_penguins(df_limpio, mode="streamlit")

st.subheader("Matriz de correlación")
correlacion_heatmap(df_limpio, mode="streamlit", mostrar_tabla=True)

st.subheader("Conteo por isla, especie y sexo")
plot_conteo_penguins(df_limpio, mode="streamlit")

st.subheader("Boxplot de Adelie por isla")
plot_boxplot_adelie_island(df_limpio, mode="streamlit")

st.subheader("Análisis multivariado")
plot_multivariado_penguins(df_limpio, mode="streamlit")