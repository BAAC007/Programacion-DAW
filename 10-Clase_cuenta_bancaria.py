class cuentaBancaria():
    def __init__(self):
        self.saldo = 0
        self.cliente = ""


#Defino setters y getters para el saldo
    def setSaldo(self,nuevosaldo):
        #Establezco una condición de que valida si el saldo nuevo es mayor que 1000 euros
        if nuevosaldo > self.saldo + 1000:
            #Si salta la alarma, avisa y NO cambia el saldo
            print("Voy a avisar a la entidad de un ingreso muy grande")
        else:
            #Si pasa el filtro, solo entonces se cambia el saldo
            self.saldo = nuevosaldo
    def getSaldo(self):
        return self.saldo

    def getSaldo(self):
        return self.saldo

cuentacliente1 = cuentaBancaria()
cuentacliente1.setSaldo(10000000000)
print(cuentacliente1.getSaldo())