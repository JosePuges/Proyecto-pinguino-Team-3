## Inspección inicial

1. La variable body_mass_g presenta asimetría positiva (skewness = X), lo que indica que la distribución no es normal y la media no es el estadístico más representativo. Se recomienda usar la mediana o aplicar transformación logarítmica antes de modelar.
2. ¿Qué problema de calidad es más relevante?
Los 11 nulos en Sex, porque es una variable categórica clave para análisis biológico y no se puede imputar matemáticamente como las numéricas — requiere criterio de dominio o descarte.
3. ¿Por qué le importa al cliente?
Si el cliente quiere analizar diferencias físicas entre machos y hembras (algo típico en estudios de fauna), esos 11 registros quedan fuera o introducen sesgo, afectando directamente la fiabilidad de sus conclusiones.
