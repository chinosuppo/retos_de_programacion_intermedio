### Reto #28: MÁQUINA EXPENDEDORA ###

"""
Simula el funcionamiento de una máquina expendedora creando una operación que reciba dinero (array de monedas) y un número que indique la selección del producto.
 * El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor número de monedas).
 * Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje y retornar todas las monedas.
 * Si no hay dinero de vuelta, el array se retornará vacío.
 * Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
 * Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""

def maquina_expendedora(dinero, producto):
    productos = {
        1: {"nombre": "Coca-Cola", "precio": 150},
        2: {"nombre": "Sprite", "precio": 150},
        3: {"nombre": "Fanta", "precio": 150},
        4: {"nombre": "Agua", "precio": 50},
        5: {"nombre": "Huevo Kinder", "precio": 300},
        6: {"nombre": "Papas Lays", "precio": 200},
        7: {"nombre": "Galletitas Oreo", "precio": 125},
        8: {"nombre": "Galletitas Sonrisa", "precio": 100},
        9: {"nombre": "Barra de cereal", "precio": 75},
        10: {"nombre": "Alfajor Minitorta", "precio": 250},
    }
    
    monedas_validas = [5, 10, 50, 100, 200] # Se podria realizar una tupla para que esta lista sea inmutable
    
    dinero_ingresado = dinero
    
    if producto not in productos:
        return "El producto que usted ingreso no se encuentra. Retire su dinero", dinero
    elif dinero_ingresado < productos[producto]["precio"]:
        return "El dinero ingresado es insuficiente. Retire su dinero", dinero
    else:
        cambio = dinero_ingresado - productos[producto]["precio"]
        cambio_devuelto = []
        for moneda in monedas_validas:
            while cambio >= moneda and moneda in dinero:
                cambio -= moneda
                cambio_devuelto.append(moneda)
                dinero.remove(moneda)
        if cambio == 0:
            return productos[producto]["nombre"], cambio_devuelto
        else:
            dinero.extend(cambio_devuelto)
            return "No hay monedas para devolver. Retire su dinero", []
        

print(maquina_expendedora(250, 2))