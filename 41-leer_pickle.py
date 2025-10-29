#pip3 install pickle |pip install pickle
import pickle

archivo=open("datos.bin","wb")
cadena=pickle.loads(archivo)
print(cadena)

pickle.dump(cadena,archivo)

archivo.close()