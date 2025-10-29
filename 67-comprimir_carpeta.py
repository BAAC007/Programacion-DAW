import os
import zipfile

origen = 'archivos'
destino = 'archivos.zip'

archivozip = zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED)
for directorio,carpetas,archivos in os.walk(origen):
    for archivo in archivos:
        rutaarchivo = os.path.join(directorio, archivo)
        rutaalternativa = os.path.relpath(rutaarchivo, origen)
        archivo.write(rutaarchivo, rutarelativa)

archivozip.close()