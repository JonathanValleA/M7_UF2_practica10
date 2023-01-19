# Importamos pandas
import pandas as pd

### Funcion Principal para la lectura de archivo csv y filtrar los datos por el id ###
def leer_y_filtrar_datos(id_a_filtrar):
    # Leemos el archivo csv con el nombre de test.csv
    df = pd.read_csv("test.csv")
    # Hacemos el filtro por id y le pasamos un arreglo de todas las id a mostrar
    id = df[df['id'].isin(id_a_filtrar)]
    return id # Retornamos el id o sino no nos devolvera nada

# 1r Funcion para mostrar los datos de clock_speed por los id que le pasemos
def mostrar_clock_speed(id_a_filtrar):
    # Llamamos a la funcion donde se muestra los id pasados
    data = leer_y_filtrar_datos(id_a_filtrar)
    # De esas id/muestras, mostramos solamente la columna de clock_speed
    clock = data["clock_speed"]
    # Retornamos Clock
    return clock
    print(clock)

# 2n Funcion para mostrar los mega pixels por los id que le pasemos
def mostrar_mega_pixels(id_a_filtrar):
    data = leer_y_filtrar_datos(id_a_filtrar)
    # Aqui buscamos el px_width
    px = data["px_width"]
    return px
    print(px)

# 3r Funcion para mostrar los datos de battery_power por los id que le pasemos
def mostrar_battery_power(id_a_filtrar):
    data = leer_y_filtrar_datos(id_a_filtrar)
    # Aqui buscamos la columna Battery power
    battery = data["battery_power"]
    return battery
    print(battery)
