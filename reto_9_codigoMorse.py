### Reto #9: CÓDIGO MORSE ###

"""
Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
"""

diccionario_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "CH": "----",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "\"": ".-..-.",
    "@": ".--.-.",
    "=": "-...-",
    "!": "−.−.−−",
}

def plano_a_morse(caracter):
    if caracter in diccionario_morse:
        return diccionario_morse[caracter]
    else:
        return ""

def codificacion_morse(texto_plano):
    texto_plano = texto_plano.lower()
    morse = ""
    for caracter in texto_plano:
        caracter_codificado = plano_a_morse(caracter)
        morse += caracter_codificado + " "
    return morse

def morse_a_plano(morse):
    for caracter in diccionario_morse:
        if diccionario_morse[caracter] == morse:
            return caracter
    return ""

def codificador_plano(morse):
    texto_plano = ""
    for caracter_morse in morse.split(" "):
        caracter_plano = morse_a_plano(caracter_morse)
        texto_plano += caracter_plano
    return texto_plano

