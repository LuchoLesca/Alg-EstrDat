from TDA_Grafo import *
from random import randint



def verticeSinApuntar(vertice):
    '''retorna True si el vértice no apunta a ningún otro'''
    return vertice.adyacentes.tamanio == 0


def verticeEsApuntado(grafo, vertice):
    '''Retorna True si el vertice no es apuntado por ningún otro'''
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
    aux_vertice = grafo.inicio
    while aux_vertice is not None:
        if verticeDesconectado(grafo, aux_vertice):
            eliminarVertice(g, aux_vertice.info)
            print("Elimnado:", aux_vertice.info)

        aux_vertice = aux_vertice.sig



lista_vertices = listaAleatoriaVerticesSinRepetir(15)

g = Grafo()

# Agrega vertices
for dato in lista_vertices:
    insertarVertice(g, dato)

# Agrega aristas
cantidad_agregadas = 0
while cantidad_agregadas < 30:
    origen = chr(randint(65, 90))
    destino = chr(randint(65, 90))
    
    insertarArista(g, randint(1, 100), origen, destino)
    cantidad_agregadas += 1


barridoVertices(g)

# A

# Eliminar vertices desconectados
eliminarVerticesDesconectados(g)