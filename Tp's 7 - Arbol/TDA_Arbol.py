from TDA_Lista import Lista, NodoLista
from random import randint
from TDA_Archivo import *
from TDA_Pila_Nodo import *
from TDA_Cola_Nodo import Cola, arribo, atencion, cola_vacia, barridoC, colaToList

# Grado de nodo = LA cantidad de nodos que hereda(hijo) un nodohuffs

# Grado del arbol(aridad) = es el mayor grado de nodo que posea

# Rama(arista) = camino entre un nodo y el siguiente. Hay un solo camino de
# ramas para llegar de un nodo a otro

# Nivel de un nodo = Se termina entre la cantidad de ramas que hay entre un
# nodo y la raíz. Esto más 1. El nodo raíz está en en el nivel 0

# Altura de un nodo = es la mayor cantidad de ramas entre ese nodo y la hoja
# más lejana. El nodo más abajo tiene altura 1.

# Arbol lleno cuando los nodos internos (no hojas) tienen dos descendientes

# Arbol perfecto cuando todas las hojas están en el mismo nivel


# ----------------------------- #
# ----------------------------- #
# USADOS PARA ARBOL DE DECISION #
# ----------------------------- #
# ----------------------------- #


class Nodoarbol2():

    def __init__(self, dato, peso=0, izq=None, der=None):
        self.info = dato
        self.peso = peso
        self.izq = izq
        self.der = der


def insertarArbol2(raiz, dato, peso):
    if raiz is None:
        raiz = Nodoarbol2(dato, peso)
    else:
        if peso < raiz.peso:
            raiz.izq = insertarArbol2(raiz.izq, dato, peso)
        else:
            raiz.der = insertarArbol2(raiz.der, dato, peso)
    return raiz


# ------------------------------------------------------ #


class NodoArbol():

    def __init__(self, info, izq=None, der=None):
        self.info = info
        self.izq = izq
        self.der = der
        self.altura = 0


def altura(raiz):
    if (raiz is None):
        return -1
    else:
        return raiz.altura


def actualizarAltura(raiz):
    if altura(raiz.izq) > altura(raiz.der):
        raiz.altura = altura(raiz.izq)+1
    else:
        raiz.altura = altura(raiz.der)+1


def rotacionSimple(raiz, control):  # Si es true rota a la der, sino izq
    '''Realiza rotacion simple'''
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz

    actualizarAltura(raiz)
    actualizarAltura(aux)
    raiz = aux

    return raiz


def rotacionDoble(raiz, control):  # La última rotación que se hace le da el
    '''Realiza rotacion doble'''
    if control:                    # nombre si es izquierda o derecha
        raiz.izq = rotacionSimple(raiz.izq, False)
        raiz = rotacionSimple(raiz, True)
    else:
        raiz.der = rotacionSimple(raiz.der, True)
        raiz = rotacionSimple(raiz, False)

    return raiz


def balancear(raiz):
    '''Balancea el arbol'''
    if (raiz is not None):
        if (altura(raiz.izq) - altura(raiz.der) == 2):  # El desbalance es izq
            if (altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotacionSimple(raiz, True)
            else:
                raiz = rotacionDoble(raiz, True)
        elif (altura(raiz.der) - altura(raiz.izq) == 2):  # El desbalancees der
            if (altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotacionSimple(raiz, False)
            else:
                raiz = rotacionDoble(raiz, False)

    return raiz


def insertar(raiz, dato):
    '''Inserta el elemento en el arbol'''
    if (raiz is None):
        raiz = NodoArbol(dato)
    else:
        if (dato < raiz.info):
            raiz.izq = insertar(raiz.izq, dato)
        else:
            raiz.der = insertar(raiz.der, dato)

    raiz = balancear(raiz)
    actualizarAltura(raiz)

    return raiz


def insertarCampo(raiz, dato, campo=0):
    '''Inserta el elemento en el arbol'''
    if (raiz is None):
        raiz = NodoArbol(dato)
    else:
        if (dato[campo] < raiz.info[campo]):
            raiz.izq = insertarCampo(raiz.izq, dato, campo)
        else:
            raiz.der = insertarCampo(raiz.der, dato, campo)

    raiz = balancear(raiz)
    actualizarAltura(raiz)

    return raiz


def arbolVacio(raiz):
    return (raiz is None)


# ---------------------------------- #
#       FUNCIONES DE BÚSQUEDA        #
# ---------------------------------- #
def busqueda(raiz, buscado):  # o clave
    '''Devuelve el nodo donde encontró la info buscada'''
    aux = None
    if (raiz is not None):
        if (raiz.info == buscado):
            aux = raiz
        else:
            if (buscado < raiz.info):
                aux = busqueda(raiz.izq, buscado)
            else:
                aux = busqueda(raiz.der, buscado)
    return aux


def busquedaCampo(raiz, buscado, campo=0):
    '''Devuelve el nodo donde encontró la info buscada, por campo ingresado'''
    aux = None
    if (raiz is not None):
        if (raiz.info[campo] == buscado):
            aux = raiz
        else:
            if (buscado < raiz.info[campo]):
                aux = busquedaCampo(raiz.izq, buscado, campo)
            else:
                aux = busquedaCampo(raiz.der, buscado, campo)
    return aux


def busquedaProximidad(raiz, buscado):
    '''Realiza busqueda por proximidad'''
    aux = None
    if (raiz is not None):
        if (buscado in raiz.info):
            return raiz
        else:
            aux = busquedaProximidad(raiz.izq, buscado)
            if aux is None:
                aux = busquedaProximidad(raiz.der, buscado)
    return aux


def busquedaProximidadCampo(raiz, buscado, campo=0):
    '''Realiza busqueda por proximidad por campo seleccionado'''
    aux = None
    if (raiz is not None):
        if (buscado in raiz.info[campo]):
            return raiz
        else:
            aux = busquedaProximidadCampo(raiz.izq, buscado, campo)
            if aux is None:
                aux = busquedaProximidadCampo(raiz.der, buscado, campo)
    return aux
# ---------------------------------- #


# ---------------------------------- #
#             RECORRIDOS             #
# ---------------------------------- #
def preorden(raiz):  # Va a servir para hacer una búsqueda más facilmente
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izq)
        postorden(raiz.der)
        print(raiz.info)


def invInorden(raiz):
    if raiz is not None:
        invInorden(raiz.der)
        print(raiz.info)
        invInorden(raiz.izq)
# ---------------------------------- #


def reemplazar(raiz):  # Va hasta la derecha, hasta que no tenga raiz derecha
    '''Se utiliza a la hora de eliminar'''
    aux = None         # Encontro el mas gande los menores (porque entro por
    if (raiz.der is not None):  # raiz izquierda)
        raiz.der, aux = reemplazar(raiz.der)
    else:
        aux = raiz  # Toma la info del elemento e indexa la raiz con la raiz
        raiz = raiz.izq  # izquierda y elimina la conexión con esa hoja
    return(raiz, aux)


def eliminar(raiz, clave):  # Si devuleve None es porque no encontro nada
    x = None
    if (raiz is not None):  # Mientras no llegue a hoja, se llama recursivament
        if (raiz.info > clave):  # Si buscado es menor, recursivo para izquierd
            raiz.izq, x = eliminar(raiz.izq, clave)
        else:  # Si es mayor o igual
            if(raiz.info < clave):  # Si es mayor, recursivo a derecha
                raiz.der, x = eliminar(raiz.der, clave)
            else:  # Si es igual
                if (raiz.izq is None):  # Si no tiene rama izquierda
                    x = raiz.info       # Saca info y enlaza con única rama
                    raiz = raiz.der     # hijo. En este caso, derecha
                else:  # Si tiene rama izquierda
                    if(raiz.der is None):  # Si no tiene rama derecha
                        x = raiz.info      # obtiene dato y enlaza con unica
                        raiz = raiz.izq    # rama hijo, en este caso, derecha
                    else:  # Si tiene ambas ramas
                        raiz.izq, aux = reemplazar(raiz.izq)  # Busca de los número mas chicos, la hoja con el valor más alto. Esta elección fue arbitraría. Por también podría de los números más grandes, elegir el menor valor
                        raiz.info = aux.info  # Reemplaza el valor de ese nodo por el de la hoja que trajo
    return(raiz, x)


def eliminarCampo(raiz, clave, campo):  # Si devuleve None es porque no encontro nada
    x = None
    if (raiz is not None):  # Mientras no llegue a hoja, se llama recursivament
        if (raiz.info[campo] > clave):  # Si buscado es menor, recursivo para izquierda
            raiz.izq, x = eliminarCampo(raiz.izq, clave, campo)
        else:  # Si es mayor o igual
            if(raiz.info[campo] < clave):  # Si es mayor, recursivo a derecha
                raiz.der, x = eliminarCampo(raiz.der, clave, campo)
            else:  # Si es igual
                if (raiz.izq is None):  # Si no tiene rama izquierda
                    x = raiz.info       # Saca info y enlaza con única rama
                    raiz = raiz.der     # hijo. En este caso, derecha
                else:  # Si tiene rama izquierda
                    if(raiz.der is None):  # Si no tiene rama derecha
                        x = raiz.info      # obtiene dato y enlaza con unica
                        raiz = raiz.izq    # rama hijo, en este caso, derecha
                    else:  # Si tiene ambas ramas
                        raiz.izq, aux = reemplazar(raiz.izq)  # Busca de los número mas chicos, la hoja con el valor más alto. Esta elección fue arbitraría. Por también podría de los números más grandes, elegir el menor valor
                        raiz.info = aux.info  # Reemplaza el valor de ese nodo por el de la hoja que trajo
    return (raiz, x)


def nodoMin(raiz):
    '''Devuelve nodo con información más baja (nodo más a la izquierda)'''
    aux = raiz
    while aux.izq is not None:
        aux = aux.izq
    return aux


def nodoMax(raiz):
    '''Devuelve nodo con información más alta (nodo más a la derecha)'''
    aux = raiz
    while aux.der is not None:
        aux = aux.der
    return aux


def pesoArbol(raiz):
    '''Cantidad de nodos en el arbol'''
    if raiz is None:
        return 0
    else:
        return 1 + pesoArbol(raiz.izq) + pesoArbol(raiz.der)


def cantidadHojas(raiz):
    '''Cantidad de hojas en el arbol'''
    if raiz is not None:
        if (raiz.izq is None) and (raiz.der is None):
            return 1
        else:
            return cantidadHojas(raiz.izq) + cantidadHojas(raiz.der)
    else:
        return 0


def nodosEnNivel(raiz, nivel, nivel_act=0):
    '''Retorna la cantidad de nodos que hay en el nivel ingresado'''
    cant = 0
    if raiz is not None:
        if nivel == nivel_act:
            cant += 1
        nivel_act += 1
        cant += nodosEnNivel(raiz.izq, nivel, nivel_act)
        cant += nodosEnNivel(raiz.der, nivel, nivel_act)
        return cant
    else:
        return 0


def nodosEnAltura(raiz, altura):  # FALTA PROBAR ESTE
    '''Cantidad de nodos en altura seleccionada'''
    cont = 0
    if raiz is not None:
        if raiz.altura == altura:
            cont = 1
        cont += nodosEnAltura(raiz.izq, altura)
        cont += nodosEnAltura(raiz.der, altura)
        return cont
    else:
        return 0


def imprimirNivel(raiz, nivel, nivel_act=0):
    if raiz is not None:
        imprimirNivel(raiz.izq, nivel, nivel_act+1)
        if nivel == nivel_act:
            print(raiz.info)
        imprimirNivel(raiz.der, nivel, nivel_act+1)


def imprimirArbol(raiz, espacios=0):
    ''' Imprime arbol, girado hacia la izquierda'''
    if raiz is not None:
        espacios += 5
        imprimirArbol(raiz.der, espacios)
        print(" " * espacios, str(raiz.info))
        imprimirArbol(raiz.izq, espacios)


def recorridoArbolTodo(raiz, nivel=0):
    '''Recorre todo el arbol mostrando la información, altura y nivel'''
    if raiz is not None:
        recorridoArbolTodo(raiz.izq, nivel+1)
        print("Info ", raiz.info, "  Altura", raiz.altura, "  Nivel", nivel)
        recorridoArbolTodo(raiz.der, nivel+1)


def esHoja(raiz):
    if (raiz.izq is None) and (raiz.der is None):
        return True


def hijoIzq(raiz):
    return raiz.izq


def hijoDer(raiz):
    return raiz.der


def hijos(raiz):
    return raiz.izq, raiz.der


def nivelMax(raiz):
    return raiz.altura - 1


# ---------------------------------- #
#          GENERACIÓN ARBOL          #
# ---------------------------------- #

def arbolAleatorio(cantidad=randint(5, 20)):
    '''Crea un arbol aleatorio con la cantidad de elementos ingresada'''
    raiz = None
    for i in range(cantidad):
        raiz = insertar(raiz, randint(-100, 100))
    return raiz


def generarArbolPorNivel(niveles=0):
    '''Crea un arbol aleatorio con la cantidad de niveles ingresados'''
    ra = None
    ra = insertar(ra, randint(0, 100))

    while ra.altura-1 != niveles:
        ra = insertar(ra, randint(0, 100))
    
    return ra


def recortarArbol(raiz, bosque, hasta, nivel_act=0):
    '''Recorta el arbol y devulve bosque de los nodos del nivel deseado'''
    if raiz is not None and (nivel_act <= hasta):
        if nivel_act == hasta:
            bosque.append(raiz)
        recortarArbol(raiz.izq, bosque, hasta, nivel_act+1)
        recortarArbol(raiz.der, bosque, hasta, nivel_act+1)

#---------------------------------------------------#


def nivelLleno(raiz, nivel):
    '''Devuelve True si el nivel seleccionado está lleno'''
    return nodosEnNivel(raiz, nivel) == calcNodosNivel(nivel)


def calcNodosNivel(nivel):
    '''Calcula la cantidad de nodos que debería haber en el nivel para que
    esté completo'''
    return pow(2, nivel)


def arbolLleno(raiz):
    '''Devuelve True, si el ultimo nivel esta lleno'''
    nivel_mas_profundo = nivelMax(raiz)
    return nivelLleno(raiz, nivel_mas_profundo)


def determinarPadre(raiz, buscado):
    '''Devuelve el padre. Si es la raiz, devuelve el mismo valor. Si nodo
    encuentra el dato al que se está buscado, devuelve None'''
    aux = None
    if (raiz is not None):
        if raiz.info == buscado:
            aux = buscado
        elif (raiz.izq is not None and raiz.izq.info == buscado) or (raiz.der is not None and raiz.der.info == buscado):
            aux = raiz
        else:
            if (buscado < raiz.info):
                aux = determinarPadre(raiz.izq, buscado)
            else:
                aux = determinarPadre(raiz.der, buscado)
    return aux

          
# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
# ------------------- Funciones referidas a arbol de Huffman -----------------#
# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #


class NodoArbolHuffman():

    def __init__(self, valor, dato, izq=None, der=None):
        self.izq = izq
        self.der = der
        self.info = dato
        self.valor = valor


def crearArbolHuffman(tabla, comparacion=None):
    '''Devuelve la raiz de un arbol de huffman a partir de tabla de
    concurrencias dada'''
    # Nodo va a ser info, frec
    lista_nodos = []

    for item in tabla:
        nodo = NodoArbolHuffman(item[0], item[1])
        lista_nodos.append(nodo)

    while len(lista_nodos) > 1:
        nodo1 = lista_nodos.pop(0)
        nodo2 = lista_nodos.pop(0)
        
        frec_nueva = nodo1.valor + nodo2.valor
        nodo3 = NodoArbolHuffman(frec_nueva, None, nodo1, nodo2)
        lista_nodos.append(nodo3)

        if comparacion:
            lista_nodos.sort(key=comparacion)
        else:

            lista_nodos.sort(key=lambda x: x.valor)

    return lista_nodos[0]


def huffmanToDicCodificaciones(raiz, diccionario, codif=""):
    '''Transforma arbol de huffman en diccionario'''
    if not esHoja(raiz):
        if hijoIzq(raiz) is not None:
            huffmanToDicCodificaciones(raiz.izq, diccionario, codif+"0")
        if hijoDer(raiz) is not None:
            huffmanToDicCodificaciones(raiz.der, diccionario, codif+"1")
    else:
        diccionario.setdefault(raiz.info, codif)


def comprimir(arbol, mensaje):
    '''Comprime un mensaje en código binario, según arbol de huffman
    ingresado'''
    msj_codificado = ""
    dicc_codif = {}
    huffmanToDicCodificaciones(arbol, dicc_codif)

    for caracter in mensaje:
        msj_codificado += dicc_codif.get(caracter)
    return msj_codificado


def moverse(raiz, caracter):
    if caracter == "0":
        return raiz.izq
    else:
        return raiz.der


def decodificar(arbol, mensaje):
    '''Decodifica un mensaje, según parámetros de arbol de huffman ingresado'''
    msj_decodificado = ""
    raiz = arbol

    while len(mensaje) >= 1:
        while not esHoja(raiz):
            if len(mensaje) > 0:
                car = mensaje[0]
                mensaje = mensaje[1:]
            if car == "0":
                raiz = raiz.izq
            else:
                raiz = raiz.der
        msj_decodificado += raiz.info
        raiz = arbol

    return msj_decodificado

# ------------------------------------------------------------------------



# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
# ------------------- Funciones referidas a arbol n-ario----------------------#
# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #


class NodoNario(object):

    def __init__(self, info):
        self.info = info
        self.hijos = []


def esTitulo1(linea):
    return linea[:10].count(".") == 1


def esTitulo2(linea):
    return linea[:10].count(".") == 2


def esTitulo3(linea):
    return linea[:10].count(".") == 3


""" 
def busquedaNario(raiz, buscado):
    '''Busqueda iterativa, por si ocurren problemas al superar el stack de recursividad'''
    aux = None
    revisar = []
    
    # Si el arbol está vacío, retorno vacío, sino agrega en revisar y comienza el while
    if raiz is not None:
        revisar.append(raiz)
    else:
        return None
    
    while (len(revisar) > 0) and (aux is None):
        nodo = revisar.pop(0)
        if(nodo.info == buscado):
            aux = nodo
        else:
            for hijo in nodo.hijos:
                revisar.append(hijo)
    return aux
 """

def insertarNario(raiz, info_padre, info):
    '''Busca el nodo padre. Si lo encuentra, inserta el nodo hijo en él'''
    if raiz is None:
        raiz = NodoNario(info)
    else:
        nodo_padre = busquedaNario(raiz, info_padre)
    
        if nodo_padre:
            hijo = NodoNario(info)
            nodo_padre.hijos.append(hijo)
    
    return raiz


def busquedaNario(raiz, buscado, aux=None):
    '''Busqueda recursiva de un nodo'''
    
    if (raiz is not None) and (aux is None):
        if (raiz.info == buscado):
            aux = raiz
        else:
            for hijo in raiz.hijos:
                aux = busquedaNario(hijo, buscado, aux)
    return aux


def barridoNario(raiz):
    '''Realiza un recorrido e impresión del arbol nario'''
    if raiz is not None:
        print(raiz.info)
        for hijo in raiz.hijos:
            barridoNario(hijo)


def fileToNario(archivo):
    '''Retorna un arbol nario del archivo (con formato específico) pasado'''
    arbol = None
    pos = 0

    arbol = insertarNario(arbol, None, "INDICE")
    largo_archivo = len(archivo)

    ultimo_titulo1 = None
    ultimo_titulo2 = None


    while pos < largo_archivo:
        line = leer(archivo, pos)
        line = line.replace("\n", "")

        if esTitulo1(line):
            arbol = insertarNario(arbol, arbol.info, line)
            
            ultimo_titulo1 = line

        if esTitulo2(line):
            padre = ultimo_titulo1
            arbol = insertarNario(arbol, padre, line)
            
            ultimo_titulo2 = line

        if esTitulo3(line):
            padre = ultimo_titulo2
            arbol = insertarNario(arbol, padre, line)

        pos += 1
        line = leer(archivo, pos)

    return arbol


def narioToCola(arbol_n, cola):
    ''' Encola todos los nodos de un arbol nario. Util para luego realizar la transformación a Binario '''
    if arbol_n is not None:
        arribo(cola, arbol_n)

        for hijo in arbol_n.hijos:
            narioToCola(hijo, cola)


# ----------------------------------------------------------------------------#
# ----------------------------------------------------------------------------#
# --------------------Funciones referidas a transformada de knuth-------------#
# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #


def busquedaKnuth(raiz, buscado):
    '''Retorna el primer nodo cuya info sea igual a buscado'''
    aux = None
    if raiz is not None:
        if raiz.info == buscado:
            return raiz
        else:
            aux = busquedaKnuth(raiz.izq, buscado)
            if not aux:
                aux = busquedaKnuth(raiz.der, buscado)
    return aux


def busquedaCoincidenciasKnuth(raiz, buscado, lista_coincidencias=[]):
    '''Devuelve todos los nodos que contengan el buscado en su info'''
    if raiz is not None:
        if buscado in raiz.info:
            lista_coincidencias.append(raiz)
        busquedaCoincidenciasKnuth(raiz.izq, buscado, lista_coincidencias)
        busquedaCoincidenciasKnuth(raiz.der, buscado, lista_coincidencias)


def busquedaCampoKnuth(raiz, buscado, campo=0):
    '''Retorna el primer nodo cuya info de campo especificado sea igual a buscado'''
    aux = None
    if raiz is not None:
        if raiz.info[campo] == buscado:
            return raiz
        else:
            aux = busquedaCampoKnuth(raiz.izq, buscado, campo)
            if not aux:
                aux = busquedaCampoKnuth(raiz.der, buscado, campo)
    return aux


def getHijosEnlazados(nodo_nario):
    '''Retorna una lista de los nodos hijos, pero en vez de como nodoNario, como nodosarbol'''
    inicio, aux = None, None

    # Si tiene hijos, se extrae la data del primero y empaqueta en un nodo
    if len(nodo_nario.hijos) > 0:
        info_hijo = nodo_nario.hijos.pop(0).info
        nodo_b = NodoArbol(info_hijo)
        
        inicio = nodo_b
        aux = inicio

    # Si tiene más de un hijo, se extrae la data de todos y enlazan los nodos
    for hijo_restante in nodo_nario.hijos:
        info = hijo_restante.info
        nodo_b = NodoArbol(info)
        
        aux.der = nodo_b
        aux = nodo_b
    return inicio


def transformarKnuth(raiz_nario):
    '''Transformada Knuth. Transforma un arbol nario a uno binario'''
    arbol_k = NodoArbol(raiz_nario.info)
    cola = Cola()
    narioToCola(raiz_nario, cola)
    nodos_n = colaToList(cola)

    for nodo in nodos_n:
        hijos_puntero_inicio = getHijosEnlazados(nodo)
        
        if hijos:
            respuesta = busquedaKnuth(arbol_k, nodo.info)
            
            if respuesta:
                respuesta.izq = hijos_puntero_inicio

    return arbol_k


def barridoKnuth(arbol):
    '''Realiza un recorrido del arbol binario (knuth), imprimiendo el arbol en el orden'''
    if arbol is not None:
        print(arbol.info)
        barridoKnuth(arbol.izq)
        barridoKnuth(arbol.der)
    