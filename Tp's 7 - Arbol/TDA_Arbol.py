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


def rotacionSimple(raiz, control):  # Si es true rota a la der, sino izq
    '''Realiza rotacion simple'''
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
    '''Realiza rotacion doble'''
    if control:                    # nombre si es izquierda o derecha
        raiz.izq = rotacionSimple(raiz.izq, False)
        raiz = rotacionSimple(raiz, True)
    else:
        raiz.der = rotacionSimple(raiz.der, True)
        raiz = rotacionSimple(raiz, False)

    return raiz


def balancear(raiz):
    '''Balancea el arbol'''
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
    '''Inserta el elemento en el arbol'''
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
    '''Devuelve el nodo donde encontró la info buscada'''
    aux = None
    if (raiz is not None):
        if (raiz.info == buscado):
            aux = raiz
        else:
            if (buscado < raiz.info):
                aux = busqueda(raiz.izq, buscado)
            else:
                aux = busqueda(raiz.der, buscado)
    return aux


def busquedaProximidad(raiz, buscado):  # o clave
    '''Devuelve el nodo donde encontró la info buscada'''
    aux = None
    if (raiz is not None):
        if (buscado in raiz.info):
            aux = raiz
        else:
            if (buscado < raiz.info):
                aux = busqueda(raiz.izq, buscado)
            else:
                aux = busqueda(raiz.der, buscado)
    return aux


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
        postorden(raiz.izq)
        postorden(raiz.der)
        print(raiz.info)


def invInorden(raiz):
    if raiz is not None:
        invInorden(raiz.der)
        print(raiz.info)
        invInorden(raiz.izq)


def reemplazar(raiz):  # Va hasta la derecha, hasta que no tenga raiz derecha
    aux = None         # Encontro el mas gande los menores (porque entro por
    if (raiz.der is not None):  # raiz izquierda)
        raiz.der, aux = reemplazar(raiz.der)
    else:
        aux = raiz  # Toma la info del elemento e indexa la raiz con la raiz
        raiz = raiz.izq  # izquierda y elimina la conexión con esa hoja
    return(raiz, aux)


def eliminar(raiz, clave):  # Si devuleve None es porque no encontro nada
    x = None
    if (raiz is not None):  # Mientras no llegue a hoja, se llama recursivament
        if (raiz.info > clave):  # Si buscado es menor, recursivo para izquierd
            raiz.izq, x = eliminar(raiz.izq, clave)
        else:  # Si es mayor o igual
            if(raiz.info < clave):  # Si es mayor, recursivo a derecha
                raiz.der, x = eliminar(raiz.der, clave)
            else:  # Si es igual
                if (raiz.izq is None):  # Si no tiene rama izquierda
                    x = raiz.info       # Saca info y enlaza con única rama
                    raiz = raiz.der     # hijo. En este caso, derecha
                else:  # Si tiene rama izquierda
                    if(raiz.der is None):  # Si no tiene rama derecha
                        x = raiz.info      # obtiene dato y enlaza con unica
                        raiz = raiz.izq    # rama hijo, en este caso, derecha
                    else:  # Si tiene ambas ramas
                        raiz.izq, aux = reemplazar(raiz.izq)  # Busca de los número mas chicos, la hoja con el valor más alto
                        raiz.info = aux.info  # Reemplaza el valor de ese nodo por el de la hoja que trajo
    return(raiz, x)


def nodoMin(raiz):
    aux = raiz
    while aux.izq is not None:
        aux = aux.izq
    return aux


def nodoMax(raiz):
    aux = raiz
    while aux.der is not None:
        aux = aux.der
    return aux


def pesoArbol(raiz):
    '''Cantidad de nodos en el arbol'''
    if raiz is not None:
        return 1 + pesoArbol(raiz.izq) + pesoArbol(raiz.der)
    else:
        return 0


def cantidadHojas(raiz):
    '''Cantidad de hojas en el arbol'''
    if raiz is not None:
        if (raiz.izq is None) and (raiz.der is None):
            return 1
        else:
            return cantidadHojas(raiz.izq) + cantidadHojas(raiz.der)
    else:
        return 0


"""def nodosEnNivel(raiz, nivel, cont=0):
    nivel -= 1
    while nivel >= 0:
"""


def nodosEnAltura(raiz, altura):
    '''Cantidad de nodos en altura seleccionada'''
    if raiz is not None and raiz.altura >= altura:
        if raiz.altura == altura:
            return 1 + nodosEnAltura(raiz.izq, altura) + nodosEnAltura(raiz.der, altura)
        else:
            return 0 + nodosEnAltura(raiz.izq, altura) + nodosEnAltura(raiz.der, altura)
    else:
        return 0


def imprimirArbol(raiz, espacios=0):
    ''' Imprime arbol, girado hacia la izquierda'''
    if raiz is not None:
        espacios += 5
        imprimirArbol(raiz.der, espacios)
        print(" " * espacios, str(raiz.info))
        imprimirArbol(raiz.izq, espacios)


def esHoja(raiz):
    if (raiz.izq is None) and (raiz.der is None):
        return True


'''
diccionario = {padre, lista_de_hijos}
'''
