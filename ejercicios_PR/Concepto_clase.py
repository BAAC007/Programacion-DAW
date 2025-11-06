
'''
Programa de gatitos en el Parque Nacional Natural
V0.1 Bryan Alejandro Avila Castro
Programa de clases de gatos con su nombre y color 
'''



class Gato():
    def __init__(self):
        self.nombre = ""
        self.color = ""
    
class gato1(Gato):
    def __init__(self):
        self.nombre = "garfield"
        self.color = "naranja"
        

class gato2(Gato):
    def __init__(self):    
        self.nombre = "gustavo"
        self.color = "naranja"
    
print("----------------")

gatito1 = gato1()
print(gatito1.nombre)
print(gatito1.color)

print("----------------")

gatito2 = gato2()
print(gatito2.nombre)
print(gatito2.color)

print("----------------")