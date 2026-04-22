import streamlit as st
from app.utils.data_loader import cargar_dataset_penguins
from app.utils.cleaning import limpiar_dataframe_penguins
from app.utils.inspection import inspeccionar_dataframe
from app.utils.plots import plot_dashboard_penguins

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