# archivo main.py
import pandas as pd
import matplotlib.pyplot as plt
from ejercicio3B import total_population, density_per_km2, density_per_m2

df = pd.read_csv('List of cities proper by population density11.csv')

result = total_population(df)
density_per_km2_results = density_per_km2(df)
density_per_m2_results = density_per_m2(df)

def grafica1(data, title):
    fig, ax = plt.subplots(figsize=(8,5))
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=45)
    ax.set_title(title)
    plt.legend()
    plt.show()

def menu():
    num = int(input("Que funcion quieres llamar?\n1)Total de poblacion por ciudades\n2)Densidad por KM2\n3)Densidad por M2\nNumero a introducir:"))

    if(num == 1):
        grafica1(result, 'Total de poblacion por ciudades')
        print("Total de poblacion por ciudades:")
        print(total_population(df))
    elif(num == 2):
        grafica1(density_per_km2_results, 'Densidad por KM2')
        print("\nDensidad por KM2:")
        print(density_per_km2(df))
    elif(num == 3):
        grafica1(density_per_m2_results, 'Densidad por M2')
        print("\nDensidad por M2:")
        print(density_per_m2(df))
    else:
        print("\n- Introduce un numero valido o una de las 3 funciones\n")
        menu()
menu()