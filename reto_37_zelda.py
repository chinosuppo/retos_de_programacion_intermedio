### Reto #37: LOS LANZAMIENTOS DE "THE LEGEND OF ZELDA” ###

"""
Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023. Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos "The Legend of Zelda" de la historia?
Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda que tú selecciones.
 * Debes buscar cada uno de los títulos y su día de lanzamiento  (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
"""

import datetime

diccionario_zelda = {
    "juego_1": {
        "nombre": "The Legend of Zelda",
        "fecha": datetime.datetime(1986, 2, 21)
    },
    "juego_2": {
        "nombre": "The Adventure of Link",
        "fecha": datetime.datetime(1987, 1, 14)
    },
    "juego_3": {
        "nombre": "A Link to the Past",
        "fecha": datetime.datetime(1991, 11, 21)
    },
    "juego_4": {
        "nombre": "Link's Awakening",
        "fecha": datetime.datetime(1993, 6, 6)
    },
    "juego_5": {
        "nombre": "Ocarina of Time",
        "fecha": datetime.datetime(1998, 11, 21)
    },
    "juego_6": {
        "nombre": "Majora's Mask",
        "fecha": datetime.datetime(2000, 4, 27)
    },
    "juego_7": {
        "nombre": "Oracle of Seasons y Oracle of Ages",
        "fecha": datetime.datetime(2001, 2, 27)
    },
    "juego_8": {
        "nombre": "The Wind Waker",
        "fecha": datetime.datetime(2002, 12, 13)
    },
    "juego_9": {
        "nombre": "A Link to the Past / Four Swords",
        "fecha": datetime.datetime(2003, 3, 14)
    },
    "juego_10": {
        "nombre": "Four Swords Adventures",
        "fecha": datetime.datetime(2004, 3, 18)
    },
    "juego_11": {
        "nombre": "The Minish Cap",
        "fecha": datetime.datetime(2004, 11, 4)
    },
    "juego_12": {
        "nombre": "Twilight Princess",
        "fecha": datetime.datetime(2006, 12, 2)
    },
    "juego_13": {
        "nombre": "Phantom Hourglass",
        "fecha": datetime.datetime(2007, 6, 23)
    },
    "juego_14": {
        "nombre": "Spirit Tracks",
        "fecha": datetime.datetime(2009, 12, 23)
    },
    "juego_15": {
        "nombre": "Skyward Sword",
        "fecha": datetime.datetime(2011, 11, 23)
    },
    "juego_16": {
        "nombre": "A Link Between Worlds",
        "fecha": datetime.datetime(2013, 12, 26)
    },
    "juego_17": {
        "nombre": "Tri Force Heroes",
        "fecha": datetime.datetime(2015, 10, 22)
    },
    "juego_18": {
        "nombre": "Breath of the Wild",
        "fecha": datetime.datetime(2017, 3, 3)
    },
    "juego_19": {
        "nombre": "Tears of the Kingdom",
        "fecha": datetime.datetime(2023, 5, 12)
    },
}

diferencia = diccionario_zelda["juego_12"]["fecha"] - diccionario_zelda["juego_5"]["fecha"]
print(diferencia)