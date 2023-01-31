import pandas as pd

def casos_totales_pais(df):
    df_grouped = df.groupby(["location", "date"]).sum().reset_index()
    df_grouped = df_grouped[["location", "date"]]
    df_grouped['location'].fillna(0, inplace=True)
    df_grouped['location'] = df_grouped['location'].astype(str).str.replace(',', '').astype(float)

    top_10_countries = df_grouped.nlargest(10, 'location')
    df_grouped = df_grouped[df_grouped["location"].isin(top_10_countries)]
    return df_grouped

def muertes_totales_pais(df):
    df_grouped = df.groupby(["location", "date"]).sum().reset_index()
    df_grouped = df_grouped[["location", "date", "total_deaths"]]
    top_10_countries = df_grouped["location"].value_counts().index[:10]
    df_grouped = df_grouped[df_grouped["location"].isin(top_10_countries)]
    return df_grouped

def reproduction_rate_pais(df):
    df_grouped = df.groupby(["location", "date"]).sum().reset_index()
    df_grouped["reproduction_rate"] = df_grouped["Confirmed"] / df_grouped["total_deaths"]
    df_grouped = df_grouped[["location", "date", "reproduction_rate"]]
    top_10_countries = df_grouped["location"].value_counts().index[:10]
    df_grouped = df_grouped[df_grouped["location"].isin(top_10_countries)]
    return df_grouped