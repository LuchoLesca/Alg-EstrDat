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



# EJERCICIO 5  FALTA TERMINAR >>>>>>>>>>>>>>>>>>>>
""" 
# txtToDat("Dioses/dioses.txt", "Dioses/dioses")
g = Grafo(False)
dioses = []

archivo = abrir("Dioses/dioses")


pos = 0
tam_archivo = len(archivo)
while pos < tam_archivo:
    linea = leer(archivo, pos)
    
    nombre, descripcion, nombre_padre, nombre_madre = linea.split(";")
    dios = Dios(nombre, descripcion, nombre_padre, nombre_madre)
    if dios not in dioses:
        dioses.append(dios)
    
    pos += 1

cerrar(archivo)

for dios in dioses:
    insertarVerticeObjeto(g, dios)
 """



# EJERCICIO 6
""" 
g = Grafo(True)
vertices = ["A", "B", "C", "D", "E", "F", "G"]

for vertice in vertices:
    insertarVertice(g, vertice)

insertarArista(g, 15, "A", "B")
insertarArista(g, 19, "A", "C")
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


# EJERCICIO 7   <<<<<<< FALTA TERMINAS
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




# EJERCICIO 8   

""" 
class Aeropuerto():

    def __init__(self, nombre, ubicacion, cant_pistas):
        self.info = nombre
        self.latitud = ubicacion[0]
        self.longitud = ubicacion[1]
        self.cant_pistas = cant_pistas
        self.sig = None
        self.visitado = False
        self.adyacentes = listaAristas()

    def __str__(self):
        return self.info + " " + str(self.latitud) + " " + str(self.longitud) + " " + str(self.cant_pistas)
 """
""" 
class Vuelo():

    def __init__(self, salida, arribo, empresa, costo, duracion, distancia):
        self.salida = salida
        self.arribo = arribo
        self.empresa = empresa
        self.costo = costo
        self.duracion = duracion
        self.distancia = distancia
        """ 
""" 
def cargarArchivoAeropuertos():

    paises = ["Argentina", "China", "Brasil", "Tailandia", "Grecia", "Alemania", "Francia", "Estados Unidos", "Japon", "Jamaica"]

    archivo = abrir("AeropuertosYViajes/aeropuertos")
    limpiar(archivo)

    for pais in paises:
        latitud, longitud = randint(-150, 300), randint(-150, 300)
        cantidad_pistas = randint(1, 6)
        guardar(archivo, Aeropuerto(pais, [latitud, longitud], cantidad_pistas))

    cerrar(archivo)
 """
# cargarArchivoAeropuertos()
""" 
archivo = abrir("AeropuertosYViajes/aeropuertos")
barridoArchivo(archivo)
cerrar(archivo)
 """
""" 
def cargarArchivoVuelos():
    paises = ["Argentina", "China", "Brasil", "Tailandia", "Grecia", "Alemania", "Francia", "Estados Unidos", "Japon", "Jamaica"]

    archivo = abrir("AeropuertosYViajes/vuelos")
    limpiar(archivo)

    for i in range(20):
        hora_salida = time()
        hora_arribo = randint()
        nombre_empresa = randint("Empresa"+str(randint(1, 10)))
        costo_pasaje = 1200
        duracion = randint(30, 2600)
        distancia = randint(600, 10000)

    cerrar(archivo)

cargarArchivoVuelos()

 """









