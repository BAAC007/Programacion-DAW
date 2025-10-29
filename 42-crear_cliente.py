class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre=nuevonombre
        self.email=nuevoemail

clientes = []

clientes.append(Cliente("Bryan Avila", "info@alevila.com"))
clientes.append(Cliente("Bryan", "Bryan@Avila.com"))

print(clientes)