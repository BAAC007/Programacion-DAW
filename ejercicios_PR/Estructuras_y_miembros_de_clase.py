class Rutina():
    def __init__(self, nombre, ejercicio, duracion):
        self.nombre = nombre
        self.ejercicio = ejercicio
        self.duracion = duracion

print("Programa de gestión de rutinas v0.1 Bryan Alejandro Avila Castro")

# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar rutina")
print("2.-Listar rutinas")
print("3.-Actualizar rutina")
print("4.-Eliminar rutina")

#Creamos una lista vacia
rutinas = []


while True: #Esto desata un bucle infinito pero controlado

    # Le permito escoger una opción
    opcion = int(input("Escoge una opción: "))

    if opcion == 1:

        nueva_rutina = Rutina()

        #Colocamos propiedades
        print("Creamos una rutina")
        
        nueva_rutina.nombre = input("Ingrese el nombre de la rutina: ")
        nueva_rutina.ejercicio = input("Ingrese el ejercicio de la rutina: ")
        nueva_rutina.duracion = int(input("Ingrese la duracion de la rutina: "))

        #Las agregamos a la lista
        rutinas.append(nueva_rutina)

    elif opcion == 2:
        print("Vamos a ver las rutinas")
        print(rutinas)

    elif opcion == 3:
        print("Vamos a actualizar la rutina")


    elif opcion == 4:
        print("Vamos a eliminar una rutina")