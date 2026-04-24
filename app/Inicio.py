import streamlit as st
from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.ui import apply_arctic_theme, render_hero, open_card, close_card, render_page_header, render_story
from utilidades.content import load_markdown
from utilidades.ui import apply_arctic_theme, render_sidebar_branding

st.set_page_config(
    page_title="Penguin Analytics Pro",
    page_icon="🐧",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_arctic_theme()
render_sidebar_branding()

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

st.divider()

st.subheader("🐧 Pregúntale al pingüino analista")

if "mensajes_pinguino" not in st.session_state:
    st.session_state.mensajes_pinguino = [
        {
            "role": "assistant",
            "content": "¡Hola! Soy PinguBot 🐧 Pregúntame sobre especies, islas, sexo o tamaño del dataset."
        }
    ]

for mensaje in st.session_state.mensajes_pinguino:
    avatar = "🐧" if mensaje["role"] == "assistant" else "🧑"
    with st.chat_message(mensaje["role"], avatar=avatar):
        st.write(mensaje["content"])

pregunta = st.chat_input("Pregunta algo sobre los pingüinos...")

if pregunta:
    st.session_state.mensajes_pinguino.append(
        {"role": "user", "content": pregunta}
    )

    pregunta_lower = pregunta.lower()

    if "cuántos" in pregunta_lower or "cuantos" in pregunta_lower:
        respuesta = f"Tenemos {len(df)} pingüinos en el dataset 🐧"

    elif "especies" in pregunta_lower:
        especies = ", ".join(df["species"].dropna().unique())
        respuesta = f"Las especies del dataset son: {especies}."

    elif "islas" in pregunta_lower or "isla" in pregunta_lower:
        islas = ", ".join(df["island"].dropna().unique())
        respuesta = f"Los pingüinos aparecen en estas islas: {islas}."

    elif "sexo" in pregunta_lower or "sexos" in pregunta_lower:
        sexos = ", ".join(df["sex"].dropna().unique())
        respuesta = f"En la columna sexo aparecen estos valores: {sexos}."

    elif "media" in pregunta_lower or "promedio" in pregunta_lower:
        respuesta = "Puedo calcular medias, pero dime de qué columna: peso, aleta, pico, etc. 🧊"

    else:
        respuesta = "Mmm... no estoy seguro, pero puedes preguntarme por especies, islas, sexos o número de pingüinos 🐧"

    st.session_state.mensajes_pinguino.append(
        {"role": "assistant", "content": respuesta}
    )

    st.rerun()