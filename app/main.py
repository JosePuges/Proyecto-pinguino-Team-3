import streamlit as st
from app.utilidades.carga_datos import cargar_dataset_penguins
from app.utilidades.limpieza import limpiar_dataframe_penguins
from app.utilidades.icon import inspeccionar_dataframe
from app.utilidades.graficas import plot_dashboard_penguins

st.set_page_config(page_title="Proyecto Pingüinos", layout="wide")

st.title("Proyecto Pingüinos")

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    df_limpio = limpiar_dataframe_penguins(df, mode="none")
    return df, df_limpio

df, df_limpio = cargar_datos()

inspeccionar_dataframe(df_limpio, mode="streamlit")
plot_dashboard_penguins(df_limpio, mode="streamlit")