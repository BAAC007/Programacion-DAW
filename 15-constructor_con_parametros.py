class Gato():
    def __init__(self,edad): #El constructor se ejecuta si o si
        self.edad = edad

    def maulla(self):
        return "El gato esta maullando" #El resto de metodos solo se ejecutan si los llamas

gato1 = Gato()


print(gato1.maulla())