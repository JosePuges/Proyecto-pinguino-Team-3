import streamlit as st

st.set_page_config(page_title="Proyecto Pingüinos", layout="wide")

st.title("Proyecto de análisis de pingüinos")
st.write("Bienvenido a la app de análisis exploratorio del dataset Palmer Penguins.")

st.markdown("""
### Contenido de la app
- **Inspección**: dimensiones, tipos, nulos y duplicados
- **Gráficos**: visualizaciones individuales
- **Dashboard**: vista resumen con varios gráficos

Usa el menú lateral de Streamlit para navegar entre páginas.
""")
