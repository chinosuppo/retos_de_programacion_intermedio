### Reto #35: BATALLA POKÉMON ###

"""
Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
 * La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
 * El programa recibe los siguientes parámetros:
    - Tipo del Pokémon atacante.
    - Tipo del Pokémon defensor.
    - Ataque: Entre 1 y 100.
    - Defensa: Entre 1 y 100.
"""

import random

def batalla(pokemon_atacante, pokemon_defensor):
    pokemon_atacante = pokemon_atacante.lower()
    pokemon_defensor = pokemon_defensor.lower()
    ataque = random.choice(range(1,101))
    defensa = random.choice(range(1,101))
    if (pokemon_atacante == 'agua' and pokemon_defensor == 'agua','planta' or pokemon_atacante == 'fuego' and pokemon_defensor == 'fuego', 'agua' or pokemon_atacante == 'planta' and pokemon_defensor == 'planta', 'fuego' or pokemon_atacante == 'electrico' and pokemon_defensor == 'electrico', 'planta'):
        efectividad = 0.5
        danio = 50 * (ataque/defensa) * efectividad
    
    elif (pokemon_atacante == 'fuego', 'agua', 'planta' and pokemon_defensor == 'electrico' or pokemon_atacante == 'electrico' and pokemon_defensor == 'fuego'):
        efectividad = 1
        danio = 50 * (ataque/defensa) * efectividad
    
    elif (pokemon_atacante == 'fuego' and pokemon_defensor == 'planta' or pokemon_atacante == 'agua' and pokemon_defensor == 'fuego' or pokemon_atacante == 'planta', 'electrico' and pokemon_defensor == 'agua'):
        efectividad = 2
        danio = 50 * (ataque/defensa) * efectividad
    return round(danio,2)

pokemon_atacante = input("Ingrese un tipo de pokemon (puede ser agua, fuego, planta o electrico): ")
pokemon_defensor = input("Ingrese un tipo de pokemon (puede ser agua, fuego, planta o electrico): ")    

print(batalla(pokemon_atacante,pokemon_defensor))