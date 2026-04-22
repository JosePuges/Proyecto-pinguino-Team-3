def limpiar_dataframe_penguins(df, mode="none"):
    df_limpio = df.copy()
    df_limpio = df_limpio.drop_duplicates()
    df_limpio = df_limpio.dropna(
        subset=[
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
        ]
    )
    if "sex" in df_limpio.columns:
        df_limpio["sex"] = df_limpio["sex"].fillna("DESCONOCIDO")
    return df_limpio
