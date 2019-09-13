import random
import math


class NodoLista():

    info, sig, ant = None, None, None


class Lista():

    def __init__(self):
        self.tamanio = 0
        self.inicio = None


def insertar(l, dato):
    """Inserta en lista, elemento deseado"""
    nodo = NodoLista()
    nodo.info = dato

    if (l.inicio is None) or (nodo.info < l.inicio.info):  # Si está vacía o es el primero
        nodo.sig = l.inicio
        l.inicio = nodo
    else:  # Si va al medio o a lo último
        anterior = l.inicio
        actual = l.inicio.sig
        while (actual is not None) and (actual.info <= nodo.info):
            actual = actual.sig
            anterior = anterior.sig
        nodo.sig = actual
        anterior.sig = nodo
    l.tamanio += 1


def inserCampo(l, dato, i):  # Para manejo con array
    nodo = NodoLista()
    nodo.info = dato

    if (l.inicio is None) or (nodo.info[i] < l.inicio.info[i]):  # Si está vacía o es el primero
        nodo.sig = l.inicio
        l.inicio = nodo
    else:  # Si va al medio o a lo último
        anterior = l.inicio
        actual = l.inicio.sig
        while (actual is not None) and (actual.info[i] <= nodo.info[i]):
            actual = actual.sig
            anterior = anterior.sig
        nodo.sig = actual
        anterior.sig = nodo
    l.tamanio += 1


def insertarEn(l, dato, pos):
    '''Inserta elemento en posicion deseada, dentro de rango del lista'''
    nodo = NodoLista()
    nodo.info = dato

    aux = l.inicio

    if (pos >= 0) and (pos <= l.tamanio):
        if (pos == 0):
            nodo.sig = l.inicio
            l.inicio = nodo
        elif (pos < l.tamanio):
            for i in range(1, pos):
                aux = aux.sig
            nodo.sig = aux.sig
            aux.sig = nodo
        else:
            while aux.sig is not None:
                aux = aux.sig
            aux.sig = nodo
        l.tamanio += 1
    else:
        print("El indice " + str(pos) + " excede el tamaño de elementos que ")
        print("posee la lista")


def eliminar(l, dato):
    """Elimina de la lista, el primer elemento deseado"""
    out = None
    if (l.inicio.info == dato):
        out = l.inicio.info
        l.inicio = l.inicio.sig
        l.tamanio -= 1
    else:
        anterior = l.inicio
        actual = anterior.sig

        while (actual is not None) and (actual.info < dato):  # Todo esto teniendo en cuenta que la lista va a estar ordenada
            actual = actual.sig
            anterior = anterior.sig

        if (actual is not None) and (actual.info == dato):  # Si el elemento no estaba al final de la lista
            out = actual.info                           # Y lo encontré
            anterior.sig = actual.sig
            l.tamanio -= 1

    return out


def eliminarCampo(lista, dato, campo):  # Para manejo con array

    if (lista.inicio.info[campo] == dato):
        while lista.inicio.info[campo] == dato:
            lista.inicio = lista.inicio.sig
            lista.tamanio -= 1
    else:
        anterior = lista.inicio
        actual = anterior.sig

        while (actual is not None) and (actual.info[campo] < dato):
            actual = actual.sig
            anterior = anterior.sig

        if (actual is not None) and (actual.info[campo] == dato):
            while actual.info[0] == dato:
                anterior.sig = actual.sig
                actual = anterior.sig
                lista.tamanio -= 1


def eliminarTodos(l, dato):
    """Elimina de la lista toda las ocurrencias del dato ingresado"""
    if (l.inicio.info == dato):
        l.inicio = l.inicio.sig
        l.tamanio -= 1
    else:
        anterior = l.inicio
        actual = anterior.sig

        while (actual is not None) and (actual.info < dato):  # Todo esto teniendo en cuenta que la lista va a estar ordenada
            actual = actual.sig
            anterior = anterior.sig

        if actual is not None:
            while (actual is not None) and (actual.info == dato):
                actual = actual.sig
                l.tamanio -= 1
            anterior.sig = actual


def barridoLista(l):
    """Barrido de lista, imprimiendo en pantalla el elemento de cada nodo"""
    aux = l.inicio
    while (aux is not None):
        print(str(aux.info))
        aux = aux.sig


def busquedaLista(l, buscado):
    """Devuelve dirección de memoria. None si no se encontró lo buscado"""
    aux = l.inicio
    while (aux is not None) and (aux.info != buscado):
        aux = aux.sig

    return aux


def busquedaListaCampo(l, buscado, campo):  # Para manejo con array
    '''Devuelve el puntero de elemento buscado por campo ingresado'''
    aux = l.inicio
    while (aux is not None) and (aux.info[campo] < buscado):
        aux = aux.sig
    if (aux is not None) and (aux.info[campo] != buscado):
        aux = None
    return aux


def busqueda(l, buscado, campo):  # Sirve cuando no está ordenado por el campo que se necesita buscar
    '''Realiza un barrido completo de la lista, buscando dato en campo especificado'''
    aux = l.inicio
    while (aux is not None) and (aux.info[campo] != buscado):
        aux = aux.sig
    return aux


def lista_vacia(l):
    return l.tamanio == 0


def cargaAutoIntL(l, cantidad):
    """Carga en lista, cantidad ingresada de numeros random"""
    for i in range(0, cantidad):
        insertar(l, random.randint(-50, 50))


def cargaAutoStrL(l, cantidad):
    """Carga en lista, cantidad ingresada de letras random"""
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, cantidad):
        insertar(l, random.choice(abc))


def ultimoNodo(lista):
    aux = lista.inicio

    while (aux.sig is not None):
        aux = aux.sig

    return aux


def copiarLista(l):
    '''Crea y devuelve una lista de la lista introducida'''
    lista = Lista()

    aux = l.inicio
    while (aux is not None):
        insertar(lista, aux.info)
        aux = aux.sig

    return lista


def concatenar(l1, l2):
    '''Devuelve lista nueva, con datos de l1 seguidos de los de l2'''
    lista = copiarLista(l1)

    aux = lista.inicio

    while (aux.sig is not None):
        aux = aux.sig

    aux.sig = l2.inicio
    lista.tamanio += l2.tamanio

    return lista


def union(l1, l2):
    '''Devuelve una lista con la union de las dos ingresadas'''
    l3 = Lista()

    aux = l1.inicio
    while (aux is not None):
        if (busquedaLista(l3, aux.info) is None):
            insertar(l3, aux.info)

        aux = aux.sig

    aux = l2.inicio
    while (aux is not None):
        if (busquedaLista(l3, aux.info) is None):
            insertar(l3, aux.info)

        aux = aux.sig

    return l3


def interseccion(l1, l2):
    '''Devuelve una lista intersección de las listas ingresadas'''
    l3 = Lista()

    aux = l1.inicio
    while (aux is not None):
        if (busquedaLista(l2, aux.info) is not None) and (busquedaLista(l3, aux.info) is None):
            insertar(l3, aux.info)

        aux = aux.sig

    return l3


def primo(num):
    pri = True
    if num < 2 and num != 0:
        return True
    elif num == 2:
        return True
    else:
        i = 2
        while (i <= math.sqrt(num)) and pri:
            if (i != num) and (num % i == 0):
                pri = False
            i += 1
        return pri
