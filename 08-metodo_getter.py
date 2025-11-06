class Gato():
    def __init__(self):
        self.color = "" #Esto es una propiedad
    
    def maulla(self): #Esto es un método (Es una acción)
        return "miau"

    def setColor(self,nuevocolor): #Defino un Setter - El metodo es el responsable de cambiar la propiedad
    
        #Aquí por ejemplo podria validar si el color es un color valido para un gato

        self.color = nuevocolor  # Y cambio la propiedad


    def getColor(self):
        #Una vez más, aquí podría poner validaciones si lo quisiera
        return self.color


gato 1 = Gato()
gato1.color = "naranja" #Aquí seteamos una propiedad directamente (no es buena practica)

gato1.setColor("naranja") # Esto es una practica mucho mejor

print(gato1.color) #Acceso directo, se puede pero no se recomienda

print(gato1.getColor()) #Acceso mediante método, se recomienda 