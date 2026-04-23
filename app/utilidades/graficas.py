import matplotlib.pyplot as plt
import seaborn as sns

def _finalize(fig):
    fig.tight_layout()
    return fig

def fig_histograma_kde(df, variable):
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(df[variable].dropna(), kde=True, ax=ax)
    ax.set_title(f"Distribución de {variable}")
    ax.set_xlabel(variable)
    ax.set_ylabel("Frecuencia")
    return _finalize(fig)

def fig_boxplot(df, variable):
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.boxplot(x=df[variable], ax=ax)
    ax.set_title(f"Boxplot de {variable}")
    ax.set_xlabel(variable)
    return _finalize(fig)

def fig_barras_categorica(df, variable):
    tabla = df[variable].value_counts()
    fig, ax = plt.subplots(figsize=(7, 4))
    tabla.plot(kind='bar', ax=ax)
    ax.set_title(f"Distribución de {variable}")
    ax.set_xlabel(variable)
    ax.set_ylabel("Frecuencia")
    ax.tick_params(axis='x', rotation=0)
    return _finalize(fig)

def fig_scatter(df, x='bill_length_mm', y='bill_depth_mm', hue='species'):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(f"Relación entre {x} y {y}")
    return _finalize(fig)

def fig_heatmap_correlacion(df):
    corr = df.select_dtypes(include='number').corr()
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(corr, cmap='coolwarm', annot=True, fmt=".2f", ax=ax)
    ax.set_title("Matriz de correlación")
    return _finalize(fig)

def fig_conteo_agrupado(df, group_cols=['island', 'species', 'sex']):
    conteo = df.groupby(group_cols).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 5))
    conteo.plot(kind='bar', ax=ax)
    ax.set_title('Especies de Pingüinos por Isla y Sexo')
    ax.set_xlabel('Grupo')
    ax.set_ylabel('Cantidad')
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title=group_cols[-1])
    return _finalize(fig)

def fig_boxplot_filtrado(df, especie='Adelie', variable='bill_length_mm', grupo='island', colores=None):
    df_filtrado = df[df['species'] == especie].copy()
    if df_filtrado.empty:
        raise ValueError(f"No hay datos para la especie: {especie}")
    if colores is None:
        colores = ['#378ADD', '#E24B4A', '#1D9E75']
    fig, ax = plt.subplots(figsize=(8, 5))
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
    return _finalize(fig)

def fig_multivariado(df, x_var='body_mass_g', y_vars=None, y_labels=None, hue='species'):
    if y_vars is None:
        y_vars = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']
    if y_labels is None:
        y_labels = y_vars
    fig, axes = plt.subplots(1, len(y_vars), figsize=(5 * len(y_vars), 4), sharex=True)
    if len(y_vars) == 1:
        axes = [axes]
    for i, (y, label) in enumerate(zip(y_vars, y_labels)):
        sns.scatterplot(data=df, x=x_var, y=y, hue=hue, ax=axes[i])
        axes[i].set_xlabel(x_var)
        axes[i].set_ylabel(label)
        if i < len(y_vars) - 1 and axes[i].get_legend() is not None:
            axes[i].get_legend().remove()
    fig.suptitle(f'Análisis multivariado de {x_var}')
    return _finalize(fig)

def fig_dashboard_resumen(df):
    corr = df.select_dtypes(include='number').corr()
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    sns.heatmap(corr, cmap='coolwarm', annot=True, fmt=".2f", ax=axes[0, 0])
    axes[0, 0].set_title('Matriz de correlación')
    sns.boxplot(data=df, x='species', y='body_mass_g', ax=axes[0, 1])
    axes[0, 1].set_title('Masa corporal por especie')
    sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', ax=axes[1, 0], legend=False)
    axes[1, 0].set_title('Longitud vs profundidad del pico')
    conteo = df.groupby(['island', 'species', 'sex']).size().unstack(fill_value=0)
    conteo.plot(kind='bar', ax=axes[1, 1])
    axes[1, 1].set_title('Especies por isla y sexo')
    axes[1, 1].tick_params(axis='x', rotation=45)
    return _finalize(fig)
