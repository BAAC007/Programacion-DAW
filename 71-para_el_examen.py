#CRUD en python (No SQL)

#Trabajaremos con clases

#1-.Presentará una pantalla de bienvenida
#2-.Ofrecerá al usuario 4 opciones (Crear, leer, actualizar, eliminar)
#3-.Habrá que definir una clase en base a una entidad que os proporcionare - no metodos set y get
#4-.Las entidades se guardarán como objetos en memoria
#5-.Las entidades persistirán en disco usando pickle


class Cliente():
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

