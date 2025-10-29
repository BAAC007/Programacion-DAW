import json

archivo = open('28-Blog.json','r')

contenido = json.load(archivo)

for linea in contenido:
    print(linea)