import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.ui import apply_arctic_theme, render_hero, open_card, close_card, render_page_header, render_story
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
    "Del hielo al codigo: Pingüinos, datos y visualizaciones en un solo lugar."

)
def render_page_header(title, subtitle):
    st.markdown(f"## {title}")
    st.markdown(f"### {subtitle}")

render_page_header("Proyecto Pinguino Team 3 - Bootcamp Data Analytics - f5", "Alejandro Posada, Arantxa Puig, Eva Ponton, Jose Pascual, Oksana Tokmakova")
                   
                   

render_story(load_markdown("00_home.md"))

c1, c2, c3, c4 = st.columns(4)
c1.metric("Pingüinos", len(df))
c2.metric("Especies", df["species"].nunique())
c3.metric("Islas", df["island"].nunique())
c4.metric("Sexos", df["sex"].nunique())

