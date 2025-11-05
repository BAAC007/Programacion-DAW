class Cliente():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
    
    def Saludo(self):
        return "Hola, buenos dias"

    def setNombreCompleto(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def setApellidos(self, nuevos_apellidos):
        self.apellidos = nuevos_apellidos

    def setEmail(self, nuevo_email):
        self.email = nuevo_email

    def getNombreCompleto(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos

    def getEmail(self):
        return self.email

    
cliente1 = Cliente("", "", "")
print(cliente1.Saludo())

cliente1.setNombreCompleto("Ricardo")
print(cliente1.getNombreCompleto())

cliente1.setApellidos("Gomez")
print(cliente1.getApellidos())

cliente1.setEmail("infor@Rimez.com")
print(cliente1.getEmail())
