# Importamos pandas
import pandas as pd

### Funcion Principal para la lectura de archivo csv y filtrar los datos por el id ###
def leer_y_filtrar_datos(id_a_filtrar):
    # Leemos el archivo csv con el nombre de test.csv
    df = pd.read_csv("df_covid19_countries.csv")
    # Hacemos el filtro por id y le pasamos un arreglo de todas las id a mostrar
    id = df[df['location'].isin(id_a_filtrar)]
    return id # Retornamos el id o sino no nos devolvera nada

# 1r Funcion para mostrar los datos de clock_speed por los id que le pasemos
def casosTotales(id_a_filtrar):
    # Llamamos a la funcion donde se muestra los id pasados
    data = leer_y_filtrar_datos(id_a_filtrar)
    # De esas id/muestras, mostramos solamente la columna de clock_speed
    clock = data["total_cases"]
    # Retornamos Clock
    return clock
    print(clock)
