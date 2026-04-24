from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.graficas import fig_barras_categorica
from utilidades.ui import apply_arctic_theme, render_page_header, open_card, close_card, render_story, render_sidebar_branding
from utilidades.content import load_markdown
from utilidades.nombres import COLUMNAS_BONITAS

apply_arctic_theme()

@st.cache_data
def cargar_datos():
    return limpiar_dataframe_penguins(cargar_dataset_penguins())

df = cargar_datos()

render_page_header("Variables categóricas", "Frecuencias, proporciones y distribución visual.")

variable = st.selectbox("Selecciona una variable categórica", df.select_dtypes(include="object").columns.tolist(), format_func=lambda x: COLUMNAS_BONITAS.get(x, x))

frecuencias = df[variable].value_counts()
proporciones = df[variable].value_counts(normalize=True).round(4)

c1, c2 = st.columns(2)
with c1:
    open_card()
    st.write("#### Frecuencias")
    st.dataframe(frecuencias.to_frame("frecuencia"), use_container_width=True)
    close_card()
with c2:
    open_card()
    st.write("#### Proporciones")
    st.dataframe(proporciones.to_frame("proporción"), use_container_width=True)
    close_card()

open_card()
st.write("#### Distribución")
st.pyplot(fig_barras_categorica(df, variable), use_container_width=True)
close_card()

render_story(load_markdown("03_categoricas.md"))
render_sidebar_branding("3_Variables_categoricas")