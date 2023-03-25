### Reto #34: LOS NÚMEROS PERDIDOS ###

"""
Enunciado: Dado un array de enteros ordenado y sin repetidos,  crea una función que calcule y retorne todos los que faltan entre el mayor y el menor.
 * Lanza un error si el array de entrada no es correcto.
"""

def numeros_perdidos(array):
    array = set(array)
    array = list(array)
    array.sort()
    # print(array)
    menor_valor = array[0]
    mayor_valor = array[-1]
    numeros = list(range(menor_valor, mayor_valor))
    for numero in numeros:
        if numero not in array:
            print (numero)
        
             
array = [3,4,5,6,2,2,3,4,77,8,5]
numeros_perdidos(array)