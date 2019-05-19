import random

max = 10


class Cola():

    def __init__(self):
        self.datos = []
        for i in range(0, max):
            self.datos.append(None)

        self.frente = 0
        self.final = -1
        self.tamanio = 0


def arribo(cola, dato):  # Insertar
    cola.tamanio += 1
    cola.final += 1
    cola.datos[cola.final] = dato

    if (cola.final == max - 1):  # Arregla el problema del desbordamiento
        cola.final = -1          # del índice


def atencion(cola):  # Quitar
    cola.tamanio -= 1
    dato = cola.datos[cola.frente]
    cola.frente += 1

    if (cola.frente == max):
        cola.frente = 0

    return dato


def cola_vacia(cola):
    return (cola.tamanio == 0)


def cola_llena(cola):
    return (cola.tamanio == max)


def moverAFinal(cola):
    if (cola.tamanio > 0):
        arribo(cola, atencion(cola))


def barrido2(cola):
    for i in range(0, cola.tamanio):
        dato = atencion(cola)
        print(dato)
        arribo(cola, dato)


"""
def barrido(cola):
    cola2 = Cola()
    while not cola_vacia(cola):
        dato = atencion(cola)
        print(dato)
        arribo(cola2, dato)

    cola = cola2
"""


def cargaAutoIntC(cola):
    while not cola_llena(cola):
        arribo(cola, random.randint(0, 100))


def cargaAutoStrC(cola):
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while (not cola_llena(cola)):
        arribo(cola, random.choice(abc))


def primo(num):
    pri = True
    if num < 2:
        return True
    elif num == 2:
        return True
    else:
        i = 2
        while (i < num) and pri:
            if (num % i == 0):
                pri = False
            i += 1
        return pri
