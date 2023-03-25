### Reto #38: BINARIO A DECIMAL ###

"""
Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for numero in binario:
        multiplicador = 2**posicion
        decimal += int(numero) * multiplicador
        posicion += 1
    return decimal


binario = input("Ingrese un numero binario: ")
decimal = binario_a_decimal(binario)
print(f"El numero {binario} en el sistema decimal es {decimal}")
