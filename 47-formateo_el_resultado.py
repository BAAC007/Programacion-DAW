import os

carpeta=input("Indica una carpeta: ")

elementos=os.listdir(carpeta)

for elemento in elementos:
    ruta = os.path.join(carpeta,elemento)
    print("Bryan |",elemento)
    print("Bryan |",os.path.getsize(ruta)/(1024*1024),"mb")
    print("Bryan |",os.path.getmtime(ruta))