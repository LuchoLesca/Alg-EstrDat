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
    return quitar(heap)


def arribo_H(heap, dato, prioridad=0):
    '''Agrega dato a cola de prioridad heap'''
    agregar(heap, [dato, prioridad])


def heapSort(heap):
    '''Metodo de ordenamiento monticulo'''
    aux = heap.tamanio
    for i in range(0, heap.tamanio):
        quitar(heap)
    heap.tamanio = aux


def monticulizar(lista):
    '''Convierte lista en montículo(la ordena como si fuese uno)'''
    for i in range(len(lista)):
        flotar(lista, i)


def heap_vacio(heap):
    return heap.tamanio == 0


def heap_lleno(heap):
    return heap.tamanio == len(heap.vector)


def cambiarPrioridad(heap, indice, prioridad):
    """Cambia la prioridad de un elemento y lo acomoda en el montículo."""
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if(prioridad < prioridad_anterior):
        flotar(heap, indice)
    elif(prioridad > prioridad_anterior):
        hundir(heap, indice)


def buscar_H(heap, buscado):
    pos = -1
    for i in range(len(heap.vector)):
        if heap.vector[i][1][0].info == buscado:
            pos = i
    return pos


def barridoMonticulo(heap):
    for i in range(heap.tamanio):
        print(heap.vector[i])
