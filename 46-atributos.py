import os

carpeta=input("Indica una carpeta: ")

elementos=os.listdir(carpeta)

for elemento in elementos:
    ruta = os.path.join(carpeta,elemento)
    print("Bryan |",elemento)
    print("Bryan |",os.path.getsize(ruta))
    print("Bryan |",os.path.getmtime(ruta))