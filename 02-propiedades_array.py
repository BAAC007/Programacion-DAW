#las propiedades son como las variables pero dentro de una clase
#los telefonos deben estar en un array
class Cliente():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = []

#ahora instancio un nuevo objeto

cliente1 = Cliente()

#ahora le escribo una propiedad

cliente1.nombre = "Bryan Avila"

print("El nombre del cliente es: ", cliente1.nombre)

cliente1.telefonos.append("6225789")
cliente1.telefonos.append("2124206")

cliente1.telefonos.pop(0)
print(cliente1.telefonos)