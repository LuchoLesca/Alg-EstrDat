from TDA_Grafo import *
from TDA_Pila import *
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
""" 
g = cargarGrafoAleatorioEj2()
 """
# B 
""" 
barridoVertices(g)
 """
# A
""" 
print("MATRIZ DE ADYACENCIA")
mostrarMatrizAdyacencia(g)
print("\nLISTA DE ADYACENCIA")
mostrarListaAdyacencia(g)
 """
# C
# Se vuelve a cargar el grafo, pero esta vez como no dirigido
""" 
g = cargarGrafoEj2V2()

print("Arbol de expansión mínima con algoritmo Prim")
arbol_exp_min = prim(g)
print(arbol_exp_min)
print("\nArbol de expansión mínima con algoritmo Kruskal")
arbol_exp_min = kruskal(g)
print(arbol_exp_min)
 """
# D
""" 
g = cargarGrafoEj2V2()
insertarArista(g, 6, "E", "C")
 """
 # E
""" 
inicio = "A"
fin = "D"

camino_mas_corto = dijkstra(g, inicio, fin)
print(camino_mas_corto)
 """


# EJERCICIO 3

# A
""" 
g = Grafo(False)
 """
# B
""" 
vertices = ["S", "T", "U", "V", "X", "Y", "Z"]

for char in vertices:
    insertarVerticeObjeto(g, antenaRandom(char))

cont = 0
while cont < 10:
    inicio = choice(vertices)
    destino = choice(vertices)
    if (inicio != destino):
        insertarArista(g, randint(0, 100), inicio, destino)
        cont += 1
 """
# C
""" 
print("Tamanio del grafo:", g.tamanio)
 """
# D
""" 
camino_mas_corto = dijkstra(g, "X", "Y")
if len(camino_mas_corto) > 1:
    print("Camino más corto desde X hasta Y:", camino_mas_corto)
else:
    print("No hay conexión entre las antenas")
 """
# E
""" 
arbol_exp_min = prim(g)
print("Arbol de expansion minimo por prim:", arbol_exp_min)
 """
# F
""" 
resultado = buscarVertice(g, "X")

if resultado:
    print(resultado)
else:
    print("La antena buscada no se encuentra")
 """



# EJERCICIO 4

# A

TIPOS = ["pc", "laptop", "servidor", "router", "switch", "impresora"]

g = Grafo(False)

# Routers
insertarVerticeObjeto(g, NodoRed("829", "Router01"))
insertarVerticeObjeto(g, NodoRed("829", "Router02"))
insertarVerticeObjeto(g, NodoRed("829", "Router03"))
# Switchs
insertarVerticeObjeto(g, NodoRed("2960-24TT", "Switch01"))
insertarVerticeObjeto(g, NodoRed("2960-24TT", "Switch02"))
# Servers
insertarVerticeObjeto(g, NodoRed("Server-PT", "Guarani"))
insertarVerticeObjeto(g, NodoRed("Server-PT", "MongoDB"))
# PC's
insertarVerticeObjeto(g, NodoRed("PC-PT", "Ubuntu"))
insertarVerticeObjeto(g, NodoRed("PC-PT", "Mint"))
insertarVerticeObjeto(g, NodoRed("PC-PT", "Fedora"))
insertarVerticeObjeto(g, NodoRed("PC-PT", "Parrot"))
insertarVerticeObjeto(g, NodoRed("PC-PT", "Manjaro"))
# Laptop's
insertarVerticeObjeto(g, NodoRed("Laptop-PT", "Debian"))
insertarVerticeObjeto(g, NodoRed("Laptop-PT", "Arch"))
insertarVerticeObjeto(g, NodoRed("Laptop-PT", "Red Hat"))
# Printers
insertarVerticeObjeto(g, NodoRed("Printer-PT", "Printer"))


insertarArista(g, 25, "Router02", "Red Hat")
insertarArista(g, 9, "Router02", "Guarani")
insertarArista(g, 37, "Router02", "Router01")
insertarArista(g, 50, "Router02", "Router03")

insertarArista(g, 43, "Router03", "Router01")
insertarArista(g, 61, "Router03", "Switch02")

insertarArista(g, 29, "Router01", "Switch01")

insertarArista(g, 17, "Switch01", "Debian")
insertarArista(g, 18, "Switch01", "Ubuntu")
insertarArista(g, 22, "Switch01", "Printer")
insertarArista(g, 80, "Switch01", "Mint")

insertarArista(g, 40, "Switch02", "Manjaro")
insertarArista(g, 12, "Switch02", "MongoDB")
insertarArista(g, 5, "Switch02", "Parrot")
insertarArista(g, 56, "Switch02", "Fedora")
insertarArista(g, 3, "Switch02", "Arch")

# B
""" 
print("Barrido de profundidad desde Red Hat")
resultado = buscarVertice(g, "Red Hat")
marcarNoVisitado(g)
barridoProfundidad(g, resultado)

print("\nBarrido de amplitud desde Red Hat")
resultado = buscarVertice(g, "Red Hat")
marcarNoVisitado(g)
barridoAmplitud(g, resultado)

print("\nBarrido de profundidad desde Debian")
resultado = buscarVertice(g, "Debian")
marcarNoVisitado(g)
barridoProfundidad(g, resultado)

print("\nBarrido de amplitud desde Debian")
resultado = buscarVertice(g, "Debian")
marcarNoVisitado(g)
barridoAmplitud(g, resultado)

print("\nBarrido de profundidad desde Arch")
resultado = buscarVertice(g, "Arch")
marcarNoVisitado(g)
barridoProfundidad(g, resultado)

print("\nBarrido de amplitud desde Arch")
resultado = buscarVertice(g, "Arch")
marcarNoVisitado(g)
barridoAmplitud(g, resultado)
 """
# C
""" 
print(dijkstra(g, "Manjaro", "Printer"))
print(dijkstra(g, "Red Hat", "Printer"))
print(dijkstra(g, "Fedora", "Printer"))
 """
# D
""" 
print("\nArbol de expansión mínima con algoritmo Kruskal")
print(kruskal(g))
 """
# E
""" 
Ej4e(g, "Guarani")
 """
# F
""" 
Ej4f(g, "Switch01", "MongoDB")
 """
# G
""" 
eliminarArista(g, buscarVertice(g, "Printer"), "Switch01")
insertarArista(g, 30, "Printer", "Router02")

print("Barrido de profundidad desde Red Hat")
resultado = buscarVertice(g, "Red Hat")
marcarNoVisitado(g)
barridoProfundidad(g, resultado)

print("\nBarrido de amplitud desde Red Hat")
resultado = buscarVertice(g, "Red Hat")
marcarNoVisitado(g)
barridoAmplitud(g, resultado)

print("\nBarrido de profundidad desde Debian")
resultado = buscarVertice(g, "Debian")
marcarNoVisitado(g)
barridoProfundidad(g, resultado)

print("\nBarrido de amplitud desde Debian")
resultado = buscarVertice(g, "Debian")
marcarNoVisitado(g)
barridoAmplitud(g, resultado)

print("\nBarrido de profundidad desde Arch")
resultado = buscarVertice(g, "Arch")
marcarNoVisitado(g)
barridoProfundidad(g, resultado)

print("\nBarrido de amplitud desde Arch")
resultado = buscarVertice(g, "Arch")
marcarNoVisitado(g)
barridoAmplitud(g, resultado)
 """








