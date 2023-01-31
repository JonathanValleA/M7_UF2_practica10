import ejercicio3A
import matplotlib.pyplot as plt
import pandas as pd
def grafica():
    df = pd.read_csv("df_covid19_countries.csv", sep=",")
    df["total_deaths"] = df["date"].apply(lambda x: x[:7])

    casos_totales = ejercicio3A.casos_totales_pais(df)

    plt.figure(figsize=(10, 5))
    plt.title("Casos totales por país y mes")
    for country in casos_totales["location"].unique():
        country_data = casos_totales[casos_totales["location"] == country]
        plt.plot(country_data["location"], country_data["total_cases"], label=country)
    plt.legend()
    plt.show()

df = pd.read_csv("df_covid19_countries.csv", sep=",")
casos = ejercicio3A.casos_totales_pais(df)
print(casos)
