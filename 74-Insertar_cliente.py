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
        cliente.append(Cliente(nombre,apellido,email))

    elif opcion == 2:


    elif opcion == 3:


    elif opcion == 4:
