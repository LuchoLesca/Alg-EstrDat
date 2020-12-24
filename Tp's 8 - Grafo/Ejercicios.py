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

# g = cargarGrafoEj2(True)
# barridoVertices(g)

# A
""" 
print("MATRIZ DE ADYACENCIA")
mostrarMatrizAdyacencia(g)
print("\nLISTA DE ADYACENCIA")
mostrarListaAdyacencia(g)
 """
# C
# Se vuelve a cargar el grafo, pero esta vez como no dirigido
g = cargarGrafoEj2(False)

arbol_expansion_min = kruskal(g)
# print(arbol_expansion_min)


# D
""" 
insertarArista(g, randint(0, 100), "E", "C")
 """
 # E
""" 
 camino_mas_corto = dijkstra(g, "A", "D")
  """
  