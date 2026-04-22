import matplotlib.pyplot as plt
import seaborn as sns


def _mostrar_figura(fig, mode="notebook"):
    if mode == "streamlit":
        import streamlit as st
        st.pyplot(fig)
    elif mode == "notebook":
        from IPython.display import display
        display(fig)
    elif mode == "none":
        pass
    else:
        raise ValueError("mode debe ser 'notebook', 'streamlit' o 'none'")
    plt.close(fig)


def plot_scatter_penguins(df, x='bill_length_mm', y='bill_depth_mm', hue='species', mode="notebook", devolver_fig=False):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(f'Relación entre {x} y {y}')
    fig.tight_layout()
    _mostrar_figura(fig, mode)
    if devolver_fig:
        return fig


def plot_boxplot_penguins(df, x='species', y='body_mass_g', mode="notebook", devolver_fig=False):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x=x, y=y, ax=ax)
    ax.set_title(f'{y} por {x}')
    fig.tight_layout()
    _mostrar_figura(fig, mode)
    if devolver_fig:
        return fig


def correlacion_heatmap(df, mostrar_tabla=False, mode="notebook", devolver_fig=False):
    corr = df.select_dtypes(include='number').corr()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, cmap='coolwarm', annot=True, ax=ax)
    ax.set_title("Matriz de correlación")
    fig.tight_layout()

    if mostrar_tabla:
        if mode == "streamlit":
            import streamlit as st
            st.write("Matriz de correlación:")
            st.dataframe(corr)
        elif mode == "notebook":
            from IPython.display import display
            display(corr)

    _mostrar_figura(fig, mode)
    if devolver_fig:
        return fig


def plot_conteo_penguins(df, group_cols=None, mode="notebook", devolver_fig=False, mostrar_tabla=False):
    if group_cols is None:
        group_cols = ['island', 'species', 'sex']

    conteo = df.groupby(group_cols).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 6))
    conteo.plot(kind='bar', ax=ax)
    ax.set_title('Especies de Pingüinos por Isla y Sexo')
    ax.set_xlabel('Grupo')
    ax.set_ylabel('Cantidad de Pingüinos')
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title='Sexo')
    fig.tight_layout()

    if mostrar_tabla:
        if mode == "streamlit":
            import streamlit as st
            st.write("Tabla de conteo:")
            st.dataframe(conteo)
        elif mode == "notebook":
            from IPython.display import display
            display(conteo)

    _mostrar_figura(fig, mode)
    if devolver_fig:
        return fig


def plot_boxplot_adelie_island(df, especie='Adelie', variable='bill_length_mm', grupo='island', colores=None, mode="notebook", devolver_fig=False):
    df_filtrado = df[df['species'] == especie]
    if df_filtrado.empty:
        raise ValueError(f"No hay datos para la especie: {especie}")
    if colores is None:
        colores = ['#378ADD', '#E24B4A', '#1D9E75']

    fig, ax = plt.subplots(figsize=(10, 6))
    bp = df_filtrado.boxplot(column=variable, by=grupo, patch_artist=True, return_type='dict', ax=ax)

    for patch, color in zip(bp[variable]['boxes'], colores):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    for median in bp[variable]['medians']:
        median.set_color('black')
        median.set_linewidth(1.5)

    ax.set_title(f'{variable} de {especie} por {grupo}')
    plt.suptitle('')
    ax.set_xlabel(grupo)
    ax.set_ylabel(variable)
    fig.tight_layout()
    _mostrar_figura(fig, mode)
    if devolver_fig:
        return fig


def plot_multivariado_penguins(df, x_var='body_mass_g', y_vars=None, y_labels=None, hue='species', mode="notebook", devolver_fig=False):
    if y_vars is None:
        y_vars = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']
    if y_labels is None:
        y_labels = y_vars

    fig, ax = plt.subplots(nrows=1, ncols=len(y_vars), figsize=(5 * len(y_vars), 4), sharex=True)
    if len(y_vars) == 1:
        ax = [ax]

    for i, (y, y_label) in enumerate(zip(y_vars, y_labels)):
        sns.scatterplot(data=df, x=x_var, y=y, hue=hue, ax=ax[i])
        ax[i].set_xlabel(x_var)
        ax[i].set_ylabel(y_label)
        if i < len(y_vars) - 1 and ax[i].get_legend() is not None:
            ax[i].get_legend().remove()

    fig.suptitle(f'Análisis Multivariado de {x_var}')
    fig.tight_layout()
    _mostrar_figura(fig, mode)
    if devolver_fig:
        return fig


def plot_dashboard_penguins(df, mode="notebook", devolver_fig=False):
    corr = df.select_dtypes(include='number').corr()
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    sns.heatmap(corr, cmap='coolwarm', annot=True, ax=axes[0, 0])
    axes[0, 0].set_title('Matriz de correlación')

    sns.boxplot(data=df, x='species', y='body_mass_g', ax=axes[0, 1])
    axes[0, 1].set_title('Masa corporal por especie')

    sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', ax=axes[1, 0], legend=False)
    axes[1, 0].set_title('Longitud vs profundidad del pico')

    conteo = df.groupby(['island', 'species', 'sex']).size().unstack(fill_value=0)
    conteo.plot(kind='bar', ax=axes[1, 1])
    axes[1, 1].set_title('Especies por isla y sexo')

    for eje in axes.flat:
        eje.tick_params(axis='x', rotation=45)

    fig.tight_layout()
    _mostrar_figura(fig, mode)
    if devolver_fig:
        return fig
