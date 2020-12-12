import random
from math import sqrt

class NodoCola():
    info, sig = None, None


class Cola():

    def __init__(self):
        self.tamanio = 0
        self.frente = None
        self.final = None


def arribo(cola, dato):
    """Inserta elemento a final de la cola"""
    nuevo = NodoCola()
    nuevo.info = dato

    if (cola.final is None):
        cola.frente = nuevo
    else:
        cola.final.sig = nuevo
    cola.final = nuevo
    cola.tamanio += 1


def atencion(cola):
    """Devuelve el primer el elemento de la cola, eliminandolo"""
    dato = cola.frente.info
    cola.frente = cola.frente.sig

    if (cola.frente is None):
        cola.final = cola.frente

    cola.tamanio -= 1
    return dato


def tamanio(cola):
    """Tamaño de la cola"""
    return cola.tamanio


def cola_vacia(cola):
    """Devuelve true si cola esta vacia"""
    return (tamanio(cola) == 0)


def cola_llena(cola):
    """Devuelve true si cola está llena"""
    return False


def moverAFinal(cola):
    if (cola.tamanio > 0):
        cola.final.sig = cola.frente
        cola.final = cola.frente
        cola.frente = cola.frente.sig
        cola.final.sig = None


def colaToList(cola):
    ''' Devuelve los nodos que se encuentran en la cola, para poder recorrerlos y mostrar los
    datos de una forma más sencilla. Se usa en TDA_Arbol para transformada'''
    nodos = []
    if tamanio(cola) > 0:
        nodo = cola.frente
        while nodo:
            nodos.append(nodo.info)
            nodo = nodo.sig
    return nodos



def barridoC(cola):
    if tamanio(cola) > 0:
        nodo = cola.frente
        while nodo:
            print(nodo.info)
            nodo = nodo.sig


def en_frente(cola):
    if tamanio(cola) > 0:
        return cola.frente.info


def cargaAutoIntC(cola, cant):
    for i in range(0, cant):
        arribo(cola, random.randint(-10, 10))


def cargaAutoStrC(cola, cant):
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, cant):
        arribo(cola, random.choice(abc))