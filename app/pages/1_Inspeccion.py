import streamlit as st

from app.utilidades.carga_datos import cargar_dataset_penguins
from app.utilidades.limpieza import limpiar_dataframe_penguins
from app.utilidades.inspeccion import inspeccionar_dataframe

st.set_page_config(page_title="Inspección", layout="wide")
st.title("Inspección del dataset")

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    df_limpio = limpiar_dataframe_penguins(df, mode="none")
    return df, df_limpio


df, df_limpio = cargar_datos()

st.subheader("Vista previa del dataset limpio")
st.dataframe(df_limpio.head())

st.subheader("Información general")
inspeccionar_dataframe(df_limpio, mode="streamlit")
