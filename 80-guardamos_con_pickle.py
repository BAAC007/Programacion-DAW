import pickle

class Cliente():
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

print("[----- Gestion de clientes V0.1 -----]")
print("[----- Bryan Alejandro Avila Castro -----]")
print("[-----------]")

clientes = []

try:    #OJO que igual no existe el archivo #
    archivo = open("clientes.dat", 'rb')
    clientes = pickle.load(archivo)
    archivo.close()
except:
    print("No existe archivo de datos")
    print("[-----------]")


while True:
    print("Escoge una opcion:")
    print("[-----------]")
    print("1.-Insertar un cliente.")
    print("[-----------]")
    print("2-.Listar cliente.")
    print("[-----------]")
    print("3-.Actualizar un cliente.")
    print("[-----------]")
    print("4-.Eliminar un cliente.")
    print("[-----------]")
    print("5-.Salir")
    print("[-----------]")
    opcion = int(input("Escoge una de las 5 opciones: "))
    print("[-----------]")

    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        print("[-----------]")
        apellido = input("Introduce el apellido del cliente: ")
        print("[-----------]")
        email = input("Introduce el email del cliente: ")
        print("[-----------]")
        clientes.append(Cliente(nombre,apellido,email))


    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID: ",identificador)
            print("[-----------]")
            print(cliente.nombre, cliente.apellido, cliente.email)
            print("[-----------]")
            identificador += 1


    elif opcion == 3:
        identificador = int(input("Introduce el id para modificar: "))
        print("[-----------]")
        nombre = input("Introduce el nombre del cliente: ")
        print("[-----------]")
        apellido = input("Introduce el apellido del cliente: ")
        print("[-----------]")
        email = input("Introduce el email del cliente: ")
        print("[-----------]")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellido = apellido
        clientes[identificador].email = email


    elif opcion == 4:
        identificador = int(input("Introduce el id para eliminar: "))
        confirmacion = input("¿Estas seguro? (S/N): ")
        if confirmacion == "S" or "s":
            clientes.pop(identificador) 
            print("[-----------]")
        elif confirmacion == "N" or "n":
            print("[-----------]")
            print("Cancelado")
            print("[-----------]")


    elif opcion == 5:
        archivo = open("clientes.dat", "wb")
        pickle.dump(clientes, archivo)
        print("Datos guardados correctamente. ¡Hasta pronto!")
        
    else:
        print("[-----------]")
        print("ERROR, opcion no valida")
        print("[-----------]")

