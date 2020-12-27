import TDA_Grafo as Gra
from Grafo_Unit import *


#  EJERCICIO 1
""" 
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
 """
# A
""" 
# Eliminar vertices desconectados
eliminados = eliminarVerticesDesconectados(g)

print("Info de nodos desconectados eliminados:")
for nodo in eliminados:
    print(nodo.info)
 """
# B
""" 
nodos_mas_conexiones_salida = nodosMayorCantidadAristasSalida(g)

print("Nodos/s con mayor cantidad de aristas que salen de él:")

for nodo in nodos_mas_conexiones_salida:
     print(nodo.info)
 """
# C
""" 
nodos_mas_conexiones_entrada = nodosMayorCantidadAristasEntrada(g)

print("Nodos/s con mayor cantidad de aristas que llegan de él:")

for nodo in nodos_mas_conexiones_entrada:
     print(nodo.info)
 """

# D 
""" 
verticesSinAccesoAOtros(g)
 """

# E
""" 
print("Cantidad de vertices luego de haberse eliminado los vértices desconectados:", grafo.tamanio)
 """

# F
""" 
print("Cantidad de vertices que se autoapuntan:", cantidadAutoapuntados(g))
 """

# G
""" 
aristas_mas_largos = aristaMasLarga(g)

print("Lista de arista/s más larga/s")
for arista in aristas_mas_largos:
    print("Origen: {}.  Destino: {}.  Distancia: {}". format(arista[0], arista[1], arista[2]))
 """


# EJERCICIO 2

# B 

# g = cargarGrafoEj2()
# barridoVertices(g)

# A
""" 
print("MATRIZ DE ADYACENCIA")
mostrarMatrizAdyacencia(g)
print("\nLISTA DE ADYACENCIA")
mostrarListaAdyacencia(g)
 """
# C

def grafoPueba():
    g = Grafo(False)
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    for char in vertices:
        insertarVertice(g, char)

    insertarArista(g, 7, 'A', 'B')
    insertarArista(g, 5, 'A', 'D')
    
    insertarArista(g, 7, 'B', 'A') #
    insertarArista(g, 8, 'B', 'C')
    insertarArista(g, 9, 'B', 'D')
    insertarArista(g, 7, 'B', 'E')
    
    insertarArista(g, 8, 'C', 'B') # 
    insertarArista(g, 5, 'C', 'E')
    
    insertarArista(g, 5, 'D', 'A') #
    insertarArista(g, 9, 'D', 'B') #
    insertarArista(g, 15, 'D', 'E')
    insertarArista(g, 6, 'D', 'F')
    
    insertarArista(g, 7, 'E', 'B') #
    insertarArista(g, 5, 'E', 'C') #
    insertarArista(g, 15, 'E', 'D') #
    insertarArista(g, 8, 'E', 'F')
    insertarArista(g, 9, 'E', 'G')
    
    insertarArista(g, 6, 'F', 'D') #
    insertarArista(g, 8, 'F', 'E') #
    insertarArista(g, 11, 'F', 'G')
    
    insertarArista(g, 9, 'G', 'E') #
    insertarArista(g, 11, 'G', 'F') #
    
    g.inicio = buscarVertice(g, "A")
    
    return g

# Se vuelve a cargar el grafo, pero esta vez como no dirigido
g = cargarGrafoEj2V2()

# g = grafoPueba()
arbol_min = prim(g)
print(arbol_min)


# D
""" 
insertarArista(g, randint(0, 100), "E", "C")
 """
 # E
""" 
 camino_mas_corto = dijkstra(g, "A", "D")
  """
  