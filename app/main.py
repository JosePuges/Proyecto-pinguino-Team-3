import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.ui import apply_global_styles, render_hero, render_metric_cards

st.set_page_config(
    page_title="Penguins Analytics",
    page_icon="🐧",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_global_styles()

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    return limpiar_dataframe_penguins(df)

df = cargar_datos()

render_hero(
    title="Proyecto Palmer Penguins",
    subtitle="Dashboard interactivo en Streamlit con navegación por páginas, filtros y visualizaciones listas para portfolio."
)

st.sidebar.markdown("## Estado del proyecto")
st.sidebar.success("Estructura multipágina activa")
st.sidebar.caption("Navega por el menú lateral para abrir cada sección.")

render_metric_cards([
    ("Pingüinos", len(df)),
    ("Especies", df["species"].nunique()),
    ("Islas", df["island"].nunique()),
    ("Sexos", df["sex"].nunique()),
])

st.markdown("### Qué incluye")
c1, c2 = st.columns(2)
with c1:
    st.markdown("""
- Inspección del dataset  
- Limpieza aplicada automáticamente  
- Análisis de variables numéricas  
- Análisis de variables categóricas  
""")
with c2:
    st.markdown("""
- Scatterplots y correlaciones  
- Conteos agrupados  
- Boxplots filtrados  
- Dashboard final  
""")

st.info("Abre las páginas desde la barra lateral: Inspección, Numéricas, Categóricas, Relaciones y Dashboard final.")
