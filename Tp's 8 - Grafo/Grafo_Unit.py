from TDA_Grafo import *
from random import randint, choice


# EJERCICIO 1

# A


def verticeSinApuntar(vertice):
    '''retorna True si el vértice no apunta a ningún otro'''
    return vertice.adyacentes.tamanio == 0


def verticeEsApuntado(grafo, vertice):
    '''Retorna True si el vertice es apuntado por algún otro'''
    apuntado = False

    aux_vertice = grafo.inicio

    while (aux_vertice is not None) and (not apuntado):
        aux_adyacentes = aux_vertice.adyacentes.inicio
        
        while (aux_adyacentes is not None) and (not apuntado):
            if aux_adyacentes.destino == vertice.info:
                apuntado = True
            aux_adyacentes = aux_adyacentes.sig
        
        aux_vertice = aux_vertice.sig

    return apuntado


def verticeDesconectado(grafo, vertice):
    '''Retorna True si el vertice no apunta a nada y no es apuntado por ninguno'''
    return verticeSinApuntar(vertice) and (not verticeEsApuntado(grafo, vertice))


def listarVerticesDesconectados(grafo):
    '''Devuelve una lista de los vertices desconectados: que nu apuntan a ninguno, y ninguno apunta a él'''
    lista = []

    aux_vertice = grafo.inicio
    
    while aux_vertice is not None:
        if verticeSinApuntar(aux_vertice) and  (not verticeEsApuntado(grafo, aux_vertice)):
            lista.append(aux_vertice)

        aux_vertice = aux_vertice.sig
    return lista


def listaAleatoriaVerticesSinRepetir(cantidad=10):
    '''Devuelve una lista aleatoria de datos de vertices a ser ingresados, sin repetirse'''
    lista_vertices = []

    while len(lista_vertices) < cantidad:
        info = chr(randint(65, 90))
        if info not in lista_vertices:
            lista_vertices.append(info)

    return lista_vertices


def eliminarVerticesDesconectados(grafo):
    '''Elimina del grafo todos los vértices desconectados. Devuelve lista'''
    eliminados = []
    aux_vertice = grafo.inicio
    
    while aux_vertice is not None:
        if verticeDesconectado(grafo, aux_vertice):
            eliminarVertice(grafo, aux_vertice.info)
            eliminados.append(aux_vertice)
    
        aux_vertice = aux_vertice.sig

    return eliminados


# B


def nodosMayorCantidadAristasSalida(grafo):
    '''Retorna lista de nodos con mayor cantidad de aristas que salen de él'''
    lista_nodos = []
    mayor_cantidad = 0

    aux_vertices = grafo.inicio
    
    while aux_vertices is not None:
        if aux_vertices.adyacentes.tamanio > mayor_cantidad:
            mayor_cantidad = aux_vertices.adyacentes.tamanio
            lista_nodos = [aux_vertices]
        elif aux_vertices.adyacentes.tamanio == mayor_cantidad:
            lista_nodos.append(aux_vertices)

        aux_vertices = aux_vertices.sig

    return lista_nodos


# C 

def listaNodosQueMeApuntan(grafo, vertice):
    '''Dado un vertice, retorna una lista de los nodos que apuntan hacia él'''
    lista = []

    aux_vertice = grafo.inicio

    while (aux_vertice is not None):
        # Recorrida los vertices grafo
        aux_adyacentes = aux_vertice.adyacentes.inicio
    
        while (aux_adyacentes is not None):
            # Recorrida de las aristas de la lista de adyacencia de cada vertice    
            if (aux_vertice not in lista) and (aux_adyacentes.destino == vertice.info):
                lista.append(aux_vertice)
            
            aux_adyacentes = aux_adyacentes.sig
        
        aux_vertice = aux_vertice.sig

    return lista


def nodosMayorCantidadAristasEntrada(grafo):
    '''Retorna lista de nodos con mayor cantidad de aristas que llegan a él'''
    lista_nodos = []
    mayor_cantidad = 0

    aux_vertices = grafo.inicio
    
    while aux_vertices is not None:
        cantidad_entrantes = len(listaNodosQueMeApuntan(grafo, aux_vertices))
        
        if cantidad_entrantes > mayor_cantidad:
            mayor_cantidad = cantidad_entrantes
            lista_nodos = [aux_vertices]
        
        elif cantidad_entrantes == mayor_cantidad:
            lista_nodos.append(aux_vertices)

        aux_vertices = aux_vertices.sig

    return lista_nodos


# D

def verticesSinAccesoAOtros(grafo):
    '''Lista la información de los vertices del  grafo que no tienen acceso a ningún otro vertice'''
    aux_vertices = grafo.inicio

    print("Vertices desde los cuales no se puede acceder a otro vértice:")

    while aux_vertices is not None:
        if verticeSinApuntar(aux_vertices):
            print(aux_vertices.info)
        
        aux_vertices = aux_vertices.sig
    

# F

def seAutoapunta(vertice):
    '''Retorna si un vertice se autoapunta'''
    aux_adyacentes = vertice.adyacentes.inicio

    while aux_adyacentes is not None:
        if aux_adyacentes.destino == vertice.info:
            return True
        aux_adyacentes = aux_adyacentes.sig

    return False

def cantidadAutoapuntados(grafo):
    '''Retorna cantidad de vértices se apuntan a si mismos'''
    cantidad_autoapuntados = 0
    aux_vertices = grafo.inicio

    while aux_vertices is not None:
        if seAutoapunta(aux_vertices):
            cantidad_autoapuntados += 1

        aux_vertices = aux_vertices.sig

    return cantidad_autoapuntados


# G

def aristaMasLarga(grafo):
    '''Determina la/s arista/s más larga, devuelve lista'''
    lista = []
    distancia_maxima = 0

    aux_vertice = grafo.inicio

    while (aux_vertice is not None):
        # Recorrida los vertices grafo
        aux_adyacentes = aux_vertice.adyacentes.inicio
    
        while (aux_adyacentes is not None):
            # Recorrida de las aristas de la lista de adyacencia de cada vertice    
            
            distancia = aux_adyacentes.info

            if distancia > distancia_maxima:
                distancia_maxima = distancia
                
                ori = aux_vertice.info
                des = aux_adyacentes.destino
                lista = [[ori, des, distancia]]
        
            elif distancia == distancia_maxima:
                ori = aux_vertice.info
                des = aux_adyacentes.destino

                lista.append([ori, des, distancia])
            
            aux_adyacentes = aux_adyacentes.sig
        
        aux_vertice = aux_vertice.sig

    return lista




# EJERCICIO 2

# A

def hayCamino(grafo, origen, destino):
    '''Retorna si hay camino desde origen hasta destino'''
    ori = buscarVertice(grafo, origen)
    if ori is not None:
        aux_aristas = ori.adyacentes.inicio
        while aux_aristas is not None:
            if aux_aristas.destino == destino:
                return True
            aux_aristas = aux_aristas.sig

    return False

def listaVertices(grafo):
    '''Devuelve una lista de los vertices del grafo'''
    lista = []
    aux = grafo.inicio
    while aux is not None:
        lista.append(aux.info)
        aux = aux.sig
    return lista

def listaLinea(grafo, lista_cabecera, nodo_origen):
    '''Devuelve lista con resultados que ha de imprimir por linea (vertice)'''
    lista = []
    for destino in lista_cabecera:
        if hayCamino(grafo, nodo_origen.info, destino):
            lista.append("1")
        else:
            lista.append("0")
    return lista
    
def mostrarMatrizAdyacencia(grafo):
    lista_vertices_cabecera = listaVertices(grafo)
    print("     " + "   ".join(lista_vertices_cabecera))
    print("------------------------")

    aux_vertices = grafo.inicio
    while aux_vertices is not None:
        lista_linea = listaLinea(grafo, lista_vertices_cabecera, aux_vertices)
        print(aux_vertices.info + " |  " + "   ".join(lista_linea))
        aux_vertices = aux_vertices.sig


def listaAdyacentes(vertice):
    '''Devuelve lista con valores de lista de adyacentes del vertices'''
    lista = []
    aux_aristas = vertice.adyacentes.inicio
    while aux_aristas is not None:
        lista.append(aux_aristas.destino)
        aux_aristas = aux_aristas.sig
    return lista

def mostrarListaAdyacencia(grafo):
    aux_vertices = grafo.inicio
    while aux_vertices is not None:
        lista_adyacentes = listaAdyacentes(aux_vertices)
        print("Vertices:", aux_vertices.info, "Aristas:", " >> ".join(lista_adyacentes))
        print()
        aux_vertices = aux_vertices.sig


# B

def cargarGrafoAleatorioEj2():
    g = Grafo(True)
    vertices = ['A', 'B', 'C', 'D', 'E']
    
    for char in vertices:
        insertarVertice(g, char)
    
    insertarArista(g, randint(0, 100), 'A', 'B')
    insertarArista(g, randint(0, 100), 'A', 'C')
    insertarArista(g, randint(0, 100), 'A', 'E')
    insertarArista(g, randint(0, 100), 'B', 'C')
    insertarArista(g, randint(0, 100), 'C', 'B')
    insertarArista(g, randint(0, 100), 'C', 'D')
    insertarArista(g, randint(0, 100), 'D', 'D')
    

    return g

#C

def cargarGrafoEj2V2():
    g = Grafo(False)
    vertices = ['A', 'B', 'C', 'D', 'E']
    
    for char in vertices:
        insertarVertice(g, char)

    insertarArista(g, 10, 'A', 'B')
    insertarArista(g, 12, 'A', 'C')
    insertarArista(g, 4, 'A', 'E')
    insertarArista(g, 1, 'B', 'C')
    insertarArista(g, 17, 'C', 'D')
    insertarArista(g, 6, 'D', 'D')

    return g




# EJERCICIO 3

class Antena():

    def __init__(self, id, lat, lon, vel_transf):
        self.info = id
        self.ubicacion = [lat, lon]
        self.vel_transf = vel_transf
        self.sig = None
        self.visitado = False
        self.adyacentes = listaAristas()

    def __str__(self):
        return "Id: " + str(self.info) + "\nUbicacion: " + str(self.ubicacion) + "\nVel. de transf.: " + str(self.vel_transf) + "MB/s"


def antenaRandom(identificador=-1):
    '''Devuelve un objeto antena con valores random'''
    if identificador == -1:
        id = randint(0, 999999)
    else:
        id = identificador
    latitud = randint(-200, 200)
    longitud = randint(-200, 200)
    trasnferencia = randint(100, 5000)

    return Antena(id, latitud, longitud, trasnferencia)



def insertarVerticeObjeto(grafo, objeto):
    '''Inserta un vertice al grafo, el cual en vez de ser un dato es un objeto completo'''
    vertice = objeto
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



# EJERCICIO 4 

class NodoRed():

    def __init__(self, tipo, nombre):
        self.info = nombre
        self.tipo = tipo
        self.sig = None
        self.visitado = False
        self.adyacentes = listaAristas()


# E

def Ej4e(g, servidor):
    '''Indica desde qué computadora (no laptop) es el camino más corto al servidor pasado'''
    resultado_server = buscarVertice(g, servidor)
    if not resultado_server:
        print("Servidor no encontrado/s en la red")
    else:
        largo_camino_mas_corto = inf
        camino_mas_corto = []

        aux_vertices = g.inicio
        while aux_vertices is not None:
            if ("PC" in aux_vertices.tipo):
                camino, largo = dijkstra2(g, aux_vertices.info, servidor)
                if largo < largo_camino_mas_corto:
                    largo_camino_mas_corto = largo
                    camino_mas_corto = camino
            aux_vertices = aux_vertices.sig

        if largo_camino_mas_corto > 0:
            print("La pc (no laptop) desde la cual hay un camino mas corto al servidor", servidor, "es", camino_mas_corto[0])
        else:
            print("No se encontró camino")

# F

def Ej4f(g, switch, servidor):
    '''Indica desde qué computadora del switch pasado, es el camino más corto al servidor pasado'''
    resultado_switch = buscarVertice(g, switch)
    resultado_server = buscarVertice(g, servidor)
    if (not resultado_switch) or (not resultado_server):
        print("Switch y/o servidor no encontrado/s en la red")
    else:
        largo_camino_mas_corto = inf
        camino_mas_corto = []

        aux_adyacentes = resultado_switch.adyacentes.inicio
        while aux_adyacentes is not None:
            resultado = buscarVertice(g, aux_adyacentes.destino)
            if ("PC" in resultado.tipo) or ("Laptop" in resultado.tipo):

                camino, largo = dijkstra2(g, resultado.info, servidor)

                if largo < largo_camino_mas_corto:
                    largo_camino_mas_corto = largo
                    camino_mas_corto = camino
            aux_adyacentes = aux_adyacentes.sig

        if largo_camino_mas_corto > 0:
            print("El camino más corto hacia", servidor, "desde una computadora del switch", switch, "es desde la computadora", camino_mas_corto[0])
        else:
            print("No se encontró camino")

