import streamlit as st
import unicodedata


def normalizar(texto):
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto



COLUMNAS = {
    "peso": "body_mass_g",
    "masa": "body_mass_g",
    "aleta": "flipper_length_mm",
    "aletas": "flipper_length_mm",
    "pico": "bill_length_mm",
    "longitud pico": "bill_length_mm",
    "profundidad pico": "bill_depth_mm",
}


def detectar_columna(pregunta):
    for key in COLUMNAS:
        if key in pregunta:
            return COLUMNAS[key]
    return None


def responder_pinguino(pregunta, df):
    pregunta = normalizar(pregunta)

    # TOTAL
    if any(p in pregunta for p in ["cuantos", "total", "numero"]):
        return f"Hay {len(df)} pingüinos en el dataset 🐧"

    # ESPECIES
    if "especie" in pregunta:
        especies = ", ".join(df["species"].dropna().unique())
        return f"Tenemos estas especies: {especies}"

    # ISLAS
    if "isla" in pregunta:
        islas = ", ".join(df["island"].dropna().unique())
        return f"Los pingüinos viven en: {islas}"

    # SEXO
    if "sexo" in pregunta:
        sexos = ", ".join(df["sex"].dropna().unique())
        return f"Valores de sexo: {sexos}"

    # DETECTAR COLUMNA NUMÉRICA
    col = detectar_columna(pregunta)

    if col:
        if any(p in pregunta for p in ["media", "promedio"]):
            return f"La media es {df[col].mean():.2f}"

        if any(p in pregunta for p in ["maximo", "mayor"]):
            return f"El valor máximo es {df[col].max():.2f}"

        if any(p in pregunta for p in ["minimo", "menor"]):
            return f"El valor mínimo es {df[col].min():.2f}"

        if "mediana" in pregunta:
            return f"La mediana es {df[col].median():.2f}"

    # ESPECIE ESPECÍFICA
    for especie in df["species"].dropna().unique():
        if especie.lower() in pregunta:
            total = len(df[df["species"] == especie])
            return f"Hay {total} pingüinos {especie} 🐧"

    # FALLBACK
    return (
        "No estoy seguro 🤔\n\n"
        "Puedes preguntarme cosas como:\n"
        "- ¿Cuántos pingüinos hay?\n"
        "- ¿Media del peso?\n"
        "- ¿Máximo de la aleta?\n"
        "- ¿Qué especies hay?\n"
    )


def render_chatbot_pinguino(df):
    st.subheader("🐧 Pregúntale al pingüino analista")

    if "mensajes_pinguino" not in st.session_state:
        st.session_state.mensajes_pinguino = [
            {
                "role": "assistant",
                "content": "¡Hola! Soy PinguBot 🐧 Pregúntame sobre especies, islas, peso o aletas."
            }
        ]

    # Mostrar historial
    for mensaje in st.session_state.mensajes_pinguino:
        avatar = "🐧" if mensaje["role"] == "assistant" else "🧑"
        with st.chat_message(mensaje["role"], avatar=avatar):
            st.write(mensaje["content"])

    # Input usuario
    pregunta = st.chat_input("Pregunta algo sobre los pingüinos...")

    if pregunta:
        st.session_state.mensajes_pinguino.append(
            {"role": "user", "content": pregunta}
        )

        respuesta = responder_pinguino(pregunta, df)

        st.session_state.mensajes_pinguino.append(
            {"role": "assistant", "content": respuesta}
        )

        st.rerun()