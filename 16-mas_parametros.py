class Gato():
    def __init__(self,edad,nombre,raza): #El constructor se ejecuta si o si
        self.edad = edad
        self.nombre = nombre
        self.raza = raza

    def maulla(self):
        return "El gato esta maullando" #El resto de metodos solo se ejecutan si los llamas

gato1 = Gato(5,"misifu","esfinge")
