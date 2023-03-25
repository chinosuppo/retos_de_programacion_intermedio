### Reto #1: ¿ES UN ANAGRAMA? ###

"""
Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
"""

def es_anagrama(palabra_uno, palabra_dos):
    if palabra_uno.lower() == palabra_dos.lower():
        return False
    return sorted(palabra_uno.lower()) == sorted(palabra_dos.lower())

print(es_anagrama('Amor', 'Lola')) # False
print(es_anagrama('Amor', 'amor')) # False
print(es_anagrama('Amor', 'Roma')) # True