class NodoLista():
    info, sig = None, None

class Lista():

    def __init__(self):
        self.tamanio = 0
        self.inicio = None

def insertar(l, dato):
    nodo = NodoLista()
    nodo.info = dato

    if l.inicio == None or (nodo.info < l.info.inicio):  # Si está vacía o es el primero
        nodo.sig = l.inicio
        l.inicio = nodo
    else:  # Si va al medio o a lo último
        actual = l.inicio.sig
        anterior = l.inicio
        while (actual != None) and (actual.info <= nodo.info):
            actual = actual.sig
            anterior = anterior.sig
        nodo.sig = actual
        anterior.sig = nodo
    l.tamanio += 1


def eliminar(l, clave):
    if (l.tamanio == 1):
        dato = l.inicio.info.clave
        l.inicio = None
    else:
        dato = None
        actual = l.inicio.sig
        anterior = l.inicio
        while (actual != None) and (actual.info.clave != clave):

            actual = actual.sig
            anterior = anterior.sig
