class Gato():
    def __init__(self):
        self.color = "" #Esto es una propiedad
    
    def maulla(self): #Esto es un método (Es una acción)
        return "miau"

    def setColor(self,nuevocolor): #Defino un Setter - El metodo es el responsable de cambiar la propiedad
    
        #Aquí por ejemplo podria validar si el color es un color valido para un gato

        self.color = nuevocolor  # Y cambio la propiedad


gato 1 = Gato()
gato1.color = "naranja" #Aquí seteamos una propiedad directamente (no es buena practica)

gato1.setColor("naranja") # Esto es una practica mucho mejor

