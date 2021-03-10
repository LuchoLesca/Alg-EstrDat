from TDA_Grafo import *
from TDA_Pila import *
from Grafo_Unit import *
from TDA_Archivo import *

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
""" 
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
 """
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



# EJERCICIO 5
""" 
g = Grafo()

cargarGrafoDeDioses(g)
 """
# C
""" 
dios_a_buscar = "Zeus"
resultado = buscarVertice(g, dios_a_buscar)

if not resultado:
    print("Vertice no encontrado")
else:
    aux_adyacentes = resultado.adyacentes.inicio
    print(dios_a_buscar, "es padre o madre de:")
    while aux_adyacentes is not None:
        if (aux_adyacentes.info == "Padre de") or (aux_adyacentes.info == "Madre de"):
            print(aux_adyacentes.destino)
        aux_adyacentes = aux_adyacentes.sig
 """
# D
""" 
vertice_a_buscar = "Ares"
resultado = buscarVertice(g, vertice_a_buscar)
if not resultado:
    print("Vertice no encontrado")
else:
    aux_adyacentes = resultado.adyacentes.inicio
    padre_madre = []
    hermanos = []
    hijos = []
    while aux_adyacentes is not None:
        if aux_adyacentes.info == "Hijo de":
            padre_madre.append(aux_adyacentes.destino)
        elif aux_adyacentes.info == "Padre de" or aux_adyacentes.info == "Madre de":
            hijos.append(aux_adyacentes.destino)
        elif aux_adyacentes.info == "Hermano de":
            hermanos.append(aux_adyacentes.destino)
        aux_adyacentes = aux_adyacentes.sig
    
    print("Nombre:", resultado.info)
    print("Padres: ", padre_madre)
    print("Hermanos: ", hermanos)
    print("Hijos: ", hijos)
 """
# E
""" 
dios1 = "Zeus"
dios2 = "Kronos"

resultado_dios1 = buscarVertice(g, dios1)
resultado_dios2 = buscarVertice(g, dios2)

if resultado_dios1 is not None and resultado_dios2 is not None:
    relacion_directa, relacion = tieneRelDirecta(resultado_dios1, resultado_dios2)
    if relacion_directa:
        print("La relacion entre {} y {} es: {}".format(dios1, dios2, relacion))
    else:
        print("{} y {} no tienen relacion directa".format(dios1, dios2))
else:
    print("Vertice/s no encontrado/s")
 """
# F
""" 
desde = "Selene"
hasta = "Ouranos"
camino = caminoMasCortoPorCantAristas(g, desde, hasta)
if len(camino) > 0:
    print("Camino más corto desde {} hasta {}".format(desde, hasta))
    print(camino)
else:
    print("No se encontro camino entre {} y {}".format(desde, hasta))
 """
# G
""" 
marcarNoVisitado(g)
print("Barrido en amplitud")
barridoAmplitud(g, g.inicio)

marcarNoVisitado(g)
print("\nBarrido en profundidad")
barridoProfundidad(g, g.inicio)
 """


# EJERCICIO 6
""" 
g = Grafo(True)
vertices = ["A", "B", "C", "D", "E", "F", "G"]

for vertice in vertices:
    insertarVertice(g, vertice)

insertarArista(g, 15, "A", "B")
insertarAOuranosrista(g, 19, "A", "C")
insertarArista(g, 13, "A", "D")
insertarArista(g, 2, "B", "C")
insertarArista(g, 20, "B", "E")
insertarArista(g, 12, "B", "F")
insertarArista(g, 5, "C", "E")
insertarArista(g, 9, "C", "F")
insertarArista(g, 27, "C", "G")
insertarArista(g, 39, "D", "F")
insertarArista(g, 45, "D", "G")
insertarArista(g, 1, "E", "F")
insertarArista(g, 3, "F", "G")
 """
# A
""" 
print("Barrido en amplitud desde A")
marcarNoVisitado(g)
barridoAmplitud(g, buscarVertice(g, "A"))
print("Barrido en amplitud desde C")
marcarNoVisitado(g)
barridoAmplitud(g, buscarVertice(g, "C"))
print("Barrido en amplitud desde F")
marcarNoVisitado(g)
barridoAmplitud(g, buscarVertice(g, "F"))
print("Barrido en profundidad desde A")
marcarNoVisitado(g)
barridoProfundidad(g, buscarVertice(g, "A"))
print("Barrido en profundidad desde C")
marcarNoVisitado(g)
barridoProfundidad(g, buscarVertice(g, "C"))
print("Barrido en profundidad desde F")
marcarNoVisitado(g)
barridoProfundidad(g, buscarVertice(g, "F"))
 """
# B
""" 
origenes = ["A", "C", "B"]
destinos = ["F", "D", "G"]

for i in range(len(origenes)):
    origen = origenes[i]
    destino = destinos[i]
    camino = dijkstra(g, origen, destino)
    if len(camino) > 1:
        print("Camino más corto desde {} hasta {}".format(origen, destino))
        print(camino)
    else:
        print("No hay camino posible entre los nodos {} y {}".format(origen, destino))
 """
# C
""" 
insertarArista(g, randint(1, 25), "C", "A")
insertarArista(g, randint(1, 25), "C", "B")
insertarArista(g, randint(1, 25), "G", "D")

origenes = ["A", "C", "B"]
destinos = ["F", "D", "G"]

for i in range(len(origenes)):
    origen = origenes[i]
    destino = destinos[i]
    camino = dijkstra(g, origen, destino)
    if len(camino) > 1:
        print("Camino más corto desde {} hasta {}".format(origen, destino))
        print(camino)
    else:
        print("No hay camino posible entre los nodos {} y {}".format(origen, destino))
 """
# D
""" 
mostrarMatrizAdyacencia(g)
 """


# EJERCICIO 7
"""  
g = Grafo(True)

# A

cargarVerticesRedesSociales(g)

# B

cargarAristasRedesSociales(g, 100)
 """

# barridoVertices(g)

# C Hallar arbol de expansión máximo para cada red social
# Para esto, será necesario crear un nuevo grafo no dirigido
""" 
g = Grafo(False)
cargarVerticesRedesSociales(g)
cargarAristasRedesSociales(g, 100)

print("Arbol de expansión maximo de Facebook")
print(kruskalRedesSociales(g, "Facebook"))
print("\nArbol de expansión maximo de Twitter")
print(kruskalRedesSociales(g, "Twitter"))
print("\nArbol de expansión maximo de Instagram")
print(kruskalRedesSociales(g, "Instagram"))
 """
# D
""" 
g = Grafo(True)
cargarVerticesRedesSociales(g)
cargarAristasRedesSociales(g, 50)

barridoVertices(g)

usuario1 = input("Desde: ")
usuario2 = input("Hasta: ")
red = input("Red: ")
print()
print(existeCaminoRedSocial(g, buscarVertice(g, usuario1), usuario2, red))
 """
# E
""" 
g = Grafo(True)
cargarVerticesRedesSociales(g)
cargarAristasRedesSociales(g, 50)

# barridoVertices(g)

usuario1 = "PeGo"
usuario2 = "MarTo"
redes_que_conectan = []

for red in ["Twitter", "Facebook", "Instagram"]:
    print()
    if existeCaminoRedSocial(g, buscarVertice(g, usuario1), usuario2, red):
        redes_que_conectan.append(red)

if len(redes_que_conectan) > 0:
    print("Redes por la/s que se conectan {} y {}".format(usuario1, usuario2))
    for red in redes_que_conectan:
        print(red)
else:
    print("Los usuarios {} y {} no tienen conexion a traves de ninguna red social".format(usuario1, usuario2))
 """
# F
""" 
g = Grafo(True)
cargarVerticesRedesSociales(g)
cargarAristasRedesSociales(g, 50)

usuario = "MarTo"
resultado_busqueda = buscarVertice(g, usuario)
if resultado_busqueda is not None:
    aux_adyacentes = resultado_busqueda.adyacentes.inicio
    print("Personas a las que sigue", usuario, "a traves de Instagram:")
    while aux_adyacentes is not None:
        if aux_adyacentes.info[0] == "Instagram":
            print(aux_adyacentes.destino)
        aux_adyacentes = aux_adyacentes.sig
else:
    print("Usuario", usuario, "no encontrado")
 """


# EJERCICIO 8

# Carga de Archivos (Los resetea y vuelve a cargar con datos random)

# generarArchivoAeropuertos()  # Recordar reemplazar en funcion para que lo haga con todos los paises, no manualmente como se puso para probar
# generarArchivoVuelos(10)  # Recordar reemplazar en funcion para que lo haga con todos los paises, no manualmente como se puso para probar

# Comprobación de datos de archivos
""" 
archivo = abrir("AeropuertosYViajes/aeropuertos")
barridoArchivo(archivo)
cerrar(archivo)
 """
""" 
archivo = abrir("AeropuertosYViajes/vuelos")
barridoArchivo(archivo)
cerrar(archivo)
 """

# Carga Grafo
g = Grafo(False)

cargarAeropuertosGrafo(g)
cargarVuelosGrafo(g)  # Acordarse modificar esto para que haga la carga desde el archivo, y no la carga manual que le puse

# Barrido para comprobar la carga correcta de los vuelos
""" 
cont = 0
aux_vertices = g.inicio

while aux_vertices is not None:
    probar(aux_vertices)
    aux_vertices = aux_vertices.sig
 """


# E  / Camino más corto desde Argentina a Tailandia

# i. Menor distancia
# ii. Menor duracion
# iii. Menor costo
# iv. Menor numero de escalas

""" vuel = AristaVuelo("", "", "EMresa", 123, 323, 32, "Arg")
print(getattr(vuel, "empresa")) """

print("Costo:")
print(dijkstra3(g, "Argentina", "Tailandia", "costo"))
print("Duracion:")
print(dijkstra3(g, "Argentina", "Tailandia", "duracion"))
print("Distancia:")
print(dijkstra3(g, "Argentina", "China", "distancia"))



# EJERCICIO 9

# A
""" 
planetas = [
    "Alderaan", "Endor", "Dagobah", "Hoth", "Tatooine", "Kamino", "Naboo", "Mustafar", "Scarif", "Bespin", "Coruscant", "Corellia", "Mantell", "Kessel", "Yavin IV", "Ansion", "Korriban", "Mygetto", "Nadiem", "Felucia"
]

g = Grafo(False)

# Agregando vertices
for planeta in planetas:
    insertarVertice(g, planeta)
 """
# B
""" 
# Agregando aristas sin que los vertice se autoapunten
for planeta in planetas:
    generados = 0
    origen = planeta
    while generados < 4:
        destino = choice(planetas)
        if destino != planeta:
            insertarArista(g, randint(10, 10000), origen, destino)
            generados += 1
 """
# C
""" 
arbol_expansion_minima = kruskal(g)
print("Arbol de expansion minima para recorrer todos los plantas")
print(arbol_expansion_minima)
 """
# D
""" 
print("Camino mas corto desde Tatooine hasta Dagobah")
print(dijkstra(g, "Tatooine", "Dagobah"))

print("Camino mas corto desde Alderaan hasta Endor")
print(dijkstra(g, "Alderaan", "Endor"))

print("Camino mas corto desde Hoth hasta Tatooine")
print(dijkstra(g, "Hoth", "Tatooine"))
 """



# EJERCICIO 10
""" 
# A - B

g = Grafo(False)
puntos = ["Acropolis", "Delfos", "Efeso", "Olimpia", "Partenon", "Sunion"]

# Carga de vertices
cargarVerticesLugaresGrafo(g, puntos)

# Carga Aristas
cargarAristasLugaresGrafo(g, puntos)
 """
# C
""" 
arbol_expansion_minima = kruskal(g)
print("Arbol de expansión mínima comenzando desde el inicio del grafo:")
print(arbol_expansion_minima)
 """
# D
""" 
camino_mas_corto = dijkstra(g, "Partenon", "Delfos")
print("Camino más corto desde Partenon hasta Delfos:")
print(camino_mas_corto)
 """

