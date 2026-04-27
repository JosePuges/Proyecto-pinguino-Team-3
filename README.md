# Proyecto-pinguino-Team-3
# 🐧 Palmer Penguins — Exploratory Data Analysis
 **Equipo de investigadores:** Alejandro Posada, Arantxa Puig, Jose Puges, Eva Pontón y Oksana Tokmakova.

<div align="center">



*Análisis exploratorio completo del dataset Palmer Penguins — estadística descriptiva, visualización y segmentación por especie.*

</div>

---

## 📌 Descripción del proyecto

Este proyecto realiza un **análisis exploratorio de datos (EDA)** sobre el dataset **Palmer Penguins**, una alternativa moderna al clásico Iris dataset, que recoge mediciones morfológicas de 344 pingüinos de tres especies distintas en el Archipiélago Palmer (Antártida).

El objetivo es extraer insights sobre las diferencias entre especies, detectar patrones, gestionar valores nulos y preparar el dataset para futuras etapas de modelado.

---

## 🗂️ Estructura del proyecto

```
📁 palmer-penguins-eda/
│
├── 📓 01_eda_descriptivo.ipynb       # Estadística descriptiva y distribuciones
├── 📓 02_visualizacion.ipynb         # Boxplots, histogramas y pairplots
├── 📓 03_outliers_nulos.ipynb        # Detección de outliers y tratamiento de nulos
├── 📊 data/
│   └── penguins.csv                  # Dataset original
├── 📁 img/                           # Gráficos exportados
└── 📄 README.md
```

---

## 🐧 Sobre el dataset

| Campo | Detalle |
|---|---|
| **Fuente** | [palmerpenguins (R/Python)](https://allisonhorst.github.io/palmerpenguins/) |
| **Filas** | 344 pingüinos |
| **Columnas** | 8 variables |
| **Especies** | Adelie · Chinstrap · Gentoo |
| **Islas** | Biscoe · Dream · Torgersen |
| **Valores nulos** | 19 (0,69% del total) |

### Variables del dataset

| Variable | Tipo | Descripción |
|---|---|---|
| `species` | Categórica | Especie del pingüino |
| `island` | Categórica | Isla de origen |
| `bill_length_mm` | Numérica | Longitud del pico (mm) |
| `bill_depth_mm` | Numérica | Profundidad del pico (mm) |
| `flipper_length_mm` | Numérica | Longitud de la aleta (mm) |
| `body_mass_g` | Numérica | Masa corporal (gramos) |
| `sex` | Categórica | Sexo del individuo |
| `year` | Numérica | Año de observación |

---

## 🔍 Principales hallazgos

Aplicando la pirámide invertida, primero lo importante, sacamos en conclusión que, las características físicas de los pingüinos no son independientes, sino que siguen patrones coherentes que permiten diferenciar grupos de forma bastante nítida.

En concreto, se observan tres hallazgos principales. 
Primero; la masa corporal y la longitud de la aleta presentan la correlación más fuerte: los pingüinos más grandes tienden a tener aletas más largas, una relación lo suficientemente consistente como para ser predictiva.
Segundo; las variables del pico aportan matices más sutiles, pero también contribuyen a la discriminación entre especies. 
Y tercero; al combinar variables de tamaño con variables del pico, la separación entre especies se vuelve aún más evidente.

Si nos fijamos en el scatterplot, aparecen tres clusters claramente diferenciados sin necesidad de aplicar ningún algoritmo: los propios datos ya revelan la estructura.

Y, como en el resto del análisis, se incluyen opciones de exportación: descarga de datos y de gráficos. Porque el análisis no debería quedarse en la pantalla, sino poder trasladarse fuera de ella.


### 📊 Distribución y asimetría
- La variable `body_mass_g` presenta **asimetría positiva global (skewness = 0.47)**, generada por la diferencia biológica entre especies, no por outliers reales.
- Dentro de cada especie, las distribuciones son **simétricas e independientes** (skewness ≈ 0).

### ⚖️ Diferencias entre especies

```
Adelie     ████████████░░░░░░░░  3.701g media
Chinstrap  ████████████░░░░░░░░  3.733g media  
Gentoo     ████████████████████  5.076g media  (+1.375g respecto a las otras)
```

> El mínimo de Gentoo (3.950g) es prácticamente igual al máximo de Adelie (4.775g). No se solapan.

### 🔴 Outliers detectados (método IQR)
- **Adelie**: 0 outliers
- **Gentoo**: 0 outliers
- **Chinstrap**: 2 outliers
  - Macho, 4.800g — extremo superior (pico 52mm, coherente biológicamente)
  - Hembra, 2.700g — extremo inferior (posiblemente individuo joven o en mal estado)
  - **Decisión**: se mantienen en el dataset al ser valores biológicamente plausibles.

### 🕳️ Valores nulos
- Las medidas físicas (`bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`) presentan **2 nulos** — probablemente el mismo individuo.
- La variable `sex` tiene **11 nulos (3.2%)** — la más relevante a tratar.

---

## 🛠️ Tecnologías utilizadas

```python
import pandas as pd          # Manipulación de datos
import numpy as np           # Cálculo numérico
import seaborn as sns        # Visualización estadística
import matplotlib.pyplot as plt  # Gráficos
from palmerpenguins import load_penguins  # Carga del dataset
```

---

## ▶️ Cómo ejecutar el proyecto

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/palmer-penguins-eda.git
cd palmer-penguins-eda

# 2. Crear entorno virtual e instalar dependencias
python -m venv myvenv
source myvenv/bin/activate        # Mac/Linux
myvenv\Scripts\activate           # Windows

pip install -r requirements.txt

# 3. Abrir Jupyter
jupyter notebook
```

---

## 📈 Próximos pasos

- [ ] Segmentación y clustering por especie
- [ ] Modelo de clasificación supervisada
- [ ] Análisis de correlaciones entre variables morfológicas
- [ ] Dashboard interactivo con Plotly

---

## 👥 Equipo de investigación

| Nombre | GitHub |
|---|---|
| _Alejandro Posada_ | [@AlexPG14](#) |
| _Arantxa Puig_ | [@ArantxaPuig(#) |
| _Eva Pontón_ | [@evaponton](#) |
| _Jose Puges_ | [@JosePuges](#) |
| _Oksana Tokmakova_ | [@ksu727096-maker](#) |
---

<div align="center">
  <sub>Proyecto desarrollado en el bootcamp de Análisis de Datos · Factoría F5 · 2026</sub>
</div>
