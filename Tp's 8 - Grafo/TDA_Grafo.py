from TDA_Cola import Cola, arribo, atencion, cola_vacia
from TDA_Pila import Pila, apilar, desapilar
from TDA_Heap import Heap, arribo_H, atencion_H, heap_vacio, buscar_H, cambiarPrioridad
from math import inf


class Grafo():

    def __init__(self, dirigido=True):
        self.inicio = None
        self.tamanio = 0
        self.dirigido = dirigido


class Vertice():
    '''Crea un vertice con la información cargada'''
    def __init__ (self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = listaAristas()


class Arista():
    def __init__ (self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None


class listaAristas():
    '''Crea una lista de aristas (lista de lista) vacía'''
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


# INSERTAR/AGREGAR

def insertarVertice(grafo, dato):
    '''Inserta un vertice al grafo'''
    vertice = Vertice(dato)
    # Si el grafo está vacío o la info es menos que el primer elemento, lo inserta primero en la lista de vertices
    if (grafo.inicio is None) or (vertice.info < grafo.inicio.info):
        vertice.sig = grafo.inicio
        grafo.inicio = vertice
    else:
    # Sino, realiza un barrido secuencial en la lista de nodos hasta encontrarel lugar a ubicar
        act = grafo.inicio.sig
        ant = grafo.inicio
        
        while (act is not None) and (act.info <= vertice.info):
            act = act.sig
            ant = ant.sig
        
        vertice.sig = act
        ant.sig = vertice
    
    grafo.tamanio += 1


def agregarArista(lista_adyacentes, dato, destino):
    '''Agrega la arista a la lista de adyacentes del orígen.'''
    arista = Arista(dato, destino)
    # Si la lista de adyacentes está vacía o el valor destino es menor que el valo destino del primer elemento, coloca este nodo como primero
    if (lista_adyacentes.inicio is None) or (destino < lista_adyacentes.inicio.destino):
        arista.sig = lista_adyacentes.inicio
        lista_adyacentes.inicio = arista
    else:
    # Sino, realiza un barrido secuencial en la lista de nodos hasta encontrarel lugar a ubicar
        ant = lista_adyacentes.inicio
        act = lista_adyacentes.inicio.sig
        
        while(act is not None and act.destino < arista.destino):
            ant = act
            act = act.sig
        
        arista.sig = act
        ant.sig = arista

    lista_adyacentes.tamanio += 1


def insertarArista(grafo, dato, origen, destino):
    '''Si los vertices de origen y destino existen, insertar arista directamente'''
    ori = buscarVertice(grafo, origen)
    des = buscarVertice(grafo, destino)
    if (ori is not None) and (des is not None):
        if grafo.dirigido:
            agregarArista(ori.adyacentes, dato, des.info)
        else:
            agregarArista(ori.adyacentes, dato, des.info)
            agregarArista(des.adyacentes, dato, ori.info)


 # BUSQUEDAS

def buscarArista(vertice, buscado):
    '''Retorna el nodoArista con la info buscada, si la encuentra'''
    aux = vertice.adyacentes.inicio
    while (aux is not None) and (aux.destino != buscado):
        aux = aux.sig
    return aux


def buscarVertice(grafo, buscado):
    '''Retorna el nodoVertice con la info buscada, si la encuentra'''
    aux = grafo.inicio
    while (aux is not None) and (aux.info != buscado):
        aux = aux.sig
    return aux


# BARRIDOS

def barridoProfundidad(grafo, vertice):
    '''Barrido en profundiad del grafos'''
    marcarNoVisitado(grafo)
    
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            
            while adyacentes is not None:
                aux_adyacente = buscarVertice(grafo, adyacentes.destino)
                if not aux_adyacente.visitado:
                    barridoProfundidad(grafo, aux_adyacente)
            
                adyacentes = adyacentes.sig
        vertice = vertice.sig


def barridoAmplitud(grafo, vertice):
    '''Barrido en amplitud del grafo'''    
    marcarNoVisitado(grafo)
    cola = Cola()
    
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
    
            while not cola_vacia(cola):
                nodo = atencion(cola)
                print(nodo.info)
                adyacente = nodo.adyacentes.inicio
    
                while adyacente is not None:
                    adyacente = buscarVertice(grafo, adyacente.destino)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacente = adyacente.sig
    
    vertice = vertice.sig


def barridoVertices(grafo):
    aux = grafo.inicio
    while aux is not None:
        print("Vertice:", aux.info)
        print("Adyacentes:")
        barridoAdyacentes(aux)
        aux = aux.sig
        print()


def barridoAdyacentes(vertice):
    '''Muestra los adyacentes del vertice.'''
    aux = vertice.adyacentes.inicio
    while(aux is not None):
        print("Destino: {}  -   Info: {}".format(aux.destino, aux.info))
        aux = aux.sig


# ELIMINAR

def eliminarVertice(grafo, clave):
    '''Elimina un vertice del grafo y devuelve el dato, si lo encuentra'''
    dato = None

    if grafo.inicio.info == clave:
        dato = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
    
        while (act is not None) and (act.info != clave):
            ant = act
            act = act.sig
    
        if (act is not None):
            dato = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    
    if dato is not None:
        aux = grafo.inicio

        # Realiza un barrido de los vertices y quita la aristas que hayan ido a ese vertice
        while aux is not None:
            if aux.adyacentes.inicio is not None:
                quitarArista(aux, dato)
            aux = aux.sig
   
    return dato


def quitarArista(vertice, destino):
    '''Quita el arista con info = destino, del vertice dado'''
    info_extraida = None
    aux_adyacentes = vertice.adyacentes.inicio

    if aux_adyacentes.destino == destino:
        info_extraida = aux_adyacentes.info
        aux_adyacentes = aux_adyacentes.sig
        vertice.adyacentes.tamanio -= 1
    else:
        ant = aux_adyacentes
        act = aux_adyacentes.sig
    
        while (act is not None) and (act.destino != destino):
            ant = act
            act = act.sig

        if (act is not None):
            info_extraida = act.info
            ant = act.sig
            vertice.adyacentes.tamanio -= 1

    return info_extraida


def eliminarArista(grafo, vertice, destino):
    '''Elimina el arista de la lista de aristas del vértice pasado, que posea el destino pasado'''
    nodo_quitado = quitarArista(vertice, destino)

    if not grafo.dirigido:
        nodo_origen = buscarVertice(grafo, destino)
        quitarArista(nodo_origen, vertice.info)
    
    return nodo_quitado


# UTILS

def grafoVacio(grafo):
    '''Devuelve True si el grafo está vacío'''
    return grafo.inicio is None


def existePaso(grafo, origen, destino):
    resultado = False
    
    if(not origen.visitado):
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
    
        while(vadyacentes is not None) and (not resultado):
            adyacente = buscarVertice(grafo, vadyacentes.destino)
            if(adyacente.info == destino.info):
                return True
            elif(not adyacente.visitado):
                resultado = existePaso(grafo, adyacente, destino)
    
            vadyacentes = vadyacentes.sig
    return resultado


def marcarNoVisitado(grafo):
    '''Marca todos los vértices como no visitado'''
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig


 # ARBOLES/CAMINOS

def dijkstra(grafo, origen, destino):
    '''Camino mas corto entre dos nodos'''
    no_visitados = Heap(grafo.tamanio)
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info == origen:
            arribo_H(no_visitados, 0, [aux, None])
        else:
            arribo_H(no_visitados, 1, [aux, None])
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = buscar_H(no_visitados, aux.destino)
            if (no_visitados.vector[pos][0] > dato[0] + aux.peso):
                no_visitados.vector[pos][1][1] = dato[1][0].info
            aux = aux.sig
    return camino


def kruskal(grafo):
    """Algoritmo de Kruskal para hallar el árbol de expansión mínimo."""
    bosque = []
    heap_aristas = Heap(grafo.tamanio**2)
    
    aux_vertices = grafo.inicio
    while aux_vertices is not None:
        bosque.append([aux_vertices.info])
        adyacentes = aux_vertices.adyacentes.inicio
        
        while adyacentes is not None:
            datos = [aux_vertices.info, adyacentes.destino]
            prioridad = adyacentes.info
            arribo_H(heap_aristas, prioridad, datos)
            
            adyacentes = adyacentes.sig
        aux_vertices = aux_vertices.sig
    
    while (len(bosque) == 1) and (not heap_vacio(heap_aristas)):
        dato = atencion_H(heap_aristas)
        origen = None
        for elemento in bosque:
            if dato[1][0] in elemento:
                origen = bosque.pop(bosque.index(elemento))
        destino = None
    
    return bosque


def prim(grafo):
    """Algoritmo de Prim para hallar el árbol de expansión mínimo."""
    bosque = []
    vertice_inicial = grafo.inicio
    heap_aristas = Heap(grafo.tamanio ** 2)
    aux_adyacentes = vertice_inicial.adyacentes.inicio

    if grafo:
        bosque += vertice_inicial.info

    while aux_adyacentes is not None:
        # Se arriban todas las aristas
        datos = [vertice_inicial.info, aux_adyacentes.destino]
        peso = aux_adyacentes.info
        arribo_H(heap_aristas, peso, datos)
        aux_adyacentes = aux_adyacentes.sig
    
    while (len(bosque) // 2 < grafo.tamanio) and not heap_vacio(heap_aristas):
        # Mientras heap no esté vació, se desencola una arista
        datos_y_prioridad = atencion_H(heap_aristas)
        datos = datos_y_prioridad[1]
        origen = datos[0]
        destino = datos[1]
        # print("Ingresado par {} > {} con peso {}".format(origen, destino, peso))

        # Si alguno de los extremos no ha sido visitado. es decir que ya existe camino entre ellos:
        if(len(bosque) == 0 or ((origen not in bosque) or (destino not in bosque))):
            bosque += destino
            
            nodo_destino = buscarVertice(grafo, destino)
            aux_adyacentes = nodo_destino.adyacentes.inicio

            # Se busca el vertice y se agrega al heap todas las aristas de este
            while aux_adyacentes is not None:
                peso = aux_adyacentes.info
                datos = [nodo_destino.info, aux_adyacentes.destino]
                arribo_H(heap_aristas, peso, datos)
                aux_adyacentes = aux_adyacentes.sig

            
    return bosque
