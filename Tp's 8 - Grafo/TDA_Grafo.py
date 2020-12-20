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
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = listaAristas()


class Arista():
    # info de vértice(peso), el siguiente nodo vértice de la lista de vertices
    # y su destino o sea el nodo vertice destino que seria

    def __init__(self, info=0, destino):
        self.info = info
        self.destino = destino
        self.sig = None


class listaAristas():
    '''Crea una lista de aristas (lista de lista) vacía'''
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertarVertice(grafo, dato):
    '''Inserta un vertice al grafo'''
    vertice = Vertice(dato)
    if (grafo.inicio is None) or (vertice.info < grafo.inicio.info):
        vertice.sig = grafo.inicio
        grafo.inicio = vertice
    else:
        act = grafo.inicio.sig
        ant = grafo.inicio
        
        while (act is not None) and (act.info <= vertice.info):
            act = act.sig
            ant = ant.sig
        
        vertice.sig = act
        ant.sig = vertice
    
    grafo.tamanio += 1


# INSERTAR/AGREGAR

def agregrarArista(lista_adyacentes, dato, destino):
    '''Agrega la arista desde el vértice origen al destino.'''
    arista = Arista(dato, destino)
    if (lista_adyacentes.inicio is None) or (lista_adyacentes.inicio.destino > destino):
        arista.sig = lista_adyacentes.inicio
        lista_adyacentes.inicio = arista
    else:
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
    ori = buscar_vertice(grafo, origen)
    des = buscar_vertice(grafo, destino)
    if (ori is not None) and (des is not None):
        if grafo.dirigido:
            agregarArista(ori.adyacentes, dato, des.info)
        else:
            agregarArista(ori.adyacentes, dato, des.info)
            agregarArista(des.adyacentes, dato, ori.info)


 # BUSQUEDA

def buscarArista(vertice, buscado):
    aux = vertice.adyacentes.inicio
    while (aux is not None) and (aux.destino != buscado):
        aux = aux.sig
    return aux


def buscarVertice(grafo, buscado):
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
                aux_adyacente = buscar_vertice(grafo, adyacentes.destino)
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


def barridoAdyacentes(vertice):
    '''Muestra los adyacentes del vertice.'''
    aux = vertice.adyacentes.inicio
    while(aux is not None):
        print(aux.destino, aux.info)
        aux = aux.sig


# ELIMINAR

def eliminarVertice(grafo, clave):
    '''Elimina un vertice del grafo y lo devuelve si lo encuentra'''
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
    
    if(dato is not None):
        aux = grafo.inicio
   
        while aux is not None:
            quitarArista(aux.adyacentes, dato)
   
    return dato


def quitarArista(vertice, destino):
    x = None

    if vertice.adyacentes.inicio.destino == destino:
        x = vertice.adyacentes.inicio.info
        vertice.adyacentes.inicio = vertice.adyacentes.inicio.sig
        vertice.adyacentes.tamanio -= 1
    else:
        ant = vertice.adyacentes.inicio
        act = vertice.adyacentes.inicio.sig
    
        while (act is not None) and (act.destino != destino):
            ant = act
            act = act.sig

        if (act is not None):
            x = act.info
            ant = act.sig
            vertice.adyacentes.tamanio -= 1


def eliminarAsrista(grafo, vertice, destino):
    '''Elimina una arista del vertice, y lo devuelve si lo encuentra'''
    nodo_quitado = quitarArista(vertice, destino)

    if not grafo.dirigido:
        ori = buscarVertice(grafo, destino)
        quitarArista(ori, vertice.info)
    
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
    
        while(vadyacentes is not None and not resultado):
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


def kruskal(grafo):
    '''Arbol de expansión mínima'''
    bosque = []
    aristas = Heap(grafo.tamanio**2)
    aux = grafo.inicio
   
    while aux is not None:
        bosque.append([aux.info])
        adyacentes = aux.adyacentes.inicio
   
        while adyacentes is not None:
            arribo_H(aristas, [aux.info, adyacentes.destino], adyacentes.info)
            adyacentes = adyacentes.sig
        aux = aux.sig
   
    while (len(bosque) > 1) and (not heap_vacio(aristas)):
        dato = atencion_H(aristas)
        origen = None
   
        for elemento in bosque:
            if dato[1][0] in elemento:
                origen = bosque.pop(bosque.index(elemento))
                break
        destino = None

        if (origen is not None) and (destino is not None):
            if (len(origen) > 1) and (len(destino) == 1):
                destino = [dato[1][0], dato[1][1]]
            elif(len(destino) > 1 and len(origen) == 1):
                origen = [dato[1][0], dato[1][1]]
            elif(len(destino) > 1 and len(origen) > 1):
                origen += [dato[1][0], dato[1][1]]
            bosque.append(origen + destino)
        else:
            bosque.append(origen)
    return bosque[0]


def dijkstra(grafo, origen, destino):
    '''Camino más corto entre dos nodos'''
    no_visitados = Heap(grafo.tamanio)
    camino = Pila()
    aux = grafo.inicio
    
    while aux is not None:
        if aux.info == origen:
            arribo_H(no_visitados, [aux, None], 0)
        else:
            arribo_H(no_visitados, [aux, None], inf)
        aux = aux.sig

    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        
        while aux is not None:
            pos = buscar_H(no_visitados, aux.destino)
            if (no_visitados.vector[pos][0] > dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiarPrioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino
