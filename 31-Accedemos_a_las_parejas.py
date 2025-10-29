import json

archivo = open('28-Blog.json','r')

contenido = json.load(archivo)

for linea in contenido:
    print("------------------")
    print(linea["Titulo"])
    print("------------------")
    print(linea["Fecha"])
    print("------------------")
    print(linea["Autor"])
    print("------------------")
    print(linea["contenido"])
    print("------------------")
    print("")