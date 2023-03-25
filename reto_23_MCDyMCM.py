### Reto #23: MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO ###

"""
Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def mcd(num_1, num_2):
    for i in range(1,1001):
        if (num_1 % i == 0 and num_2 % i == 0):
            divisor = []
            divisor.append(i)
    return divisor


print(mcd(100,98))
            

def mcm(num_1, num_2):
    rango = max(num_1,num_2)
    while True:
        if (rango % num_1 == 0) and (rango % num_2 == 0):
            return rango
        
        rango += 1

print(mcm(12,8))