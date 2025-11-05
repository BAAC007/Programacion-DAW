import pickle

class Cliente():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

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

clientes = []

try:
    archivo = open("examen_unidad5.bin",'rb')
    clientes = pickle.load(archivo)
    archivo.close()
    print(clientes)
except:
    print("No existe archivo de datos")

print("Gestor de clientes V0.2 Bryan Alejandro Avila Castro")

while True:
        archivo = open("examen_unidad5.bin", "wb")
        pickle.dump(clientes, archivo)
        archivo.close()

        print("------------------")
        print("Selecciona una opcion")
        print("1.-Insertar un nuevo cliente")
        print("2.-Obtener un listado de clientes")
        opcion = int(input("Indique su opcion (1,2): "))

        if (opcion == 1):
            print("Voy a insertar un cliente")
            cliente1 = Cliente("","","")
            nombre_cliente = input("Introduzca el nombre del cliente: ")
            cliente1.setNombreCompleto(nombre_cliente)
            apellidos_cliente = input("Introduzca los apellidos del cliente: ")
            cliente1.setApellidos(apellidos_cliente)
            email_cliente = input("Introduzca el email del cliente: ")
            cliente1.setEmail(email_cliente)
            clientes.append(cliente1)
        elif (opcion == 2):
            print("Saco el listado de clientes")
            for cliente in clientes:
                print("------------------")
                print("Nombre: ", cliente.getNombreCompleto())
                print("Apellidos: ", cliente.getApellidos())
                print("Email: ", cliente.getEmail())
                print("------------------")