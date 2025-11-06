'''
Programa de gestion de productos
V0.1 Bryan Alejandro Avila Castro
Este programa gestiona productos

'''

#esta aplicación no aplica importar librerías

class Product():
    def __init__():
        self.nombre = ""
        self.precio = 0


#creamos las variables globales

productos = []

#primero lanzamos un mensaje de bienvenida

print("Gestos de productos V0.1 Bryan Alejandro Avila Castro")

#Metemos al usuario en un bucle infinito
while True:

    #le mostramos al usuario las opciones que tiene

    print("Selecciona una opcion")
    print("1.-Crear un nuevo producto")
    print("2.-Listar productos")
    print("3.-Actualizar productos")
    print("4.-Eliminar productos")
    opcion = int(input("Escoge tu opcion: "))

    #En función de la opción que coja el usuario
    if opcion == 1:
        # O bien creamos un nuevo producto
        print("Creamos un nuevo producto")
        producto = Producto() #creo una nueva instancia de la clase
        producto.nombre = input("Introduce el nombre del producto: ") #Escribo la propiedad
        producto.precio = input("Introduce el precio del producto: ") #Escribo la propiedad
        producto.append(prodcuto1) # Y a la Lista se le añade el producto.



    elif opcion == 2:
        # O bien listamos los productos
        print("Vamos a listar productos")
    elif opcion == 3:
        # O bien actualizamos los productos
        print("Vamos a actualizar los productos")
    elif opcion == 4: 
        # O bien eliminamos los productos
        print("Vamos a eliminar un producto")
    #Y volvemos a repetir

    