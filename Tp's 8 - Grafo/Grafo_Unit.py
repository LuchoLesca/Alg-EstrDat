from TDA_Grafo import *
from random import randint, choice
from TDA_Archivo import *


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

def hayCaminoDirecto(grafo, origen, destino):
    '''Retorna si hay camino directo desde origen hasta destino'''
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
        if hayCaminoDirecto(grafo, nodo_origen.info, destino):
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




# EJERCICOI 5

class Dios():

    def __init__(self, nombre, descripcion, nombre_padre, nombre_madre):
        self.info = nombre
        self.descripcion = descripcion
        self.padre = nombre_padre
        self.madre = nombre_madre
        self.sig = None
        self.visitado = False
        self.adyacentes = listaAristas()

    def __eq__(self, other):
        if (isinstance(other, Dios)):
            return self.info == other.info

    def __str__(self):
        return "Info(nombre): " + self.info + " - Padre: " + self.padre + " - Madre: " + self.madre


def extraerDiosesDesdeArchivo(g, archivo):
    '''Carga los vertices de los dioses en el grafo'''
    dioses = []

    pos = 0
    tam_archivo = len(archivo)
    while pos < tam_archivo:
        linea = leer(archivo, pos)
        datos_dios = linea.split(";")
        nombre = datos_dios[0].strip()
        descripcion = datos_dios[1].strip()
        nombre_padre = datos_dios[2].strip()
        nombre_madre = datos_dios[3].strip()
        dios = Dios(nombre, descripcion, nombre_padre, nombre_madre)
        if dios not in dioses:
            dioses.append(dios)
        pos += 1
    return dioses

def cargarGrafoDeDioses(g):
    txtToDat("Dioses/dioses.txt", "Dioses/dioses")
    
    archivo = abrir("Dioses/dioses")
    dioses = extraerDiosesDesdeArchivo(g, archivo)
    cerrar(archivo)

    cargarVerticesDiosesGrafo(g, dioses)
    cargarAristasDiosesGrafo(g, dioses)

def cargarVerticesDiosesGrafo(g, lista_dioses):
    for dios in lista_dioses:
        insertarVerticeObjeto(g, dios)

def cargarAristasDiosesGrafo(g, lista_dioses):
    for dios in lista_dioses:
        nombre_dios = dios.info
        nombre_padre = dios.padre
        nombre_madre = dios.madre
        
        # cargarRelacionPareja(g, nombre_padre, nombre_madre)
        
        cargarRelacionPadresHijos(g, nombre_padre, nombre_dios, "Padre de")
        cargarRelacionPadresHijos(g, nombre_madre, nombre_dios, "Madre de")
        
        cargarRelacionHermanos(g, nombre_dios, nombre_padre, nombre_madre, lista_dioses)

def cargarRelacionPareja(g, dios1, dios2):
    '''Carga las aristas de las relaciones pareja'''
    datos_dios1 = buscarVertice(g, dios1)
    datos_dios2 = buscarVertice(g, dios2)
    
    if (datos_dios1 is not None) and (datos_dios2 is not None):
        if buscarArista(datos_dios1, dios2) is None:
            insertarArista(g, "Pareja", dios1, dios2)
            insertarArista(g, "Pareja", dios2, dios1)

def cargarRelacionPadresHijos(g, padre_madre, hijo, condicion_madre_padre):
    '''Carga las aristas de las relaciones padres/hijos'''
    datos_padre_madre = buscarVertice(g, padre_madre)
    datos_hijo = buscarVertice(g, hijo)
    if (datos_padre_madre is not None) and (datos_hijo is not None):
        if buscarArista(datos_padre_madre, condicion_madre_padre) is None:
            insertarArista(g, condicion_madre_padre, padre_madre, hijo)
        if buscarArista(datos_hijo, "Hijo de") is None:
            insertarArista(g, "Hijo de", hijo, padre_madre)

def cargarRelacionHermanos(g, nombre_dios, nombre_padre, nombre_madre, dioses):
    for dios in dioses:
        mismo_padre = (nombre_padre != "-") and (nombre_padre == dios.padre)
        misma_madre = (nombre_madre != "-") and (nombre_madre == dios.madre)
        comparten_padre_o_madre = mismo_padre or misma_madre
        
        if (comparten_padre_o_madre) and (dios.info != nombre_dios):
            insertarArista(g, "Hermano de", nombre_dios, dios.info)

# E

def tieneRelDirecta(vertice1, vertice2):
    rel_directa = False
    relacion = ""
    # Busca si un vertice es adyacente de otro
    aux_aristas = vertice1.adyacentes.inicio
    while aux_aristas is not None:
        if aux_aristas.destino == vertice2.info:
            rel_directa = True
            relacion += aux_aristas.info
            break
        aux_aristas = aux_aristas.sig

    # Lo mismo que antes pero con los datos de busqueda intercambiados
    aux_aristas = vertice2.adyacentes.inicio
    while aux_aristas is not None:
        if aux_aristas.destino == vertice1.info:
            rel_directa = True
            relacion += " - " + aux_aristas.info
            break
        aux_aristas = aux_aristas.sig
    
    return rel_directa, relacion

# F

def caminoMasCortoPorCantAristas(g, origen, destino):
    '''Camino mas corto (menos aristas) entre dos nodos'''
    no_visitados = Heap(g.tamanio)
    camino = Pila()
    aux_vertices = g.inicio
    while aux_vertices is not None:
        if aux_vertices.info == origen:
            arribo_H(no_visitados, 0, [aux_vertices, None])
        else:
            arribo_H(no_visitados, inf, [aux_vertices, None])
        aux_vertices = aux_vertices.sig

    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)
        aux_adyacentes = dato[1][0].adyacentes.inicio

        while aux_adyacentes is not None:
            pos = buscar_H(no_visitados, aux_adyacentes.destino)
            distancia_acumulada = dato[0] + 1
            if (distancia_acumulada < no_visitados.vector[pos][0]):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiarPrioridad(no_visitados, pos, distancia_acumulada)
            aux_adyacentes = aux_adyacentes.sig

    return resolverCaminoDijkstra(camino, destino)


# EJERCICIO 7


class Persona():

    def __init__(self, nombre, apellido, dni, username):
        self.info = username
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.sig = None
        self.visitado = False
        self.adyacentes = listaAristas()

    def __eq__(self, other):
        if (isinstance(other, Dios)):
            return self.info == other.info

    def __str__(self):
        return self.info + " " + self.dni

# A

def cargarVerticesRedesSociales(g):
    datos_personas = [
        Persona("Pedro", "Gonzalez", randint(10000000, 60000000), "PeGo"),
        Persona("Alfonso", "Rodriguez", randint(10000000, 60000000), "AlRo"),
        Persona("Miguel", "Lopez", randint(10000000, 60000000), "MiLo"),
        Persona("Carmen", "Fernandez", randint(10000000, 60000000), "CarFer"),
        Persona("Eduardo", "Garcia", randint(10000000, 60000000), "EduGa"),
        Persona("Roberto", "Perez", randint(10000000, 60000000), "RoPe"),
        Persona("Mario", "Martinez", randint(10000000, 60000000), "MaMa"),
        Persona("Norma", "Gomez", randint(10000000, 60000000), "NorGo"),
        Persona("Federico", "Diaz", randint(10000000, 60000000), "FeDi"),
        Persona("Lucrecia", "Sanchez", randint(10000000, 60000000), "LuSa"),
        Persona("Manolo", "Alvarez", randint(10000000, 60000000), "MaAl"),
        Persona("Etelvina", "Romero", randint(10000000, 60000000), "EeRo"),
        Persona("Ricardo", "Sosa", randint(10000000, 60000000), "RiSo"),
        Persona("Ana", "Ruiz", randint(10000000, 60000000), "AnRu"),
        Persona("Martin", "Torres", randint(10000000, 60000000), "MarTo"),
        Persona("Abel", "Suarez", randint(10000000, 60000000), "AbSu"),
        Persona("Florencia", "Castro", randint(10000000, 60000000), "FloCas"),
        Persona("Rosa", "Gimenez", randint(10000000, 60000000), "RoGi"),
        Persona("Maria", "Vazquez", randint(10000000, 60000000), "MaVaz"),
        Persona("Joaquin", "Acosta", randint(10000000, 60000000), "JoAcos")
    ]

    for persona in datos_personas:
        insertarVerticeObjeto(g, persona)

# B

def cargarAristasRedesSociales(g, cantidad):
    redes = ["Twitter", "Instagram", "Facebook"]

    for i in range(cantidad):
        red = choice(redes)
        retwitts_megustas = randint(0, 100)
        lista_vertices = listaVertices(g)
        origen = choice(lista_vertices)
        destino = choice(lista_vertices)
        
        insertarArista(g, [red, retwitts_megustas], origen, destino)

# C

def pesoMaximoDeAristas(g, red_social):
    peso_max = -1
    aux_vertices = g.inicio
    
    while aux_vertices is not None:
        aux_adyacentes = aux_vertices.adyacentes.inicio
    
        while aux_adyacentes is not None:
            red = aux_adyacentes.info[0]
            peso = aux_adyacentes.info[1]
            
            if (red == red_social) and (peso > peso_max):
                peso_max = peso
            aux_adyacentes = aux_adyacentes.sig
        aux_vertices = aux_vertices.sig
    
    return peso_max


def kruskalRedesSociales(grafo, red_social):
    """Algoritmo de Kruskal para hallar el árbol de expansión màximo de la red social pasada."""
    bosque = []
    heap_aristas = Heap(grafo.tamanio**2)

    peso_maximo = pesoMaximoDeAristas(grafo, red_social)
    aux_vertices = grafo.inicio
    
    while aux_vertices is not None:
        bosque.append([aux_vertices.info])
        adyacentes = aux_vertices.adyacentes.inicio
        
        while adyacentes is not None:
            if adyacentes.info[0] == red_social:
                datos = [aux_vertices.info, adyacentes.destino]
                peso = peso_maximo - adyacentes.info[1]
                arribo_H(heap_aristas, peso, datos)            
            adyacentes = adyacentes.sig
        aux_vertices = aux_vertices.sig
    
    while (len(bosque) > 1) and (not heap_vacio(heap_aristas)):
        datos_y_peso = atencion_H(heap_aristas)
        peso = datos_y_peso[0]
        datos = datos_y_peso[1]
        
        origen = datos[0]
        destino = datos[1]
        array_origen = None
        array_destino = None

        for array_conexo in bosque:
            if origen in array_conexo:
                indice = bosque.index(array_conexo)
                array_origen = bosque.pop(indice)
                break
        for array_conexo in bosque:
            if destino in array_conexo:
                indice = bosque.index(array_conexo)
                array_destino = bosque.pop(indice)
                break
        
        if (array_origen is not None) and (array_destino is not None):
                if (len(array_origen) > len(array_destino)) or (len(array_origen) == len(array_destino)):
                    bosque.append(array_origen + array_destino)
                else:
                    bosque.append(array_destino + array_origen)
        else:
            bosque.append(array_origen)

    return bosque[0]


# D y E

def existeCaminoRedSocial(g, vertice, destino, red_social):
    marcarNoVisitado(g)

    cola = Cola()
    
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
    
            while not cola_vacia(cola):
                nodo = atencion(cola)
                if nodo.info == destino:
                    # print("Cortó en", nodo.info)
                    return True
                # else:
                #     print("Pasó por", nodo.info)
                # print(nodo.info)
                
                aux_adyacentes = nodo.adyacentes.inicio
                while aux_adyacentes is not None:
                    if aux_adyacentes.info[0] == red_social:
                        resultado = buscarVertice(g, aux_adyacentes.destino)

                        if not resultado.visitado:
                            resultado.visitado = True
                            arribo(cola, resultado)

                    aux_adyacentes = aux_adyacentes.sig
        vertice = vertice.sig

    return False



# EJERCICIO 8

class VerticeAeropuerto():
    '''Nodo vertice con datos de aeropuerto'''
    def __init__(self, nombre, ubicacion, cant_pistas):
        self.info = nombre
        self.latitud = ubicacion[0]
        self.longitud = ubicacion[1]
        self.cant_pistas = cant_pistas
        self.sig = None
        self.visitado = False
        self.adyacentes = listaAristas()

    def __str__(self):
        return "Nombre:" + self.info + " - Latitud:" + str(self.latitud) + " - Longitud" + str(self.longitud) + " - Pistas:" + str(self.cant_pistas)


class AristaVuelo():
    '''Nodo arista con datos de vuelo'''
    def __init__(self, salida, arribo, empresa, costo, duracion, distancia):
        self.salida = salida
        self.arribo = arribo
        self.empresa = empresa
        self.costo = costo
        self.duracion = duracion
        self.distancia = distancia

    def __str__(self):
        return "Salida:" + self.salida + " - Arribo:" + self.arribo + " - Empresa:" + self.empresa + " - Costo:" + str(self.costo) + " - Duracion:" + str(self.duracion) + " - Distancia:" + str(self.distancia)
        
    
def cargarArchivoAeropuertos():
    '''Carga aeropuertos(vertices) con info random (excepto nombre/info) a un archivo'''
    paises = ["Argentina", "China", "Brasil", "Tailandia", "Grecia", "Alemania", "Francia", "Estados Unidos", "Japon", "Jamaica"]

    archivo = abrir("AeropuertosYViajes/aeropuertos")
    limpiar(archivo)

    for pais in paises:
        latitud, longitud = randint(-150, 300), randint(-150, 300)
        cantidad_pistas = randint(1, 6)
        guardar(archivo, VerticeAeropuerto(pais, [latitud, longitud], cantidad_pistas))

    cerrar(archivo)


def cargarArchivoVuelos(cantidad=20):
    '''Carga vuelos(aristas) con info random (excepto origen y destino) a un archivo'''
    paises = ["Argentina", "China", "Brasil", "Tailandia", "Grecia", "Alemania", "Francia", "Estados Unidos", "Japon", "Jamaica"]

    archivo = abrir("AeropuertosYViajes/vuelos")
    limpiar(archivo)

    for i in range(cantidad):
        hora_salida = str(randint(00, 23)) + ":" + str(randint(00, 59))
        hora_arribo = str(randint(00, 23)) + ":" + str(randint(00, 59))
        nombre_empresa = "Empresa"+str(randint(1, 10))
        costo_pasaje = 1200
        duracion = randint(30, 2600)
        distancia = randint(600, 10000)

        nuevo_vuelo = AristaVuelo(hora_salida, hora_arribo, nombre_empresa, costo_pasaje, duracion, distancia)

        guardar(archivo, nuevo_vuelo)

    cerrar(archivo)