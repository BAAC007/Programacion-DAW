'''
Caracteristicas de los objetos
V0.1 Bryan Alejandro Avila Castro
Este ejercicio se prueba el uso de assert 
'''

edad = 17

try:
    assert edad >= 18, "Error."
    print("Puedes viajar.")
    
except AssertionError:
    print("Eres menor de edad, no puedes viajar.")