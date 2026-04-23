from io import StringIO
import streamlit as st

def obtener_resumen_dataframe(df):
    buffer = StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()

    return {
        "dimensiones": df.shape,
        "info": info_str,
        "dtypes": df.dtypes.astype(str),
        "nulos": df.isna().sum().astype(int),
        "duplicados": int(df.duplicated().sum()),
    }

def mostrar_resumen_streamlit(resumen):
    st.write(f"**Dimensiones:** {resumen['dimensiones']}")
    st.text(resumen["info"])

    c1, c2 = st.columns(2)
    with c1:
        st.write("**Tipos de datos**")
        st.dataframe(resumen["dtypes"].to_frame(name="tipo"), use_container_width=True)
    with c2:
        st.write("**Nulos por columna**")
        st.dataframe(resumen["nulos"].to_frame(name="nulos"), use_container_width=True)

    st.write(f"**Duplicados:** {resumen['duplicados']}")
