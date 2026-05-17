productos = []
cantidades = []
precios = [] # Creamos listas para guardar datos

archivo = open("datos_de_ventas.csv", "r") # Abrimos el archivo CSV creado

lineas = archivo.readlines() # Creamos variable para leer las líneas del archivo

for linea in lineas[1:]: # Salteamos el encabezado

    datos = linea.strip().split(",") # Quitamos los espacios en blanco y los salto de linea con .strip() y con .split() cortamos la linea del archivo cada vez que hay una coma para poder crear una lista ordenada

    producto = datos[1] # Accedemos al elemento 1 que va a ser siempre los productos
    cantidad = int(datos[2]) # Accedemos al elemento 2 que va a ser siempre las cantidades y los transformamos en int para manejarlos como numeros
    precio = int(datos[3]) # Accedemos al elemento 3 que va a ser siempre los precios y los transformamos en int para manejarlos como numeros

    productos.append(producto)
    cantidades.append(cantidad)
    precios.append(precio) # Los 3 datos extraidos de la linea del archivo lo guardamos con .append() al final de las listas creadas al inicio

archivo.close() # Cerramos el archivo para evitar errores

ventas_totales = 0 # Creamos una variabe para guardar las ventas totales

for i in range(len(cantidades)): # Recorremos con bucle for la lista cantidades
    ventas_totales += cantidades[i] # Guardamos las cantidades vendidas en la variable ventas_totales

ventas_productos = {} # Creamos diccionario para conocer el producto mas vendido

for i in range(len(productos)): # Recorremos con bucle for la lista productos

    producto = productos[i]
    cantidad = cantidades[i] # Creamos variables locales para poder iniciar estructuras condicionales

    if producto in ventas_productos: # Analizamos si el producto ya esta en el diccionario
        ventas_productos[producto] += cantidad # Si esta sumamos la cantidad correspondiente al producto
    else:
        ventas_productos[producto] = cantidad # Si no esta lo ponemos en el diccionario con su cantidad correspondiente

producto_mas_vendido = max(ventas_productos, key=ventas_productos.get) # Analizamos cual es el producto mas vendido y lo guardamos en la variable producto_mas_vendido

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido) # Mostramos los resultados

archivo_resumen = open("resultados/resumen.txt", "w") # Creamos el archivo resumen.txt en la carpeta resultados e ingresamos W para abrirlo en modo escribir

archivo_resumen.write("Ventas totales: " + str(ventas_totales) + "\n") # Escribimos en el archivo las ventas totales, transformamos el valor de ventas totales en str y saltamos la linea
archivo_resumen.write("Producto más vendido: " + producto_mas_vendido) # Escribimos en el archivo el producto mas vendido

archivo_resumen.close() # Cerramos el archivo para evitar errores

print("Análisis finalizado correctamente") # Comunicamos que el analisis fue finalizado

import matplotlib.pyplot as plt # importamos la libreria de python matplotlib con su modulo pyplot para realizar el grafico y le ponemos como apodo plt para que sea mas claro el codigo

nombres = list(ventas_productos.keys()) # Creamos una lista en la variable nombres de los nombres de los productos
valores = list(ventas_productos.values()) # Creamos una lista en la variable valores con las cantidades vendidas de cada producto

# Crear gráfico de barras
plt.bar(nombres, valores) # Creamos un grafico de barras y les pasamos los nombres y sus cantidades vendidas para que las acomode en orden

# Títulos
plt.title("Cantidad vendida por producto") # Ponemos un titulo
plt.xlabel("Productos") # Ingresamos el texto que va en el eje horizontal
plt.ylabel("Cantidad") # Ingresamos el texto que va en el eje vertical

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png") # Exportamos el grafico y lo guardamos como una imagen

print("Gráfico generado correctamente") # Comunicamos que el grafico fue generado correctamente
