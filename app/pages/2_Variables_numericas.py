from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.graficas import fig_histograma_kde, fig_boxplot
from utilidades.ui import apply_global_styles, render_page_header

apply_global_styles()

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    return limpiar_dataframe_penguins(df)

df = cargar_datos()

render_page_header("Variables numéricas", "Distribuciones, estadísticos descriptivos, asimetría y boxplots.")

variables_numericas = ['bill_length_mm', 'bill_depth_mm', 'body_mass_g', 'flipper_length_mm']
variable = st.selectbox("Selecciona una variable numérica", variables_numericas)

c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown("#### Estadísticos")
    st.dataframe(df[variable].describe().to_frame("valor"), use_container_width=True)
    st.info(f"Asimetría (skew): {df[variable].skew():.4f}")
with c2:
    st.markdown("#### Histograma")
    st.pyplot(fig_histograma_kde(df, variable), use_container_width=True)

st.markdown("#### Boxplot")
st.pyplot(fig_boxplot(df, variable), use_container_width=True)
