class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""

    def setNombreCompleto(self,nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email

#CRUD - create- read- update- delete

#CRUD SQL - INSERT- SELECT- UPDATE- DELETE


clientes = [] ####### Meto una lista de clientes vacia

print("Gestor de clientes V0.1 Bryan Alejandro Avila Castro")

while True:
        print("Selecciona una opcion")
        print("1.-Insertar un nuevo cliente")
        print("2.-Obtener un listado de clientes")
        opcion = int(input("Indique su opcion (1,2): "))

        if (opcion == 1):
            print("Voy a insertar un cliente")
            nuevocliente = Cliente()
            nombrecliente = input("Introduzca el nombre del cliente: ")#Tomo el dato
            nuevocliente.setNombreCompleto(nombrecliente) #Uso el metodo set para meter el dato en el objeto
            emailcliente = input("Introduzca el email del cliente: ") #Tomo el dato
            nuevocliente.setEmail(emailcliente) #Uso el metodo set para meter el dato en el objeto
            clientes.append(nuevocliente)
        elif (opcion == 2): #Los getters se usan en las operaciones de listado
            print("Saco el listado de clientes")
            for cliente in clientes:
                print("------------------")
                print("Nombre", cliente.getNombreCompleto())
                print("Email", cliente.getEmail())
                print("------------------")
