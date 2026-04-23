from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.inspeccion import obtener_resumen_dataframe, mostrar_resumen_streamlit
from utilidades.ui import apply_global_styles, render_page_header

apply_global_styles()

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    return limpiar_dataframe_penguins(df)

df = cargar_datos()

render_page_header("Inspección del dataset", "Vista general, estructura, tipos de datos, nulos y duplicados.")

c1, c2 = st.columns([1.2, 1])
with c1:
    st.markdown("#### Vista previa")
    st.dataframe(df.head(10), use_container_width=True)
with c2:
    st.markdown("#### Información rápida")
    st.metric("Filas", len(df))
    st.metric("Columnas", df.shape[1])
    st.metric("Duplicados", int(df.duplicated().sum()))

st.markdown("---")
resumen = obtener_resumen_dataframe(df)
mostrar_resumen_streamlit(resumen)
