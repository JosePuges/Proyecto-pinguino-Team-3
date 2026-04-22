from io import StringIO

def inspeccionar_dataframe(df, mode="none", devolver_resultados=False):
    buffer = StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()

    resultados = {
        "dimensiones": df.shape,
        "info": info_str,
        "dtypes": df.dtypes,
        "nulos": df.isna().sum(),
        "duplicados": df.duplicated().sum(),
    }

    if mode == "streamlit":
        import streamlit as st
        st.subheader("Información general")
        st.write(f"Dimensiones: {resultados['dimensiones']}")
        st.text(resultados["info"])
        st.dataframe(resultados["dtypes"].to_frame("tipo"))
        st.dataframe(resultados["nulos"].to_frame("nulos"))
        st.write(f"Duplicados: {resultados['duplicados']}")

    elif mode == "notebook":
        print("Dimensiones:", resultados["dimensiones"])
        print(resultados["info"])
        print(resultados["dtypes"])
        print(resultados["nulos"])
        print("Duplicados:", resultados["duplicados"])

    if devolver_resultados:
        return resultados