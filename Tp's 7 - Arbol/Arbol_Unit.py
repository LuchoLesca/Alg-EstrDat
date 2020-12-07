'''
Archivo donde se almacenarán todos lo la mayoría de las funciones creadas
específicamente para los ejercicios del archivo Ejercicios.py. Exceptuando las que
están contenidas en TDA_Arbol y TDA_Archivo
'''
import json
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

    def __str__(self):
        return "Nombre: " + str(self.nombre) + " -  Nro: " + str(self.nro) + " -  Tipo/s:" + str(self.tipos) + " -  Debilidad/es:" + str(self.debilidades)

def initFilePokemon():
    ruta_json = "Pokemons/pokemon.json"
    ruta_file = "Pokemons/pokemons"
 
    a = abrir(ruta_file)
    limpiar(a)
    cerrar(a)

    jsonToFile(ruta_json, ruta_file)


def obtenerTipos(pokemon):
    tipos = [pokemon.get("type1"), pokemon.get("type2")]
    return tipos


def obtenerDebilidades(pokemon):
    nombres_deb = ["against_bug","against_dark","against_dragon","against_electric","against_fairy","against_fight","against_fire","against_flying","against_ghost","against_grass","against_ground","against_ice","against_normal","against_poison","against_psychic","against_rock","against_steel","against_water"]
    
    # Selecciona las debilidades (son las que tienen valor mayor a 2 en el json)
    lista_deb = []
    for deb in nombres_deb:
        valor = pokemon.get(deb)
        # Si es debilidad, almacena en la lista, eliminando el "against_"
        if (valor == 2):
            lista_deb.append(deb.replace("against_", ""))
    return lista_deb


def jsonToFile(ruta_json, ruta_file):
    '''Extra datos de .json y guarda en archivo, para trabajar con él'''
    with open(ruta_json, "r") as read_file:
        pokemons = json.load(read_file)

    archivo = abrir(ruta_file)

    for pokemon in pokemons:
        nombre = pokemon.get("name")
        nro = pokemon.get("pokedex_number")        
        tipos = obtenerTipos(pokemon)
        debilidades = obtenerDebilidades(pokemon)

        nuevo_pokemon = Pokemon(nombre, nro, tipos, debilidades)

        guardar(archivo, nuevo_pokemon)


def extraerDataPokemons(ruta):
    '''Devuelve array con los datos y la posición de cada pokemon almacenado en el archivo'''
    archivo = abrir(ruta)
    array = []
    pos = 0
    while pos < len(archivo):
        data_personaje = [leer(archivo, pos), pos]
        array.append(data_personaje)
        pos += 1
    cerrar(archivo)
    return array


def generarArbolPoke(ruta_file, tipo_gen):
    '''Genera un arbol binario de pokemons, ordenandolos por tipo de generacion pasada'''
    raiz = None
    dataPokemons = extraerDataPokemons(ruta_file)

    for item in dataPokemons:
        pokemon = item[0]
        indice = item[1]

        if tipo_gen == "nombre":
            dato = pokemon.nombre
        elif tipo_gen == "nro":
            dato = pokemon.nro
        elif tipo_gen == "tipo":
            dato = pokemon.tipos

        nuevo_pokemon = [dato, indice]
        raiz = insertarCampo(raiz, nuevo_pokemon, 0)

    return raiz


def obtenerIndicesPorNombre(raiz, buscado, resultados_arbol):
    '''Realiza busqueda por proximidad por campo seleccionado
    Devuelve los pares [dato, indice] de cada uno'''
    if (raiz is not None):
        if (buscado.lower() in raiz.info[0].lower()):
            resultados_arbol.append(raiz.info[1])
        obtenerIndicesPorNombre(raiz.izq, buscado, resultados_arbol)
        obtenerIndicesPorNombre(raiz.der, buscado, resultados_arbol)


def listaPokemonsNombre(ruta_file, raiz, nombre_buscado):
    '''Devuelve lista de pokemons que haya encontrado por proximidad'''
    indices_poke_a_obtener_data = []
    # En el arbol por nombre, se busca por proximidad, y se devuelve los indices de quienes coincidan
    obtenerIndicesPorNombre(raiz, nombre_buscado, indices_poke_a_obtener_data)

    # Por cada indice, se busca en el archivo y trae el objeto Pokemon del susodicho
    datos_pokemons = []

    archivo = abrir(ruta_file)
    for indice in indices_poke_a_obtener_data:
        datos_pokemons.append(leer(archivo, indice))
    cerrar(archivo)

    return datos_pokemons


def busquedaNroPoke(ruta_file, raiz, nro_buscado):
    '''Devuelve pokemon que haya encontrado con nro de pokedex solicitado'''
    pokemon = None

    encontrado = busquedaCampo(raiz, nro_buscado, 0)
    if encontrado:
        indice = encontrado.info[1]

        archivo = abrir(ruta_file)
        pokemon = leer(archivo, indice)
        cerrar(archivo)

    return pokemon


def busqTipos(raiz, tipo_buscado, lista=[]):
    '''Devuelve lista de indices de pokemons que sean del tipo indicado'''
    if (raiz is not None):
        if (tipo_buscado in raiz.info[0]):
            lista.append(raiz.info[1])
        busqTipos(raiz.izq, tipo_buscado, lista)
        busqTipos(raiz.der, tipo_buscado, lista)


def listaBusquedaTipoArbol(ruta, arbol, tipo):
    '''Devuelve lista de pokemons del tipo especificado, traidos desde el archivo'''
    lista = []
    
    indices_pokemon_tipo = []
    busqTipos(arbol, tipo, indices_pokemon_tipo)

    archivo = abrir(ruta)
    for indice in indices_pokemon_tipo:
        lista.append(leer(archivo, indice))
    cerrar(archivo)

    return lista



# EJERCICIO 17

def generarReporteAleatorio(codigo=0):
    generales = ["Kylo Ren", "Hux", "Phasma"]
    tipos_soldados = ["Imperial Stromtrooper", "Imperial Scout Trooper", "Imprerial Death Trooper", "Sith Trooper", "First Order Stromtrooper"]
    fechas = [ "1/02/2019",
                "23/11/2018",
                "4/4/2006",
                "13/9/2010",
                "7/7/2013",
                "30/12/2015"
            ]    
    
    general = choice(generales)
    fecha = choice(fechas)
    estado = choice([True, False])
    tipo_soldado = choice(tipos_soldados)

    return [general, fecha, codigo, estado, tipo_soldado]


def obtenerMismoNombre(arbol, nombre, lista):
    '''A partir de un indice del arbol, se expande. Devolviendo lista de
    todos quienes tengan el mismo valor (nombre, en este caso)'''
    if (arbol is not None) and (arbol.info[0] == nombre):
        lista.append(arbol.info)
        obtenerMismoNombre(arbol.izq, nombre, lista)
        obtenerMismoNombre(arbol.der, nombre, lista)


def listadoPorNombre(arbol, nombre):
    '''Busca el indice con el nombre, y luego se exapande, encontrando en el
    arbol los que posean el mismo nombre. Devuelve un array de estos'''
    puntero_resultado = busquedaCampo(arbol, nombre, 0)
    listado = []
    if puntero_resultado:
        obtenerMismoNombre(puntero_resultado, nombre, listado)
    return listado


def armasFalladasPorGeneral(arbol):
    generales = ["Kylo Ren", "Hux", "Phasma"]

    for general in generales:
        reportes = listadoPorNombre(arbol, general)

        falladas = 0
        for reporte in reportes:
            if reporte[3]:
                falladas += 1
        
        print("Armas falladas por general", general, ":", falladas)


def soldadosCantidadPorGeneral(arbol, general):
    tipos_soldados = ["Imperial Stromtrooper", "Imperial Scout Trooper", "Imprerial Death Trooper", "Sith Trooper", "First Order Stromtrooper"]

    reportes_general = listadoPorNombre(arbol, general)

    # Almacena clave soldado-cantidad
    soldado_cantidad = {}
    for soldado in tipos_soldados:
        soldado_cantidad.setdefault(str(soldado), 0)

    for reporte in reportes_general:
        soldado = reporte[4]

        soldado_cantidad[soldado] += 1

    print(soldado_cantidad)


def cantidadSoldados(arbol, soldado, cant_soldado=0, cant_fallas=0):
    if arbol is not None:
        cant_soldado, cant_fallas = cantidadSoldados(arbol.izq, soldado, cant_soldado, cant_fallas)
        if arbol.info[4] == soldado:
            if arbol.info[3]:
                cant_fallas += 1
            cant_soldado += 1
        cant_soldado, cant_fallas = cantidadSoldados(arbol.der, soldado, cant_soldado, cant_fallas)
    return cant_soldado, cant_fallas


def determinarSithyFallas(arbol):    
    cant_sith, cant_fallas = cantidadSoldados(arbol, "Sith Trooper")

    print("Cantidad Sith en misiones:", cant_sith)
    print("Cant de Sith a quienes le fallaron las armas:", cant_fallas)

        
def obtenerMismaFecha(arbol, fecha, lista):
    '''A partir de un indice del arbol, se expande. Devolviendo lista de
    todos quienes tengan el mismo valor (fecha, en este caso)'''
    if (arbol is not None) and (arbol.info[1] == fecha):
        lista.append(arbol.info)
        obtenerMismaFecha(arbol.izq, fecha, lista)
        obtenerMismaFecha(arbol.der, fecha, lista)


def listadoPorFecha(arbol, fecha):
    '''Busca el indice con la fecha, y luego se exapande, encontrando en el
    arbol los que posean la misma fecha. Devuelve un array de estos'''
    puntero_resultado = busquedaCampo(arbol, fecha, 1)
    listado = []
    if puntero_resultado:
        obtenerMismaFecha(puntero_resultado, fecha, listado)
    return listado


def codigoDeMisionesFecha(arbol, fecha_buscada):

    listado_reportes_fecha = listadoPorFecha(arbol, fecha_buscada)

    print("Códigos de blasters de las misiones en la fecha:", fecha_buscada)
    for reporte in listado_reportes_fecha:
        print(reporte[2])

    cant_fallas = 0
    for reporte in listado_reportes_fecha:
        if reporte[3]:
            cant_fallas += 1

    print("Porcentaje  de estas que fallaron:", (cant_fallas * 100) / len(listado_reportes_fecha))


# EJERCICIO 18