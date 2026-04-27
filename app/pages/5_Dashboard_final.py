from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.graficas import fig_dashboard_resumen
from utilidades.ui import apply_arctic_theme, render_page_header, open_card, close_card, render_story, render_sidebar_branding
from utilidades.content import load_markdown
from utilidades.export import descargar_metricas_csv, descargar_grafico_matplotlib


apply_arctic_theme()

@st.cache_data
def cargar_datos():
    return limpiar_dataframe_penguins(cargar_dataset_penguins())

df = cargar_datos()
render_sidebar_branding("5_Dashboard_final")

render_page_header("Dashboard final", "Resumen ejecutivo con las visualizaciones principales del proyecto.")


open_card()

fig = fig_dashboard_resumen(df)

st.pyplot(fig, use_container_width=True)
st.caption("Diseño inspirado en una paleta antártica: blanco, azules profundos, azules oceánicos y tonos hielo.")

close_card()


open_card()

st.subheader("📥 Exportar resultados")


descargar_grafico_matplotlib(fig, "dashboard_penguins.png")

close_card()

render_story(load_markdown("05_dashboard.md"))