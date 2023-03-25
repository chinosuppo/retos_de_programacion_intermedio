### Reto #12: ¿ES UN PALÍNDROMO? ###

"""
Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos. Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda. NO se tienen en cuenta los espacios, signos de puntuación y tildes. Ejemplo: Ana lleva al oso la avellana.
"""

def esPalindromo(texto):
    # eliminar caracteres no deseados
    texto = texto.lower().replace(" ", "").replace(",","").replace(".","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    
    if texto == texto[::-1]:
        return True
    else:
        return False
    
print(esPalindromo('Ana lleva al oso la avellana')) # True
print(esPalindromo('Python')) # False