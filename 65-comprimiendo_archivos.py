import zipfile

origen = 'modelo2.py'

destino = 'ejercicio.zip'

archivo = zipfile.ZipFile(destino,'w')
archivo.write(origen)