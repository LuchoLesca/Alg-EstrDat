from TDA_Arbol import *
from random import randint, choice
import TDA_Lista as Lista
import locale
from TDA_Archivo import abrir, cerrar, leer, guardar, modificar, barridoArchivo
import queue


r = None

# EJERCICIO 1  HECHO

# A

# for i in range(randint(5, 10)):
#    num = randint(0, 50)
#    lista_numeros.append(num)
#    r = insertar(r, num)

# print("Lista de números ingresados", lista_numeros)
# 20, 29, 11, 41, 32, 72, 99, 50, 65, 91

r = insertar(r, 20)
r = insertar(r, 29)
r = insertar(r, 11)
r = insertar(r, 41)
r = insertar(r, 32)
r = insertar(r, 72)
r = insertar(r, 99)
r = insertar(r, 50)
r = insertar(r, 65)
r = insertar(r, 91)


"""
print()
print("Preorden")
preorden(r)
print()

print("Inorden")
inorden(r)
print()

print("Postorden")
postorden(r)
print()


imprimirArbol(r)
"""
# B
"""
buscado = lista_numeros[0]
# buscado = 100

resultado = busqueda(r, buscado)

if resultado is None:
    print("El elemento " + str(buscado) + " no está en el arbol")
else:
    print("El elemento " + str(buscado) + " se encuentra en el arbol")
"""
# C
"""
print()
print("ELiminados: ")
for i in range(3):
    num = lista_numeros[i]
    eliminar(r, num)
    print(lista_numeros[i])

print()
print("Arbol inorden")
inorden(r)
"""

# D
"""
print("Altura de sub arbol izquierdo: ", altura(r.izq))
print("Altura de sub arbol derecho: ", altura(r.der))
"""

# E
"""
r = insertar(r, 20)
r = insertar(r, 29)
r = insertar(r, 11)

imprimirArbol(r)


def repetido(raiz):
    if raiz is not None:
        if busqueda(raiz.izq, raiz.info) is not None:
            print("Se repite", raiz.info)
        if busqueda(raiz.der, raiz.info) is not None:
            print("Se repite:", raiz.info)
        repetido(raiz.izq)
        repetido(raiz.der)


print()
repetido(r)
"""

# F
"""
imprimirArbol(r)


def paresImpares(raiz):
    if raiz is not None:
        if raiz.info % 2 == 0:
            return (1 + paresImpares(raiz.izq)[0] + paresImpares(raiz.der)[0], 0 + paresImpares(raiz.izq)[1] + paresImpares(raiz.der)[1])
        else:
            return (0 + paresImpares(raiz.izq)[0] + paresImpares(raiz.der)[0], 1 + paresImpares(raiz.izq)[1] + paresImpares(raiz.der)[1])
    else:
        return 0, 0


print()
pares, impares = paresImpares(r)
print("Pares:", pares, "Impares:", impares)
"""

# EJERCICIO 2   HECHO

"""

def operacion(operador, izq, der):
    resultado = 0
    if operador == "+":
        resultado = izq + der
    elif operador == "-":
        resultado = izq - der
    elif operador == "*":
        resultado = izq * der
    elif operador == "/":
        resultado = izq / der

    return resultado


def calcular(raiz):
    if esHoja(raiz):
        return raiz.info
    else:
        return operacion(raiz.info, calcular(raiz.izq), calcular(raiz.der))


def arbolPruebaA(r=None):
    # Expresión 1
    # Expresión original: ((2 + 3) * 4) + 26

    r = Nodoarbol("+")
    r.der = Nodoarbol(26)
    r.izq = Nodoarbol("*")
    r.izq.der = Nodoarbol(4)
    r.izq.izq = Nodoarbol("+")
    r.izq.izq.izq = Nodoarbol(2)
    r.izq.izq.der = Nodoarbol(3)

    return r


def arbolPruebaB(r=None):

    # Expresión 2
    # Expresión original: (((2*7) + 8) / 5) / ((4*(-1)) - 3)

    r = Nodoarbol("/")

    r.der = Nodoarbol("-")
    r.der.der = Nodoarbol(3)
    r.der.izq = Nodoarbol("*")
    r.der.izq.izq = Nodoarbol(4)
    r.der.izq.der = Nodoarbol(-1)

    r.izq = Nodoarbol("/")
    r.izq.izq = Nodoarbol("+")
    r.izq.der = Nodoarbol(5)
    r.izq.izq.izq = Nodoarbol(8)
    r.izq.izq.der = Nodoarbol("*")
    r.izq.izq.der.izq = Nodoarbol(2)
    r.izq.izq.der.der = Nodoarbol(7)

    return r


raiz1 = arbolPruebaA()
raiz2 = arbolPruebaB()
"""
# A
"""
print()
print("En forma de prefijo:")
preorden(r)
print()
print("En orden pero sin paréntesis")
inorden(r)
print()
print("En orden de postfijo")
postorden(r)
print()
print("El barrido inorden muestra la expresión en el orden correcto")
"""

# B
"""
print()
imprimirArbol(raiz1)
print("Resultado:\n", calcular(raiz1))

print()
print()
print()

imprimirArbol(raiz2)
print("Resultado:\n", calcular(raiz2))
"""

# EJERCICIO 3   <<<< PENDIENTES HASTA QUE ME PASEN LOS PSEUDOCÓDIGOS

"""
class NodoarbolM():
    info, hijos = None, Lista.Lista()


def hijoDer(raiz, nodo):  # No entendí la letra
    if raiz is not None:
        if busqueda(nodo.info) is not None:
            x = nodo
            aux = nodo.der


def cargarHijos(raiz, padre):  # No entendí la letra
    aux = buscar(raiz, padre)
    if aux is not None:
        while True:  # Aca hay que cambiar la condicion, preguntar a Mari
            # leer(nombre_hijo)
            insertar_lista(aux.hijos, nombre_hijo)
            # ACtualizar condicion del mientras


def transformar(AM, AB=None):
    if AM is not None:
        if AB is None:
            AB = Nodoarbol(AM.info)

        while not Lista.lista_vacia(AM.hijos):
            aux = Lista.eliminar(AM.hijos, AM.hijos.inicio.info)
            if AB.izq is None:
                AB.izq = Nodoarbol(aux.info)
                transformar(aux, AB.izq)
            else:
                aux = AB.izq.der
                while aux is not None:
                    aux = aux.der
                aux.der = Nodoarbol(aux.info)
                transformar(aux, aux.der)
"""


"""

def esNum(car):
    return car.isnumeric()


def esTitulo1(linea):
    if linea[:8].count(".") == 1:
        return True
    else:
        return False


def esTitulo2(linea):
    if linea[:8].count(".") == 2:
        return True
    else:
        return False


def esTitulo3(linea):
    if linea[:8].count(".") == 3:
        return True
    else:
        return False


archivo_indice = open('Indice_Summerville.txt', mode='r', encoding='utf-8')
r = "Indice"

for linea in archivo_indice:
    #if (len(linea) > 1) and (esTitulo2(linea)):
    #    print(linea)
"""

# EJERCICIO 4  HECHO
"""
def arbolIzquierdo(raiz):
    return raiz.izq


def arbolDerecho(raiz):
    return raiz.der


print("Arbol original")
imprimirArbol(r)

print()
print("Arbol izquierdo")
imprimirArbol(arbolIzquierdo(r))

print()
print("Arbol derecho")
imprimirArbol(arbolDerecho(r))
"""

# EJERCICIO 5  HECHO

# A
"""
heroes = ["Capitan America", "Iron Man", "Thor", "Hulk", "Black Widow",
          "Hawkeye", "Vision", "Dotor Strange", "Groot", "Spider-man"]
villanos = ["Thanos", "Yellowjacket", "Ultron", "Red Skull", "Iron Monger",
            "Loki", "Vulture", "Whiplash", "Crossbones", "The Mandarin"]


r = None
for i in range(10):
    r = insertar(r, [heroes[i], True])
    r = insertar(r, [villanos[i], False])
"""

# B

"""
def mostrarVillanos(raiz):
    if raiz is not None:
        mostrarVillanos(raiz.izq)
        if not raiz.info[1]:
            print(raiz.info)
        mostrarVillanos(raiz.der)


print()
print("Villanos ordenados alfabeticamente:")
mostrarVillanos(r)
"""
# C

"""
def mostrarC(raiz):
    if raiz is not None:
        mostrarC(raiz.izq)
        if (raiz.info[0][0] == "C") and (raiz.info[1]):
            print(raiz.info)
        mostrarC(raiz.der)


print()
print("Superheroes que empiezan con C")
mostrarC(r)
"""

# D

"""
def contHeores(raiz):
    if raiz is not None:
        if raiz.info[1]:
            return 1 + contHeores(raiz.izq) + contHeores(raiz.der)
        else:
            return 0 + contHeores(raiz.izq) + contHeores(raiz.der)
    else:
        return 0


print()
print("La cantidad de heroes en el arbol es de:", contHeores(r))
"""

# E
"""
busc = "Strange"
buscado = busquedaProximidadCampo(r, busc, 0)
if buscado is not None:
    nombre_ant = buscado.info[0]
    buscado.info[0] = "Dr. Strange"
    print("El personaje buscado " + busc + " se encontró y se modificó su")
    print("nombre de " + nombre_ant + " a " + buscado.info[0])
else:
    print("No se encontró el personaje por busqueda por proximidad")

print()
inorden(r)
"""

# F
"""
invInorden(r)
"""

# G
"""
bosque = [None, None]  # 0: arbol heroes. 1: arbol villanos


def insertarHeroe(heroe):
    bosque[0] = insertar(bosque[0], heroe)


def insertarVillano(villano):
    bosque[1] = insertar(bosque[1], villano)


def serpararHeroesVillanos(raiz):
    if raiz is not None:
        serpararHeroesVillanos(raiz.izq)
        serpararHeroesVillanos(raiz.der)
        if raiz.info[1]:
            insertarHeroe(raiz.info)
        else:
            insertarVillano(raiz.info)


inorden(r)

# I
print()
print("Cantidad de nodos por arbol:")
print("Héroes:", pesoArbol(bosque[0]))
print("Villanos:", pesoArbol(bosque[1]))

# II
print()
print("Arbol de heroes")
serpararHeroesVillanos(r)
inorden(bosque[0])
print()
print("Arbol de villanos:")
inorden(bosque[1])

"""
# EJERCICIO 6 <<<<<<<<<<<<<<<<<


# EJERCICIO 7   HECHO
"""
imprimirArbol(r)
print()
print("Info de nodo minimo", nodoMin(r).info)
print("Info de nodo máximo", nodoMax(r).info)
"""


# EJERCICIO 8


# TABLA DE FRECUENCIAS
"""
tabla = {"A": 0.2, "F": 0.17, "1": 0.13, "3": 0.21, "0": 0.05, "M": 0.09,
         "T": 0.15}
"""
"""
tabla = [["A", 0.2], ["F", 0.17], ["1", 0.13], ["3", 0.21], ["0", 0.05],
         ["M", 0.09], ["T", 0.15]]

# ORDENA TABLA DE FRECUENCIAS SEGÚN PARÁMETRO
parametro = 1
tabla.sort(key=lambda x: x[1])


def crearArbolHuffman(lista):
    while(len(lista) >= 2):
        nod1 = lista.pop()
        nod2 = lista.pop()
        nuevo_nodo = Nodoarbol(nod1.info[1] + nod2.info[1], nod1, nod2)
        lista.append(nuevo_nodo)
        lista.sort()
        lista.reverse()
    return lista.pop()
"""

# Con tipo de lista del TDA
"""
lista = Lista.Lista()

Lista.inserCampo(lista, ["A", 0.2], 1)
Lista.inserCampo(lista, ["F", 0.17], 1)
Lista.inserCampo(lista, ["1", 0.13], 1)
Lista.inserCampo(lista, ["3", 0.21], 1)
Lista.inserCampo(lista, ["0", 0.05], 1)
Lista.inserCampo(lista, ["M", 0.09], 1)
Lista.inserCampo(lista, ["T", 0.15], 1)


Lista.barridoLista(lista)
"""

"""
def crearTabla(palabra):
    '''Devuelve una tabla de pares de caracteres y peso, por cada dígito de
    la palabra ingresada'''
    tabla_aux = []
    largo_total = len(palabra)

    for letra in palabra:
        peso = palabra.count(letra)/largo_total
        peso = round(peso, 3)

        if [letra, peso] not in tabla_aux:
            tabla_aux.append([letra, peso])

    tabla_aux.sort(key=lambda x: x[1])
    return tabla_aux


pal = "Allá en la fuenta había un chorrito, se hacía grandote, se hacía chiquito"
tabla = crearTabla(pal)


def comprimir(palabra):
    pass


def descomprimir():
    pass
"""


# EJERCICIO 9   # HECHO Y PROBADO
"""
def calcNodosNivel(nivel):
    '''Calcula la cantidad de nodos que debería haber en el nivel para que
    esté completo'''
    return pow(2, nivel)


imprimirArbol(r)

# PRUEBA DE CALCULAR NODO POR NIVEL
for i in range(4):  # Dondei representa a cada nivel
    cant_nodos = nodosEnNivel(r, i)
    deberia_haber = calcNodosNivel(i)
    print("Nivel:", i, " Debería haber", deberia_haber, " Hay:", cant_nodos,
          " Faltan:", int(deberia_haber - cant_nodos))
"""

# EJERCICIO 10

# imprimirArbol(r)

# A
"""
print("Cantidad de nodos en el arbol:", pesoArbol(r))
"""
# B
"""
print("Cantidad de hojas:", cantidadHojas(r))
"""
# C
"""
def mostrarHojas(raiz):
    if raiz is not None:
        mostrarHojas(raiz.izq)
        if esHoja(raiz):
            print(raiz.info)
        mostrarHojas(raiz.der)


print("Información de los nodos hojas")
mostrarHojas(r)
"""
# D  <<<< falta este. Determinarlo agregando atributo, o pasado un dato buscarlo?

# E
"""
print("Altura de arbol:", r.altura)
"""


# EJERCICIO 11    Falta terminar todo esto también

"""
def generarArbol(niveles):
    raiz = None
    raiz = insertar(raiz, randint(0, 100))
    while raiz.altura <= niveles:
        raiz = insertar(raiz, randint(0, 100))
    return raiz


r = generarArbol(9)


imprimirArbol(r)
"""
# A
"""# Crea bosque y recorta arbol en nivel deseado
nivel_a_cortar = 3
bosque = []
recortarArbol(r, bosque, nivel_a_cortar)
"""
# B
"""# Muestras los nodos que hay en el bosque
print()
print("Raices")
for arbol in bosque:
    print("Raiz:", arbol.info, " Cantidad de nodos:", pesoArbol(arbol))
"""
# C
"""
for i in range(len(bosque)):
    print()
    print("Barrido arbol " + str(i+1))
    preorden(bosque[i])

"""
# D
"""
if len(bosque) == 0:
    print("No hay arboles en el bosque")
else:
    mayor = bosque[0]
    cant = pesoArbol(mayor)
    for arbol in bosque:
        if cant <= pesoArbol(arbol):
            mayor = arbol
            cant = pesoArbol(arbol)


print()
print("Raiz de arbol más pesado", mayor.info, " Cantidad de nodos", cant)
"""

# E     <<<<< Falta este




# EJERCICIO 12
