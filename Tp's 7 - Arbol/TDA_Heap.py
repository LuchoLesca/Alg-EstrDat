import random


class Heap():
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None]*tamanio


def agregar(heap, dato):
    '''Agrega elemento y flota hasta ordenar heap'''
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1


def quitar(heap):
    '''Quita primer elemento y reordena heap'''
    primer_elemento = heap.vector[0]
    heap.vector[0], heap.vector[heap.tamanio-1] = heap.vector[heap.tamanio-1], heap.vector[0]
    heap.tamanio -= 1
    hundir(heap, 0)
    return primer_elemento


def flotar(heap, indice):
    """Flota el elemento en la posicion del indice"""
    padre = (indice-1)//2
    while (padre >= 0) and (heap.vector[padre] > heap.vector[indice]):
        heap.vector[padre], heap.vector[indice] = heap.vector[indice], heap.vector[padre]
        indice = padre
        padre = (padre - 1) // 2


def hundir(heap, indice):
    """Hunde el elemento en la posicion del indice"""

    # hi = Hijo izquierdo
    hi = (2 * indice) + 1
    control = True

    while (hi < heap.tamanio - 1) and control:
        # Ve cual de los hijos es mayor
        menor = hi
        # hd = Hijo derecho
        hd = hi + 1
        if (hd <= heap.tamanio - 1) and (heap.vector[hd] < heap.vector[hi]):
            menor = hd
        # Intercambio con el hijo que haya sido el mayor
        if (heap.vector[indice] < heap.vector[menor]):
            heap.vector[indice], heap.vector[menor] = heap.vector[menor], heap.vector[indice]
        # Si ningun hijo de mayor, termina de hundir
        else:
            control = False

        hi = (2 * menor) + 1


def atencion_H(heap):
    '''Elimina y devuelve primer elemento en cola de prioridad'''
    aux = quitar(heap)
    return aux


def arribo_H(heap, dato, prioridad=0):
    '''Agrega dato a cola de prioridad heap'''
    agregar(heap, [dato, prioridad])


"""
def ordenarHeap(heap):
    '''Ordena el heap'''
    for i in range(heap.tamanio):
        flotar(heap, i)
"""

"""
def heapSort(heap):
    '''Metodo de ordenamiento monticulo'''
    aux = heap.tamanio
    for i in range(0, heap.tamanio-1):
        quitar(heap)
    heap.tamanio = aux
"""


def monticulizar(lista):
    '''Convierte lista en montículo'''
    heap_aux = Heap(len(lista))
    for elemento in lista:
        arribo_H(heap_aux, lista.pop())
    return heap_aux


def heap_vacio(heap):
    return heap.tamanio == 0


def buscar_H(heap, dato):
    if dato in heap:
        return heap.index(dato)
    else:
        return None


def barridoMonticulo(heap):
    for i in range(heap.tamanio):
        print(heap.vector[i])


lala = [2, 45, 1, 15, 18, 99, 0, 233, 57]
mont = Heap(100)

for i in range(len(lala)):
    arribo_H(mont, lala[i])

barridoMonticulo(mont)
