import zipfile
import os

carpeta = input("Indica una carpeta: ")

for directorio,carpetas,archivo in os.walk(carpeta):
    for nombre_archivo in archivo:
        origen = os.path.join(directorio,archivo)
        destino = os.path.join(directorio, archivo)+".zip"
        archivo = zipfile.ZipFile(destino, "w", compression = zipfile.ZIP_DEFLATED)
        archivo.write(origin, arcname = nombre_archivo)