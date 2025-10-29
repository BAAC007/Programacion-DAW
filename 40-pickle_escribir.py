#pip3 install pickle |pip install pickle
import pickle

archivo=open("datos.bin","wb")
cadena="Bryan Avila"

pickle.dump(cadena,archivo)

archivo.close()