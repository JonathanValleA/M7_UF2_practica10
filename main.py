import matplotlib.pyplot as plt
import ejercicio3 as ejercicio3

## Definir los id a filtrar que en todo caso serian las 10 muestras a mostrar.
id_a_filtrar = [3,13,34,56,70,85,110,120,210,400]
### Llamar a todas las funciones definida que esta en el archivo ejercicio3.py
leer_datos_data = ejercicio3.leer_y_filtrar_datos(id_a_filtrar)
clock_speed_data = ejercicio3.mostrar_clock_speed(id_a_filtrar)
megapixels_data = ejercicio3.mostrar_mega_pixels(id_a_filtrar)
battery_power_data = ejercicio3.mostrar_battery_power(id_a_filtrar)

## Definir los colores de la grafica Generica
colores = ['red','blue','green','orange','pink','lightblue','yellow','purple','brown','gray']
## Definir el tamaño de mi grafica de 8x5 Generica
fig, ax = plt.subplots(figsize= (8,5))
## La Posicion del arreglo id_a_filtrar
lista = [0,1,2,3,4,5,6,7,8,9]
# 1r Funcion para mostrar la grafica 1 de Clock_speed
def grafica_barras1(data, nombre_eje_x):
    plt.xlabel("Clock Speed")
    plt.ylabel("Count")
    plt.bar(lista, nombre_eje_x, color=colores)
    # Asigno los valores de id_a_filtrar a cada posicion de la lista
    plt.xticks(lista, id_a_filtrar)
    # Guardo todos los valores de clock_speed
    legend_list = clock_speed_data.values
    # Muestro en la legenda, los valores 2.8, 1.4 que hace referencia al clock_speed
    plt.legend(legend_list)
    plt.show()

# 2n Funcion para mostrar la grafica 2 de Mega Pixels
def grafica_barras2(data, nombre_eje_y):

    plt.xlabel("Mega Pixels")
    plt.ylabel("Count")
    plt.bar(lista, nombre_eje_y, color=colores)
    # Asigno los valores de id_a_filtrar a cada posicion de la lista
    plt.xticks(lista, id_a_filtrar)
    # Guardo todos los valores de clock_speed
    legend_list = megapixels_data.values
    # Muestro en la legenda, los valores 2.8, 1.4 que hace referencia al clock_speed
    plt.legend(legend_list)
    plt.show()

# 3n Funcion para mostrar la grafica 3 de Battery Power
def grafica_barras3(data, nombre_eje_z):
    plt.xlabel("Battery Power")
    plt.ylabel("Count")
    plt.bar(lista, nombre_eje_z, color=colores)
    # Asigno los valores de id_a_filtrar a cada posicion de la lista
    plt.xticks(lista, id_a_filtrar)
    # Guardo todos los valores de clock_speed
    legend_list = battery_power_data.values
    # Muestro en la legenda, los valores 2.8, 1.4 que hace referencia al clock_speed
    plt.legend(legend_list)
    plt.show()

# Funcion Principal para el menu de opciones y para llamar a mis 3 funciones
def inicio():
    entero = int(input("Que funcion quieres llamar?\n1)Mostrar el grafico de Clock_speed\n2)Mostrar el grafico de Mega Pixels\n3)Mostrar el grafico de Battery_power\nNumero a introducir:"))

    if(entero == 1):
        grafica_barras1(clock_speed_data.index,clock_speed_data.values)
        print(clock_speed_data)
    elif(entero == 2):
       grafica_barras2(megapixels_data.index, megapixels_data.values)
       print(megapixels_data)
    elif(entero == 3):
        grafica_barras3(battery_power_data.index, battery_power_data.values)
        print(battery_power_data)
    else:
        print("Introduce una de las 3 opcions (1-2-3)\n")
        inicio()
inicio()