class Cliente():
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

print("[----- Gestion de clientes V0.1 -----]")
print("[----- Bryan Alejandro Avila Castro -----]")

clientes = []

while True:
    print("Escoge una opcion:")
    print("1.-Insertar un cliente.")
    print("2-.Listar cliente.")
    print("3-.Actualizar un cliente.")
    print("4-.Eliminar un cliente.")
    opcion = int(input("Escoge una de las 4 opciones: "))

    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellido = input("Introduce el apellido del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre,apellido,email))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID: ",identificador)
            print(cliente.nombre, cliente.apellido, cliente.email)
            identificador += 1

    elif opcion == 3:
        identificador = int(input("Introduce el id para modificar: "))
        nombre = input("Introduce el nombre del cliente: ")
        apellido = input("Introduce el apellido del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellido = apellido
        clientes[identificador].email = email


    elif opcion == 4:
        identificador = int(input("Introduce el id para modificar: "))
        confirmacion = input("¿Estas seguro? (S/N): ")
        if confirmacion == "S" or "s":
            clientes.pop(identificador) 
        elif confirmacion == "N" or "n":
            print("Cancelado")
        else:
            print("ERROR, opcion no valida")