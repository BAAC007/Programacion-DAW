archivo = open("Clientes.txt",'r') # r = Read (leer)

contenido = archivo.readline()
#Tambien existe archivo.readlines()

print(contenido)

archivo.close()