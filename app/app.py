import streamlit as st

from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.icon import inspeccionar_dataframe
from utilidades.graficas import (
    plot_scatter_penguins,
    plot_boxplot_penguins,
    correlacion_heatmap,
    plot_conteo_penguins,
    plot_boxplot_adelie_island,
    plot_multivariado_penguins,
    plot_dashboard_penguins
)



st.set_page_config(page_title="Proyecto Pingüinos", layout="wide")

st.title("Proyecto Pingüinos")
st.write("Bienvenido a la app de análisis de pingüinos.")

st.markdown("""
Usa el menú lateral para navegar por:
- Inspección del dataset
- Análisis univariado
- Análisis bivariado
- Dashboard final
""")


st.title("Proyecto de análisis de pingüinos")
st.write("Aplicación de análisis exploratorio con Streamlit")

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    df_limpio = limpiar_dataframe_penguins(df, mode="none")
    return df, df_limpio

df, df_limpio = cargar_datos()

st.header("1. Vista general del dataset")
inspeccionar_dataframe(df_limpio, mode="streamlit")

st.header("2. Dashboard general")
plot_dashboard_penguins(df_limpio, mode="streamlit")

st.header("3. Análisis específicos")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Scatterplot")
    plot_scatter_penguins(df_limpio, mode="streamlit")

    st.subheader("Boxplot por especie")
    plot_boxplot_penguins(df_limpio, mode="streamlit")

with col2:
    st.subheader("Heatmap de correlación")
    correlacion_heatmap(df_limpio, mode="streamlit")

    st.subheader("Conteo por isla, especie y sexo")
    plot_conteo_penguins(df_limpio, mode="streamlit")

st.header("4. Análisis filtrado")
plot_boxplot_adelie_island(df_limpio, mode="streamlit")

st.header("5. Análisis multivariado")
plot_multivariado_penguins(df_limpio, mode="streamlit")