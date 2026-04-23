from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.graficas import fig_dashboard_resumen
from utilidades.ui import apply_arctic_theme, render_page_header, open_card, close_card, render_story
from utilidades.content import load_markdown

apply_arctic_theme()

@st.cache_data
def cargar_datos():
    return limpiar_dataframe_penguins(cargar_dataset_penguins())

df = cargar_datos()

render_page_header("Dashboard final", "Resumen ejecutivo con las visualizaciones principales del proyecto.")

open_card()
st.pyplot(fig_dashboard_resumen(df), use_container_width=True)
st.caption("Diseño inspirado en una paleta antártica: blanco, azules profundos, azules oceánicos y tonos hielo.")
close_card()

render_story(load_markdown("05_dashboard.md"))