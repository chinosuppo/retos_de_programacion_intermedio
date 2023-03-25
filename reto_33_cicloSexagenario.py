### Reto #33: CICLO SEXAGENARIO CHINO ###

"""
Enunciado: Crea un función, que dado un año, indique el elemento  y animal correspondiente en el ciclo sexagenario del zodíaco chino.
 * El ciclo sexagenario se corresponde con la combinación de los elementos madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
 conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo (en este orden).
 * Cada elemento se repite dos años seguidos.
 * El último ciclo sexagenario comenzó en 1984 (Madera Rata).
"""

def ciclo_sexagenario(anio):
    elementos = ("madera", "fuego", "tierra", "metal", "agua")
    animales = ("rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo")
    elemento_actual = elementos[(anio - 4) % 10 // 2]
    animal_actual = animales[(anio - 4) % 12]
    return f"En el {anio} el zodiaco chino es: {elemento_actual} {animal_actual}"

print(ciclo_sexagenario(2023)) # agua conejo
print(ciclo_sexagenario(1993)) # agua gallo
print(ciclo_sexagenario(1988)) # tierra dragón