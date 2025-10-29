class Matematicas():
    def __init__(self):
        self.PI = 3.14169265359
    
    def Redondeo(self,numero):
        entero = int(numero)
        decimal = numero - entero
        if decimal < 0.5:
            redondeo = 0
        else:
            redondeo = 1
        return entero + redondeo

    def Techo(self,numero):
        return int(numero)+1
    def Suelo(self,numero):
        return int(numero)
    
mate = Matematicas()
print(mate.Redondeo(4.7))
print(mate.Redondeo(4.2))
print(mate.Techo(4.7))
print(mate.Suelo(4.7))