from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.graficas import fig_barras_categorica
from utilidades.ui import apply_global_styles, render_page_header

apply_global_styles()

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    return limpiar_dataframe_penguins(df)

df = cargar_datos()

render_page_header("Variables categóricas", "Frecuencias, proporciones y distribución por categorías.")

variables_categoricas = df.select_dtypes(include="object").columns.tolist()
variable = st.selectbox("Selecciona una variable categórica", variables_categoricas)

frecuencias = df[variable].value_counts()
proporciones = df[variable].value_counts(normalize=True).round(4)

c1, c2 = st.columns(2)
with c1:
    st.markdown("#### Frecuencias")
    st.dataframe(frecuencias.to_frame("frecuencia"), use_container_width=True)
with c2:
    st.markdown("#### Proporciones")
    st.dataframe(proporciones.to_frame("proporción"), use_container_width=True)

st.markdown("#### Gráfico de barras")
st.pyplot(fig_barras_categorica(df, variable), use_container_width=True)
