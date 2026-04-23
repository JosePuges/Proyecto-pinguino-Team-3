from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.graficas import fig_dashboard_resumen
from utilidades.ui import apply_global_styles, render_page_header

apply_global_styles()

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    return limpiar_dataframe_penguins(df)

df = cargar_datos()

render_page_header("Dashboard final", "Vista resumen con las visualizaciones más importantes del proyecto.")
fig = fig_dashboard_resumen(df)
st.pyplot(fig, use_container_width=True)
st.caption("Esta página está pensada para demo, presentación y portfolio.")
