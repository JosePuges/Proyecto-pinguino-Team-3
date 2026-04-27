from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.graficas import fig_histograma_kde, fig_boxplot
from utilidades.ui import apply_arctic_theme, render_page_header, open_card, close_card, render_story,render_sidebar_branding
from utilidades.content import load_markdown
from utilidades.nombres import COLUMNAS_BONITAS
from utilidades.export import  exportar_estadisticos, descargar_grafico_matplotlib

apply_arctic_theme()

@st.cache_data
def cargar_datos():
    return limpiar_dataframe_penguins(cargar_dataset_penguins())

df = cargar_datos()

render_page_header("Variables numéricas", "Estadísticos, asimetría, histogramas y boxplots.")


variables = ['bill_length_mm', 'bill_depth_mm', 'body_mass_g', 'flipper_length_mm']
variable = st.selectbox("Selecciona una variable", variables, format_func=lambda x: COLUMNAS_BONITAS.get(x, x))

c1, c2 = st.columns([1, 1.2])
with c1:
    open_card()
    st.write("#### Estadísticos")
    st.dataframe(df[variable].describe().to_frame("valor"), use_container_width=True)
    st.info(f"Asimetría (skew): {df[variable].skew():.4f}")
    close_card()
with c2:
    open_card()
    st.write("#### Histograma")
    fig_hist = fig_histograma_kde(df, variable)
    st.pyplot(fig_hist, use_container_width=True)
    close_card()

open_card()
st.write("#### Boxplot")
fig_box = fig_boxplot(df, variable)
st.pyplot(fig_box, use_container_width=True)
close_card()

open_card()
st.subheader("📥 Exportar resultados")

# 📊 Estadísticos
exportar_estadisticos(df, variable) 


# 📈 Gráficos
descargar_grafico_matplotlib(
    fig_hist,
    f"histograma_{variable}.png"
)

descargar_grafico_matplotlib(
    fig_box,
    f"boxplot_{variable}.png"
)

close_card()

render_story(load_markdown("02_numericas.md"))

render_sidebar_branding("2_Variables_numericas")