'''
Archivo donde se almacenarán todos lo la mayoría de las funciones creadas
específicamente para los ejercicios del archivo Ejercicios.py. Exceptuando las que
están contenidas en TDA_Arbol y TDA_Archivo
'''

from TDA_Arbol import *
from random import randint, choice, uniform
from TDA_Archivo import abrir, cerrar, leer, guardar, modificar, barridoArchivo
from TDA_Archivo import txtToDat

# EJERCICIO 1


def repetido(raiz):
    if raiz is not None:
        if busqueda(raiz.izq, raiz.info) is not None:
            print("Se repite", raiz.info)
        if busqueda(raiz.der, raiz.info) is not None:
            print("Se repite:", raiz.info)
        repetido(raiz.izq)
        repetido(raiz.der)


def paresImpares(raiz):
    if raiz is not None:
        if raiz.info % 2 == 0:
            return (1 + paresImpares(raiz.izq)[0] + paresImpares(raiz.der)[0], 0 + paresImpares(raiz.izq)[1] + paresImpares(raiz.der)[1])
        else:
            return (0 + paresImpares(raiz.izq)[0] + paresImpares(raiz.der)[0], 1 + paresImpares(raiz.izq)[1] + paresImpares(raiz.der)[1])
    else:
        return 0, 0



# EJERCICIO 2

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


# EJERCICIO 5

def mostrarVillanos(raiz):
    if raiz is not None:
        mostrarVillanos(raiz.izq)
        if not raiz.info[1]:
            print(raiz.info)
        mostrarVillanos(raiz.der)


def mostrarC(raiz):
    if raiz is not None:
        mostrarC(raiz.izq)
        if (raiz.info[0][0] == "C") and (raiz.info[1]):
            print(raiz.info)
        mostrarC(raiz.der)


def contHeores(raiz):
    if raiz is not None:
        if raiz.info[1]:
            return 1 + contHeores(raiz.izq) + contHeores(raiz.der)
        else:
            return 0 + contHeores(raiz.izq) + contHeores(raiz.der)
    else:
        return 0



# EJERCICIO 10

def mostrarHojas(raiz):
    if raiz is not None:
        mostrarHojas(raiz.izq)
        if esHoja(raiz):
            print(raiz.info)
        mostrarHojas(raiz.der)


# EJERCICIO 12

def arbolDeci(ASIGNACIONES):
    ''' Genera arbol de decisiones para este ejercicio '''
    arbol = None
    for item in ASIGNACIONES:
        # Inserta pregunta
        arbol = insertarArbol2(arbol, item.get("mision"), item.get("peso"))
        # Inserta respuesta de si
        arbol = insertarArbol2(arbol, item.get("asignado"), item.get("peso")-500)

    return arbol


def busquedaHeroes(raiz, mision):
    aux = None

    if raiz is not None:
        if raiz.info == mision:
            aux = raiz.izq.info
        else:
            aux = busquedaHeroes(raiz.der, mision)
        
    return aux


def asignarHeroe(mision, arbol_dec):
    resultados = busquedaHeroes(arbol_dec, mision)

    return resultados


# EJERCICIO 13

def arbolMorse(lista_morse):
    raiz = Nodoarbol2(' ', 1650000)

    for item in lista_morse:
        raiz = insertarArbol2(raiz, item[0], item[1])
    return raiz


def desplazarse(raiz, digito):
    if digito == ".":
        return raiz.izq
    elif digito == "-":
        return raiz.der
    else:
        return None

def decodSegm(arbol, segmento):
    aux = arbol
    seg_decod = ""

    for digito in segmento:
        if digito == " ":
            seg_decod += aux.info
            aux = arbol
        else:
            aux = desplazarse(aux, digito)
    
    seg_decod += aux.info
    return seg_decod


def decodMsj(arbol, codigo):
    msj_decod = ""
    segmentos = codigo.split("/")

    for segmento in segmentos:
        msj_decod += decodSegm(arbol, segmento)

    return msj_decod


# EJERCICIO 14

class PersonajeStarWars():
    def __init__ (self, nombre="", altura=0, peso=0):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso
        self.estado = True


def initArchivoPersonajes(ruta):
    file_starwars = abrir(ruta)
    limpiar(file_starwars)
    personajes = ['Chewbacca', 'Darth Vader', 'Yoda', 'Luke Skywalker', 'R2-D2', 'C3PO', 'Obi-Wan Kenobi', 'Boba Fett']

    for personaje in personajes:
        altura = round(uniform(0.3, 5.2), 2)
        peso = round(uniform(1, 150),2)
        nuevo_personaje = PersonajeStarWars(personaje, altura, peso)
        guardar(file_starwars, nuevo_personaje)


def extraerDataPersonajes(ruta):
    '''Devuelve array con los datos y la posición de cada personaje almacenado en el archivo'''
    archivo = abrir(ruta)
    array = []
    pos = 0
    while pos < len(archivo):
        array.append([leer(archivo, pos), pos])
        pos += 1

    return array


def generarArbolPersonajesNombre(personajes):
    raiz = None

    for item in personajes:
        dato = [item[0].nombre, item[1]]
        raiz = insertarCampo(raiz, dato, 0)

    return raiz




# EJERCICIO 3
# EJERCICIO 3
# EJERCICIO 3
# EJERCICIO 3
# EJERCICIO 3
# EJERCICIO 3
# EJERCICIO 3
# EJERCICIO 3