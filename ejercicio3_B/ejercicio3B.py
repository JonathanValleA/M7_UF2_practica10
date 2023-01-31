import pandas as pd

def total_population(df):
    df['Population'].fillna(0, inplace=True)
    df['Population'] = df['Population'].astype(str).str.replace(',', '').astype(int)
    df = df.nlargest(10, 'Population')
    return df.groupby('City')['Population'].sum()

def density_per_km2(df):
    df['Density KM2'].fillna(0, inplace=True)
    df['Density KM2'] = df['Density KM2'].astype(str).str.replace(',', '').astype(float)
    df = df.nlargest(10, 'Density KM2')
    return df.groupby('City')['Density KM2'].sum()

def density_per_m2(df):
    df['Density  M2'].fillna(0, inplace=True)
    df['Density  M2'] = df['Density  M2'].astype(str).str.replace(',', '').astype(float)
    df = df.nlargest(10, 'Density  M2')
    return df.groupby('City')['Density  M2'].sum()