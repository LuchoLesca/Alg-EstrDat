from random import randint


class Nodoarbol():

    def __init__(self, dato):
        self.izq = None
        self.der = None
        self.altura = 0
        self.info = dato


def altura(raiz):
    if (raiz is None):
        return 0
    else:
        return raiz.altura


def actualizarAltura(raiz):
    if (altura(raiz.izq) > altura(raiz.der)):
        raiz.altura = altura(raiz.izq) + 1
    else:
        raiz.altura = altura(raiz.der) + 1
    return raiz


# Para balancear el arbol se hacen rotaciones, a la derecha y/o
# izquierda. simple o doble


def rotacionSimple(raiz, control):  # Si es true rota a la derecha, sino izquierdas
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz

    actualizarAltura(raiz)
    actualizarAltura(aux)
    raiz = aux

    return raiz


def rotacionDoble(raiz, control):  # La última rotación que se hace le da el
    if control:                    # nombre si es izquierda o derecha
        raiz.izq = rotacionSimple(raiz.izq, False)
        raiz = rotacionSimple(raiz, True)
    else:
        raiz.der = rotacionSimple(raiz.der, True)
        raiz = rotacionSimple(raiz, False)

    return raiz


def balancear(raiz):
    if (raiz is not None):
        if (altura(raiz.izq) - altura(raiz.der) == 2):  # El desbalance es izq
            if (altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotacionSimple(raiz, True)
            else:
                raiz = rotacionDoble(raiz, True)
        elif (altura(raiz.der) - altura(raiz.izq) == 2):  # El desbalancees der
            if (altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotacionSimple(raiz, False)
            else:
                raiz = rotacionDoble(raiz, False)

    return raiz


def insertar(raiz, dato):
    if (raiz is None):
        raiz = Nodoarbol(dato)
    else:
        if (dato < raiz.info):
            raiz.izq = insertar(raiz.izq, dato)
        else:
            raiz.der = insertar(raiz.der, dato)

    actualizarAltura(raiz)
    raiz = balancear(raiz)

    return(raiz)


def arbolVacio(raiz):
    return (raiz is None)


def busqueda(raiz, buscado):  # o clave
    pos = None
    if (raiz is not None):
        if (raiz.info == buscado):
            pos = raiz
        else:
            if (buscado < raiz.info):
                pos = busqueda(raiz.izq, buscado)
            else:
                pos = busqueda(raiz.der, buscado)
    return(pos)


def preorden(raiz):  # Va a servir para hacer una búsqueda más facilmente
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)


def reemplazar(raiz):
    aux = None
    if (raiz.der is not None):
        raiz.der, aux = reemplazar(raiz.der)
    else:
        aux = raiz
        raiz = raiz.izq
    return(raiz, aux)


def eliminar(raiz, clave):
    x = None
    if (raiz is not None):
        if (raiz.info > clave):
            raiz.izq, x = eliminar(raiz.izq, clave)
        else:
            if(raiz.info < clave):
                raiz.der, x = eliminar(raiz.der, clave)
            else:
                if (raiz.izq is None):
                    x = raiz.info
                    raiz = raiz.der
                else:
                    if(raiz.der is None):
                        x = raiz.info
                        raiz = raiz.izq
                    else:
                        raiz.izq, aux = reemplazar(raiz.izq)
                        raiz.info = aux.info
    return(raiz, x)
