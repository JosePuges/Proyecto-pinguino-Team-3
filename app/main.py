import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.ui import apply_arctic_theme, render_hero, open_card, close_card, render_story
from utilidades.content import load_markdown

st.set_page_config(
    page_title="Penguin Analytics Pro",
    page_icon="🐧",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_arctic_theme()

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    return limpiar_dataframe_penguins(df)

df = cargar_datos()

render_hero(
    "Penguin Analytics Pro",
    "Dashboard multipágina con una identidad visual inspirada en la Antártida: limpio, profesional y construido en distintos tonos de azul sobre fondo blanco."
)

render_story(load_markdown("00_home.md"))

c1, c2, c3, c4 = st.columns(4)
c1.metric("Pingüinos", len(df))
c2.metric("Especies", df["species"].nunique())
c3.metric("Islas", df["island"].nunique())
c4.metric("Sexos", df["sex"].nunique())

open_card()
st.markdown("### Navegación")
st.markdown("""
Usa el menú lateral para ir a:
- **Inspección**
- **Variables numéricas**
- **Variables categóricas**
- **Relaciones**
- **Dashboard final**
""")
close_card()
