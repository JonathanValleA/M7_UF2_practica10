import matplotlib.pyplot as plt
import ejercicio3 as ejercicio3

id_a_filtrar = [3,13,34,56,70,85,110,120,210,400]
leer_datos_data = ejercicio3.leer_y_filtrar_datos(id_a_filtrar)
clock_speed_data = ejercicio3.mostrar_clock_speed(id_a_filtrar)
megapixels_data = ejercicio3.mostrar_mega_pixels(id_a_filtrar)
battery_power_data = ejercicio3.mostrar_battery_power(id_a_filtrar)

colores = ['red','blue','green','orange','pink','lightblue','yellow']
def grafica_barras1(data, nombre_eje_x):
    fig, ax = plt.subplots(figsize= (8,5))
    plt.xlabel("Clock Speed")
    plt.ylabel("Count")
    plt.bar(data, nombre_eje_x, color=colores)
    plt.show()
def grafica_barras2(data, nombre_eje_y):
    fig, ax = plt.subplots(figsize=(8, 5))
    plt.xlabel("Mega Pixels")
    plt.ylabel("Count")
    plt.bar(data, nombre_eje_y, color=colores)
    plt.show()

def grafica_barras3(data, nombre_eje_z):
    fig, ax = plt.subplots(figsize=(8, 5))
    plt.xlabel("Battery Power")
    plt.ylabel("Count")
    plt.bar(data, nombre_eje_z, color=colores)
    plt.show()

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