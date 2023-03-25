### Reto #25: PIEDRA, PAPEL, TIJERA ###

"""
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 * El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * La función recibe un listado que contiene pares, representando cada jugada.
 * El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 * Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""

import random

def piedra_papel_tijera(humano):
        if (not(humano.lower() in ["piedra", "papel", "tijera"])):
            return "No se puede comenzar el juego si usted no elige una opción correcta"
        compu = random.choice(["piedra", "papel", "tijera"])
        if humano == compu:
            return "Empate"
        else:
            if((humano=="piedra" and compu=="tijera") or (humano=="papel" and compu=="piedra") or (humano=="tijera" and compu=="papel")):
                return "Gano humano"
            else:
                return "Gano PC"
        

print(piedra_papel_tijera("tijera"))