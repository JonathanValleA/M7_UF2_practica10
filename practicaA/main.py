import matplotlib.pyplot as plt
import ejercicioA as exA

id_a_filtrar = ["Afghanistan","Albania","Algeia","Andorra",
                "Anguilla","Australia","Austria","Azerbaijan","Bahamas","Bahrain"]

leer_datos_data = exA.leer_y_filtrar_datos(id_a_filtrar)

casosTotales = exA.casosTotales(id_a_filtrar)
## Definir los colores de la grafica Generica
colores = ['red','blue','green','orange','pink','lightblue','yellow','purple','brown','gray']
## Definir el tamaño de mi grafica de 8x5 Generica
fig, ax = plt.subplots(figsize= (8,5))
## La Posicion del arreglo id_a_filtrar
lista = [0,1,2,3,4,5,6,7,8,9]

def grafica_barras1(data, nombre_eje_x):
    plt.xlabel("Casos Totales")
    plt.ylabel("Count")
    plt.plot(lista, nombre_eje_x, color=colores)
    # Asigno los valores de id_a_filtrar a cada posicion de la lista
    plt.xticks(lista, id_a_filtrar)
    # Guardo todos los valores de clock_speed
    legend_list = casosTotales.values
    # Muestro en la legenda, los valores 2.8, 1.4 que hace referencia al clock_speed
    plt.legend(legend_list)
    plt.show()

grafica_barras1(casosTotales.index, casosTotales.values)