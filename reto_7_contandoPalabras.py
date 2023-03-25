### Reto #7: CONTANDO PALABRAS ###

"""
Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * Los signos de puntuación no forman parte de la palabra.
 * Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""

texto = input('Introduce un texto: ')
palabras = texto.lower().split()
contador = {}

for palabra in palabras:
    palabra = palabra.strip(".,;:!¿?¡()[]{}")
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
        
for palabra, count in contador.items():
    print(f"{palabra}: {count}")
    
