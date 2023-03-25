### Reto #3: ¿ES UN NÚMERO PRIMO? ###

"""
Escribe un programa que se encargue de comprobar si un número es o no primo. Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime(n):
    if n > 1: # el 1 es ignorado
        for i in range (2, int(n/2)+1):
            if(n % i) == 0:
                return False
        else:
            return True
    else:
        return("NUMERO INCORRECTO")

print(is_prime(13)) # True
print(is_prime(10)) # False
print(is_prime(-8)) # Numero incorrecto