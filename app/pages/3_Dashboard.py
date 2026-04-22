import streamlit as st

from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.graficas import plot_dashboard_penguins

st.set_page_config(page_title="Dashboard", layout="wide")
st.title("Dashboard general")

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    df_limpio = limpiar_dataframe_penguins(df, mode="none")
    return df_limpio


df_limpio = cargar_datos()

st.write("Resumen visual del análisis exploratorio del dataset.")
plot_dashboard_penguins(df_limpio, mode="streamlit")
