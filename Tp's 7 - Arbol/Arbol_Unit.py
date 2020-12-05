'''
Archivo donde se almacenarán todos lo la mayoría de las funciones creadas
específicamente para los ejercicios del archivo Ejercicios.py. Exceptuando las que
están contenidas en TDA_Arbol y TDA_Archivo
'''
from sys import getsizeof
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
    alturas = [2.14, 2.03, 0.66, 1.75, 1.1, 1.67, 1.82, 1.83]
    pesos = [200, 136, 17, 73, 0.37, 85.2, 80, 78.2]
    
    for i in range(len(personajes)):
        nuevo_personaje = PersonajeStarWars(personajes[i], alturas[i], pesos[i])
        
        guardar(file_starwars, nuevo_personaje)


def extraerDataPersonajes(ruta):
    '''Devuelve array con los datos y la posición de cada personaje almacenado en el archivo'''
    archivo = abrir(ruta)
    array = []
    pos = 0
    while pos < len(archivo):
        data_personaje = [leer(archivo, pos), pos]
        array.append(data_personaje)
        pos += 1

    return array


def generarArbolPersonajesNombre(ruta):
    ''' Genera arbol de nombre de personajes a partir del array que se obtuvo al
    extraer la data del archivo'''

    data_personajes = extraerDataPersonajes(ruta)

    raiz = None

    for item in data_personajes:
        dato = [item[0].nombre, item[1]]
        raiz = insertarCampo(raiz, dato, 0)

    return raiz


def obtenerIndice(arbol, buscado):
    resultado = busquedaCampo(arbol, buscado, 0)
    if resultado:
        return resultado.info[1]
    else:
        return -1


def altaPersonaje(arbol, ruta_archivo):
    """Da de alta un personaje en el archivo y actualiza el arbol"""
    nombre = input('Ingrese el nombre del personaje: ')
    altura = float(input('Ingrese la altura del personaje: '))
    peso = float(input('Ingrese el peso del personaje: '))

    personaje = PersonajeStarWars(nombre, altura, peso)

    archivo = abrir(ruta_archivo)
    guardar(archivo, personaje)
    cerrar(archivo)
    
    arbol = generarArbolPersonajesNombre(ruta_archivo)
    
    return arbol


def modificarPersonaje(arbol, ruta_archivo):
    '''Busca un personaje, de encontrarlo, permite su modificación'''
    archivo = abrir(ruta_archivo)
    
    buscado = input("Nombre del personaje buscado: ")

    indice = obtenerIndice(arbol, buscado)

    if indice == -1:
        print("Personaje no encontrado")
    else:
        personaje = leer(archivo, indice)
        
        print("1- Nombre:", personaje.nombre)
        print("2- Altura:", personaje.altura)
        print("3- Peso:", personaje.peso)
        opcion = input("Seleccione campo a modificar: ")
        print()

        if (opcion in ["1", "2", "3"]):
            nuevo_valor = input("Nuevo valor: ")
            
            if opcion == "1":
                personaje.nombre = nuevo_valor
            elif opcion == "2":
                personaje.altura = float(nuevo_valor)
            elif opcion == "3":
                personaje.peso = float(nuevo_valor)
            
            modificar(archivo, personaje, indice)
            cerrar(archivo)
            
            arbol = generarArbolPersonajesNombre(ruta_archivo)
            print("Personaje Guardado")
        else:
            print("Opcion seleccionada incorrecta")

    return arbol


def bajaPersonaje(arbol, ruta_archivo):
    '''La la baja (lógica) de un personaje'''
    archivo = abrir(ruta_archivo)
    
    buscado = input("Nombre del personaje buscado: ")

    indice = obtenerIndice(arbol, buscado)

    if indice == -1:
        print("Personaje no encontrado")
    else:
        personaje = leer(archivo, indice)
        personaje.estado = False

        modificar(archivo, personaje, indice)
        cerrar(archivo)

        print("Personaje dado de baja")

        arbol = generarArbolPersonajesNombre(ruta_archivo)

    return arbol


def consultaPersonaje(arbol, buscado, ruta_archivo):
    archivo = abrir(ruta_archivo)

    indice = obtenerIndice(arbol, buscado)

    if indice == -1:
        print("El personaje buscado no se encuentra")
    else:
        personaje = leer(archivo, indice)
        print("Nombre:", personaje.nombre)
        print("Altura:", personaje.altura)
        print("Peso:", personaje.peso)
        print()
    

def listadoIndicesAltura(arbol, archivo):
    if arbol is not None:        
        listadoIndicesAltura(arbol.izq, archivo)

        indice = obtenerIndice(arbol, arbol.info[0])
        if indice != -1:
            personaje = leer(archivo, indice)
            if (personaje.estado) and (personaje.altura > 1):
                print("Nombre:", personaje.nombre)
                print("Altura:", personaje.altura)
                print("Peso:", personaje.peso)
                print()

        listadoIndicesAltura(arbol.der, archivo)


def listadoIndicesPeso(arbol, archivo):
    if arbol is not None:        
        listadoIndicesPeso(arbol.izq, archivo)

        indice = obtenerIndice(arbol, arbol.info[0])
        if indice != -1:
            personaje = leer(archivo, indice)
            if (personaje.estado) and (personaje.peso < 75):
                print("Nombre:", personaje.nombre)
                print("Altura:", personaje.altura)
                print("Peso:", personaje.peso)
                print()

        listadoIndicesPeso(arbol.der, archivo)


# EJERCICIO 15

def nanoMensaje():

    estado = choice(["Despejado", "Nublado", "Lluvia"])
    humedad = choice(["Baja", "Alta"])
    cod1 = str(choice([1, 2]))
    cod2 = str(choice([3, 5]))
    cod3 = str(choice([7, 8]))

    mensaje = estado + "-" + humedad + "-" + cod1 + "-" + cod2 + "-" + cod3

    return mensaje


def comprimirMedicion(arbol, mensaje):
    msj_codificado = ""
    dicc_codif = {}
    huffmanToDicCodificaciones(arbol, dicc_codif)

    segmentos = mensaje.split("-")

    for segmento in segmentos:
        
        msj_codificado += dicc_codif.get(segmento)

    return msj_codificado


def descomprimirMedicion(arbol, mensaje):
    segmentos = []
    raiz = arbol

    while len(mensaje) >= 1:
        while not esHoja(raiz):
            car = mensaje[0]
            mensaje = mensaje[1:]
            if car == "0":
                raiz = raiz.izq
            else:
                raiz = raiz.der
        segmentos.append(raiz.info[1])
        raiz = arbol

    return "-".join(segmentos)


def diferenciaTamano(trama1, trama2):
    tam1 = getsizeof(trama1)
    tam2 = getsizeof(trama2)

    return abs(tam1 - tam2)



# EJERCICIO 16

class Pokemon():

    def __init__(self, nombre="", nro=-1, tipos=[], debilidades=[]):
        self.nombre = nombre
        self.nro = nro
        self.tipos = tipos
        self.debilidades = debilidades


