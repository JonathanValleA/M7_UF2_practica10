# Importamos pandas
import pandas as pd

### Funcion Principal para la lectura de archivo csv y filtrar los datos por el id ###
def leer_y_filtrar_datos(id_a_filtrar):
    df = pd.read_csv("test.csv")
    id = df[df['id'].isin(id_a_filtrar)]
    return id

# 1r Funcion para mostrar los datos de clock_speed por los id que le pasemos
def mostrar_clock_speed(id_a_filtrar):
    data = leer_y_filtrar_datos(id_a_filtrar)
    """ Lo hize de 2 opciones ya que de la primera, se me muestran los 10 id de clock_speed pero la grafica se me muestran muy finos
    en la otra opcion, lo agrupamos por clock_speed pero solo se me muestran los 6 id de clock_speed pero me sale bien la grafica """
    clock = data["clock_speed"]
    #clock = data.groupby('clock_speed')['clock_speed'].agg(len)
    return clock
    print(clock)

# 2n Funcion para mostrar los mega pixels por los id que le pasemos
def mostrar_mega_pixels(id_a_filtrar):
    data = leer_y_filtrar_datos(id_a_filtrar)
    #px = data["px_width"]
    px = data.groupby('px_width')['px_width'].agg(len)
    return px
    print(px)

# 3r Funcion para mostrar los datos de battery_power por los id que le pasemos
def mostrar_battery_power(id_a_filtrar):
    data = leer_y_filtrar_datos(id_a_filtrar)
    battery = data["battery_power"]
    #battery = data.groupby('battery_power')['battery_power'].agg(len)
    return battery
    print(battery)
