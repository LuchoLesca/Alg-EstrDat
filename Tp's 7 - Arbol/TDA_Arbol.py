# Árbol Estricto: Si un subárbol está vacío, el otro también. Cada nodo puede
# tener 0 ó 2 hijos.

# Árbol Lleno: Árbol estricto donde en cada nodo la altura del subárbol
# izquierdo es igual a la del derecho, y ambos subárboles son árboles llenos.

# Árbol Completo: Árbol lleno hasta el penúltimo nivel. En el último nivel los
# nodos están agrupados a la izquierda.
from TDA_Lista import Lista, NodoLista
from random import randint


class Nodoarbol():

    def __init__(self, dato, izq=None, der=None):
        self.izq = izq
        self.der = der
        self.altura = 0
        self.info = dato


def altura(raiz):
    if (raiz is None):
        return 0
    else:
        return raiz.altura


def actualizarAltura(raiz):
    if (altura(raiz.izq) > altura(raiz.der)):
        raiz.altura = altura(raiz.izq) + 1
    else:
        raiz.altura = altura(raiz.der) + 1
    return raiz


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
        raiz = Nodoarbol(dato)
    else:
        if (dato < raiz.info):
            raiz.izq = insertar(raiz.izq, dato)
        else:
            raiz.der = insertar(raiz.der, dato)

    actualizarAltura(raiz)
    raiz = balancear(raiz)

    return(raiz)


def arbolVacio(raiz):
    return (raiz is None)


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


def reemplazar(raiz):  # Va hasta la derecha, hasta que no tenga raiz derecha
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
                        raiz.izq, aux = reemplazar(raiz.izq)  # Busca de los número mas chicos, la hoja con el valor más alto
                        raiz.info = aux.info  # Reemplaza el valor de ese nodo por el de la hoja que trajo
    return(raiz, x)


def nodoMin(raiz):
    aux = raiz
    while aux.izq is not None:
        aux = aux.izq
    return aux


def nodoMax(raiz):
    aux = raiz
    while aux.der is not None:
        aux = aux.der
    return aux


def pesoArbol(raiz):
    '''Cantidad de nodos en el arbol'''
    if raiz is not None:
        return 1 + pesoArbol(raiz.izq) + pesoArbol(raiz.der)
    else:
        return 0


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


def recortarArbol(raiz, bosque, hasta, nivel_act=0):
    '''Recorta el arbol y devulve bosque de los nodos del nivel deseado'''
    if raiz is not None and (nivel_act <= hasta):
        if nivel_act == hasta:
            bosque.append(raiz)
        recortarArbol(raiz.izq, bosque, hasta, nivel_act+1)
        recortarArbol(raiz.der, bosque, hasta, nivel_act+1)


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


def arbolAleatorio(cantidad=randint(5, 20)):
    '''Crea un arbol aleatorio de la cantidad ingresada'''
    raiz = None
    for i in range(cantidad):
        raiz = insertar(raiz, randint(-100, 100))
    return raiz


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


def eliminarHuffman(l):
    aux = None
    if l.tamanio >= 1:
        aux = l.inicio
        l.inicio = l.inicio.sig
        l.tamanio -= 1
    return aux.info


# ------------------- Funciones referidas a arbol de Huffman -----------------
def insertarHuffman(l, nodoarbol):
    '''Inserta nuevo nodo en lista de nodosarbol'''
    nodo = NodoLista()
    nodo.info = nodoarbol

    if (l.inicio is None) or (nodo.info.info[0] < l.inicio.info.info[0]):
        nodo.sig = l.inicio
        l.inicio = nodo
    else:  # Si va al medio o a lo último
        anterior = l.inicio
        actual = l.inicio.sig
        while (actual is not None) and (actual.info.info[0] <= nodo.info.info[0]):
            actual = actual.sig
            anterior = anterior.sig
        nodo.sig = actual
        anterior.sig = nodo
    l.tamanio += 1


def tablaToListaNodos(tabla):
    '''Transforma tabla ingresada en lista de nodos arbol'''
    tabla.sort(key=lambda x: x[0])

    lista_nodos = Lista()

    for elemento in tabla:
        insertarHuffman(lista_nodos, Nodoarbol(elemento))

    return lista_nodos


def crearArbolHuffman(tabla):
    '''Devuelve la raiz de un arbol de huffman a partir de tabla de
    concurrencias dada'''

    lista_nodos = tablaToListaNodos(tabla)

    while lista_nodos.tamanio > 1:
        nod1 = eliminarHuffman(lista_nodos)
        nod2 = eliminarHuffman(lista_nodos)
        info_nueva = [(nod1.info[0]+nod2.info[0]), None]
        nod3 = Nodoarbol(info_nueva, nod1, nod2)

        insertarHuffman(lista_nodos, nod3)

    return lista_nodos.inicio.info

# ------------------------------------------------------------------------
