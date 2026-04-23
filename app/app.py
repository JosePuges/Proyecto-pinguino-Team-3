import streamlit as st

from utilidades.carga_datos import cargar_dataset_penguins
from utilidades.limpieza import limpiar_dataframe_penguins
from utilidades.inspeccion import obtener_resumen_dataframe, mostrar_resumen_streamlit
from utilidades.graficas import (
    fig_histograma_kde,
    fig_boxplot,
    fig_barras_categorica,
    fig_scatter,
    fig_heatmap_correlacion,
    fig_conteo_agrupado,
    fig_boxplot_filtrado,
    fig_multivariado,
    fig_dashboard_resumen
)

st.set_page_config(page_title="Dashboard Pingüinos", layout="wide")

st.title("Dashboard interactivo de Palmer Penguins")
st.caption("Versión web del notebook con filtros, análisis y visualizaciones interactivas en Streamlit.")

@st.cache_data
def cargar_datos():
    df = cargar_dataset_penguins()
    return limpiar_dataframe_penguins(df)

df = cargar_datos()

st.sidebar.header("Filtros")
species_opts = sorted(df["species"].dropna().unique().tolist())
island_opts = sorted(df["island"].dropna().unique().tolist())
sex_opts = sorted(df["sex"].dropna().unique().tolist())

species_sel = st.sidebar.multiselect("Especie", species_opts, default=species_opts)
island_sel = st.sidebar.multiselect("Isla", island_opts, default=island_opts)
sex_sel = st.sidebar.multiselect("Sexo", sex_opts, default=sex_opts)

df_filtrado = df[
    df["species"].isin(species_sel) &
    df["island"].isin(island_sel) &
    df["sex"].isin(sex_sel)
].copy()

st.sidebar.markdown("---")
st.sidebar.metric("Filas filtradas", len(df_filtrado))
st.sidebar.metric("Filas totales", len(df))

if df_filtrado.empty:
    st.warning("No hay datos con esos filtros. Ajusta la selección del panel lateral.")
    st.stop()

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Resumen",
    "Inspección",
    "Variables numéricas",
    "Variables categóricas",
    "Relaciones",
    "Dashboard final"
])

with tab1:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Pingüinos", len(df_filtrado))
    c2.metric("Especies", df_filtrado["species"].nunique())
    c3.metric("Islas", df_filtrado["island"].nunique())
    c4.metric("Sexos", df_filtrado["sex"].nunique())

    st.subheader("Vista previa")
    st.dataframe(df_filtrado.head(), use_container_width=True)

    st.subheader("Resumen general")
    st.pyplot(fig_dashboard_resumen(df_filtrado))

with tab2:
    st.subheader("Inspección del dataset filtrado")
    resumen = obtener_resumen_dataframe(df_filtrado)
    mostrar_resumen_streamlit(resumen)

with tab3:
    st.subheader("Análisis univariante de variables numéricas")
    variables_numericas = ['bill_length_mm', 'bill_depth_mm', 'body_mass_g', 'flipper_length_mm']
    variable_num = st.selectbox("Selecciona variable numérica", variables_numericas)

    c1, c2 = st.columns([1, 1])
    with c1:
        st.write("Estadísticos")
        st.dataframe(df_filtrado[variable_num].describe().to_frame("valor"), use_container_width=True)
        st.write(f"Asimetría (skew): {df_filtrado[variable_num].skew():.4f}")
    with c2:
        st.write("Histograma")
        st.pyplot(fig_histograma_kde(df_filtrado, variable_num))

    st.write("Boxplot")
    st.pyplot(fig_boxplot(df_filtrado, variable_num))

with tab4:
    st.subheader("Análisis univariante de variables categóricas")
    variables_categoricas = df_filtrado.select_dtypes(include="object").columns.tolist()
    variable_cat = st.selectbox("Selecciona variable categórica", variables_categoricas)

    frec = df_filtrado[variable_cat].value_counts()
    prop = df_filtrado[variable_cat].value_counts(normalize=True).round(4)

    c1, c2 = st.columns([1, 1])
    with c1:
        st.write("Frecuencias")
        st.dataframe(frec.to_frame("frecuencia"), use_container_width=True)
    with c2:
        st.write("Proporciones")
        st.dataframe(prop.to_frame("proporción"), use_container_width=True)

    st.pyplot(fig_barras_categorica(df_filtrado, variable_cat))

with tab5:
    st.subheader("Análisis bivariado y multivariado")
    section = st.radio(
        "Selecciona visualización",
        ["Scatterplot", "Heatmap correlación", "Conteo agrupado", "Boxplot filtrado", "Multivariado"],
        horizontal=True
    )

    if section == "Scatterplot":
        x_var = st.selectbox("Eje X", ['bill_length_mm', 'bill_depth_mm', 'body_mass_g', 'flipper_length_mm'], index=0, key="scatter_x")
        y_var = st.selectbox("Eje Y", ['bill_length_mm', 'bill_depth_mm', 'body_mass_g', 'flipper_length_mm'], index=1, key="scatter_y")
        st.pyplot(fig_scatter(df_filtrado, x=x_var, y=y_var, hue="species"))

    elif section == "Heatmap correlación":
        st.dataframe(df_filtrado.select_dtypes(include="number").corr(), use_container_width=True)
        st.pyplot(fig_heatmap_correlacion(df_filtrado))

    elif section == "Conteo agrupado":
        st.pyplot(fig_conteo_agrupado(df_filtrado))

    elif section == "Boxplot filtrado":
        especie = st.selectbox("Especie", sorted(df_filtrado["species"].unique().tolist()))
        variable = st.selectbox("Variable", ['bill_length_mm', 'bill_depth_mm', 'body_mass_g', 'flipper_length_mm'])
        st.pyplot(fig_boxplot_filtrado(df_filtrado, especie=especie, variable=variable, grupo="island"))

    elif section == "Multivariado":
        x_var = st.selectbox("Variable eje X", ['body_mass_g', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm'], index=0, key="multi_x")
        st.pyplot(fig_multivariado(
            df_filtrado,
            x_var=x_var,
            y_vars=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm'],
            y_labels=['Longitud del pico [mm]', 'Altura del pico [mm]', 'Longitud de la aleta [mm]'],
            hue='species'
        ))

with tab6:
    st.subheader("Dashboard final")
    st.pyplot(fig_dashboard_resumen(df_filtrado))
