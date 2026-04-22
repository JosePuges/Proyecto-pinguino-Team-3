import streamlit as st
from app.utilidades.carga_datos import cargar_dataset_penguins
from app.utilidades.limpieza import limpiar_dataframe_penguins
from app.utilidades.icon import inspeccionar_dataframe

st.title("Inspección del dataset")

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    return limpiar_dataframe_penguins(df, mode="none")

df_limpio = cargar_datos()

inspeccionar_dataframe(df_limpio, mode="streamlit")