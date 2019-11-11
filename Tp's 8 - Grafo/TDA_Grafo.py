
class NodoArista():
    info = None
    sig = None
    peso = None

    def __str__(self):
        return "Info: " + str(self.info) + "Sig: " + str(self.sig)


class Arista():
    def __init__(self):
        self.tamanio = 0
        self.inicio = None


class NodoVertice():
    info = None
    sig = None
    arista = Arista()

    def __str__(self):
        return "Info: " + str(self.info) + "Sig: " + str(self.sig)


class Grafo():
    def __init__(self):
        self.tamanio = 0
        self.inicio = None


def insertar_vertice(g, dato, campo=0):
    campo = int(campo)
    nodo = NodoVertice()
    nodo.info = dato
    if (g.inicio is None) or (nodo.info[campo] < g.inicio.info[campo]):  # Si esta vacia o es el primero
        nodo.sig = g.inicio
        g.inicio = nodo
    else:  # Si va al medio o a lo ultimo
        anterior = g.inicio
        actual = g.inicio.sig
        while (actual is not None) and (actual.info[campo] <= nodo.info[campo]):
            actual = actual.sig
            anterior = anterior.sig
        nodo.sig = actual
        anterior.sig = nodo
    g.tamanio += 1
