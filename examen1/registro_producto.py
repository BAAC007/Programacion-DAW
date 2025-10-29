"""
Programa de registro de un producto
V0.1 Bryan Alejandro Avila Castro
Este programa muestra el registro y la información de un producto 
"""

#Solicitamos al Usuario los datos del producto (NOMBRE, PRECIO, CANTIDAD)
nombre_producto = input("Ingrese el nombre del producto: ")
print("//----------------------//")
precio_producto = int(input("Ingrese el precio del producto: "))
print("//----------------------//")
cantidad_en_stock = int(input("Ingrese la cantidad del producto: "))


#Agregamos la constante IVA
IVA = 0.21


#Usamos condicionales para determinar la disponibilidad del producto según la cantidad del producto
if cantidad_en_stock > 0:
    print("//----------------------//")
    print("El producto esta disponible")
    print("//----------------------//")


#Agregamos otro condicional para advertir de un stock bajo del producto
if cantidad_en_stock < 5:
    print("//----------------------//")
    print("ADVERTENCIA!!!, el stock del producto tiene menos de 5 unidades.")
    print("//----------------------//")


#Calculamos el precio
precio_completo = precio_producto * IVA
precio_total = precio_completo * cantidad_en_stock


#Imprimimos los datos del producto
print("Nombre del producto: ",nombre_producto)
print("//----------------------//")
print("Precio del producto: ",precio_producto, "€")
print("//----------------------//")
print("La cantidad del producto: ",cantidad_en_stock, "unidades")
print("//----------------------//")
print("IVA: ",IVA, "€")
print("//----------------------//")
print("Precio del producto por el IVA: ",precio_completo, "€")
print("//----------------------//")
print("Precio total: ",precio_total, "€")
print("//----------------------//")