from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.inspeccion import obtener_resumen_dataframe, mostrar_resumen_streamlit
from utilidades.ui import apply_arctic_theme, render_page_header, open_card, close_card, render_story
from utilidades.content import load_markdown

apply_arctic_theme()

@st.cache_data
def cargar_datos():
    return limpiar_dataframe_penguins(cargar_dataset_penguins())

df = cargar_datos()

render_page_header("Inspección del dataset", "Estructura, esquema y estado del dataset limpio.")
render_story(load_markdown("01_inspeccion.md"))

open_card()
st.dataframe(df.head(12), use_container_width=True)
close_card()

open_card()
mostrar_resumen_streamlit(obtener_resumen_dataframe(df))
close_card()
