'''
Programa que calcula el ritmo cardiaco
V0.1 Bryan Alejandro Avila Castro
Este programa calcula el ritmo cardíaco promedio después de varios minutos de ejercicio.
'''

def calcula_ritmo(minutos_ejercicio, ritmos_cardiacos):

    if len(ritmos_cardiacos) != minutos_ejercicio:
        print("Cuidado, los minutos de ejercicio no coinciden con el ritmo cardiaco.")

    suma = sum(ritmos_cardiacos)
    longitud = len(ritmos_cardiacos)
    dividir = suma/longitud

    return dividir, suma, longitud

promedio = calcula_ritmo(5, [70, 70, 70, 70, 70])
print("El ritmo cardiaco promedio es de: ", promedio)
