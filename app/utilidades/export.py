import streamlit as st
import pandas as pd
from io import BytesIO


def descargar_metricas_csv(metricas, nombre_archivo="metricas_penguins.csv"):
    df_metricas = pd.DataFrame(
        list(metricas.items()),
        columns=["Metrica", "Valor"]
    )

    csv = df_metricas.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Descargar métricas CSV",
        data=csv,
        file_name=nombre_archivo,
        mime="text/csv"
    )


def descargar_grafico_matplotlib(fig, nombre_archivo="grafico.png"):
    buffer = BytesIO()
    fig.savefig(buffer, format="png", bbox_inches="tight", dpi=300)
    buffer.seek(0)

    st.download_button(
        label="📥 Descargar gráfico PNG",
        data=buffer,
        file_name=nombre_archivo,
        mime="image/png"
    )


def descargar_grafico_plotly(fig, nombre_archivo="grafico_interactivo.html"):
    html = fig.to_html(include_plotlyjs="cdn")

    st.download_button(
        label="📥 Descargar gráfico interactivo HTML",
        data=html,
        file_name=nombre_archivo,
        mime="text/html"
    )

def exportar_estadisticos(df, variable, nombre_archivo=None):
    """
    Genera estadísticas descriptivas + skew y permite descargarlas en CSV
    """

    df_stats = df[variable].describe().to_frame("valor")
    df_stats.loc["skew"] = df[variable].skew()

    if nombre_archivo is None:
        nombre_archivo = f"estadisticos_{variable}.csv"

    csv = df_stats.to_csv().encode("utf-8")

    st.download_button(
        label="📥 Descargar estadísticas CSV",
        data=csv,
        file_name=nombre_archivo,
        mime="text/csv"
    )

def descargar_csv(df, nombre="datos.csv"):
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Descargar CSV",
        data=csv,
        file_name=nombre,
        mime="text/csv"
    )