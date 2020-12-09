import json
from TDA_Arbol import *
from Arbol_Unit import *
from random import randint, choice, uniform
from TDA_Archivo import abrir, cerrar, leer, guardar, modificar, barridoArchivo
from TDA_Archivo import txtToDat

""" 
r = None  # Importante no eliminar esta variable, ya que se usará como raíz para la mayoría de los ejercicios

lista_numeros = [20, 29, 11, 41, 32, 72, 99, 50, 65, 91]

for i in range(randint(5, 10)):
   num = randint(0, 50)
   lista_numeros.append(num)
   r = insertar(r, num)
 """
# print("Lista de números ingresados", lista_numeros)
# 20, 29, 11, 41, 32, 72, 99, 50, 65, 91
""" 
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
# EJERCICIO 1

# A
""" 
r = arbolAleatorio(10)

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
# buscado = lista_numeros[0]  # este debería necontrarlo
# buscado = 100  # Este no debería encontrarlo

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

print()
repetido(r)
"""

# F
"""
imprimirArbol(r)

print()
pares, impares = paresImpares(r)
print("Pares:", pares, "Impares:", impares)
"""

# EJERCICIO 2

""" 
raiz1 = arbolPruebaA()
raiz2 = arbolPruebaB()
 """
# A

""" 
print()
print("En forma de prefijo:")
preorden(raiz1)
print()
print("En orden pero sin paréntesis")
inorden(raiz1)
print()
print("En orden de postfijo")
postorden(raiz1)
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

# EJERCICIO 3

# txtToDat("Indices/indice_summerville.txt", "Indices/indice_summerville")

a_indices = abrir("Indices/indice_summerville")
aknuth = fileToBinaryTree(a_indices)
cerrar(a_indices)

# A

barridoKnuth(aknuth)


# B


def busquedaKnuthCampo(raiz, buscado, campo):
    pass






# EJERCICIO 4
""" 
r = arbolAleatorio(10)

print("Arbol original")
imprimirArbol(r)

print()
print("Arbol izquierdo")
imprimirArbol(hijoIzq(r))

print()
print("Arbol derecho")
imprimirArbol(hijoDer(r))
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
print()
print("Villanos ordenados alfabeticamente:")
mostrarVillanos(r)
 """
# C

""" 
print()
print("Superheroes que empiezan con C")
mostrarC(r)
 """

# D

""" 
print()
print("La cantidad de heroes en el arbol es de:", contHeores(r))
 """

# E
""" 
print("Previo a busqueda y modificacion")
inorden(r)

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
print("Luego busqueda y modificacion")
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
# EJERCICIO 6

""" 
indice_archivos = [["arduino"], ["documentos"], ["libros"], ["escritorio"],
                   ["imagenes"], ["musica"], ["nodeProjects"], ["plantillas"],
                   ["prueba_cluster"], ["PythonProyects"]

]
 """

# EJERCICIO 7 
""" 
r = arbolAleatorio(10)
imprimirArbol(r)

print()
print("Info de nodo minimo", nodoMin(r).info)
print("Info de nodo máximo", nodoMax(r).info)
 """


# EJERCICIO 8

# TABLA DE FRECUENCIAS
""" 
tabla = [
            [0.2, "A"],
            [0.17, "F"],
            [0.13, "1"],
            [0.21, "3"],
            [0.05, "0"],
            [0.09, "M"],
            [0.15, "T"]
        ]
 """
# A
""" 
raiz = crearArbolHuffman(tabla)
imprimirArbol(raiz)
print()
 """
# B
""" 
msj_in = "AF130M3TF"
msj_cod = comprimir(raiz, msj_in)
print("Mensaje original: ", msj_in)
print("Mensaje codificado: ", msj_cod)
msj_dec = decodificar(raiz, msj_cod)
print("Mensaje decodificado: ", msj_dec)
 """



# EJERCICIO 9

""" 
r = arbolAleatorio(10)
imprimirArbol(r)

# PRUEBA DE CALCULAR NODO POR NIVEL
for i in range(altura(r)):  # Dondei representa a cada nivel
    cant_nodos = nodosEnNivel(r, i)
    deberia_haber = calcNodosNivel(i)
    print("Nivel:", i, " Debería haber", deberia_haber, " Hay:", cant_nodos,
          " Faltan:", int(deberia_haber - cant_nodos))
 """

# EJERCICIO 10

# imprimirArbol(r)

# A
# print("Cantidad de nodos en el arbol:", pesoArbol(r))

# B
# print("Cantidad de hojas:", cantidadHojas(r))

# C
"""
print("Información de los nodos hojas")
mostrarHojas(r)
"""

# D
""" 
buscado = int(input("Ingrese valor del que desea determinar el padre: "))

padre = determinarPadre(r, buscado)

if padre == buscado:
    print("El elemento buscado es la raiz, no tiene padre")
else:
    if padre is not None:
        print("El padre de", buscado, "es", padre.info)
    else:
        print("El elemento buscado no se encuentra. No tiene padre")
 """

# E

# print("Altura de arbol:", r.altura)


# EJERCICIO 11
""" 
cant_niveles = 9
r = generarArbolPorNivel(cant_niveles)
 """
# imprimirArbol(r)


# A
# Crea bosque y recorta arbol en nivel deseado
""" 
nivel_a_cortar = 3
bosque = []
recortarArbol(r, bosque, nivel_a_cortar)
 """

"""
for arbol in bosque:
    print("##################")
    print()
    imprimirArbol(arbol)
    print()
    print("##################")
 """

# B
# Muestras los nodos que hay en el bosque
""" 
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

# E
# Indicar qué arboles del bosque están llenos
""" 
print()
for arbol in bosque:
    if arbolLleno(arbol):
        print("El arbol que empieza con raíz", arbol, "esta lleno")
    else:
        print("El arbol que empieza con raíz", arbol, "no esta lleno")

 """

# EJERCICIO 12
""" 
superheroes = ["Guardianes de las galaxias",
                "Ant-Man",
                "Hulk",
                "Capitan America",
                "Capitana Marvel",
                "Spiderman",
                "Black Widow",
                "Iron Man",
                "Dr. Strange",
                "Thor"
            ]


ASIGNACIONES = [
    {"mision": "Intergalactica", "peso": 1000, "asignado": ["Guardianes de las galaxias", "Capitana Marvel"]},
    {"mision": "En equipo", "peso": 2000, "asignado": ["Guardinaes de las galaxias"]},
    {"mision": "Recuperacion", "peso": 3000, "asignado": ["Ant-Man", "Capitan America", "Black Widow"]},
    {"mision": "Indetectable", "peso": 4000, "asignado": ["Ant-Man", "Spiderman"]},
    {"mision": "Destructivo", "peso": 5000, "asignado": ["Hulk", "Thor"]},
    {"mision": "Incorrumpible", "peso": 6000, "asignado": ["Capitan America"]},
    {"mision": "Defensa", "peso": 7000, "asignado": ["Capitan America", "Spiderman", "Iron Man"]},
    {"mision": "Poderoso", "peso": 8000, "asignado": ["Capitana Marbel", "Thor"]},
    {"mision": "Habilidoso", "peso": 9000, "asignado": ["Spiderman", "Dr. Strange"]},
    {"mision": "Estretegica", "peso": 10000, "asignado": ["Iron Man", "Dr. Strange"]}
]


arbol_deci = arbolDeci(ASIGNACIONES)

heroes = asignarHeroe("Destructivo", arbol_deci)
if heroes:
    print(heroes)
else:
    print("Tipo de misión inexistente")

 """


# EJERCICIO 13
""" 
lista_morse = [ ['E', 850000],
                ['T', 2450000],
                ['I', 450000],
                ['A', 1250000],
                ['N', 2050000],
                ['M', 2850000],
                ['S', 250000],
                ['U', 650000],
                ['R', 1050000],
                ['W', 1450000],
                ['D', 1850000],
                ['K', 2250000],
                ['G', 2650000],
                ['O', 3050000],
                ['H', 150000],
                ['V', 350000],
                ['F', 550000],
                [' ', 750000],
                ['L', 950000],
                [' ', 1150000],
                ['P', 1350000],
                ['J', 1550000],
                ['B', 1750000],
                ['X', 1950000], 
                ['C', 2150000], 
                ['Y', 2350000], 
                ['Z', 2550000], 
                ['Q', 2750000], 
                [' ', 2950000], 
                [' ', 3150000], 
                ['5', 100000],
                ['4', 200000],
                [' ', 300000],
                ['3', 400000],
                [' ', 500000],
                [' ', 600000],
                [' ', 700000],
                ['2', 800000],
                [' ', 900000],
                [' ', 1000000], 
                [' ', 1100000], 
                [' ', 1200000], 
                [' ', 1300000], 
                [' ', 1400000], 
                [' ', 1500000], 
                ['1', 1600000], 
                ['6', 1700000],
                [' ', 1800000], 
                [' ', 1900000], 
                [' ', 2000000], 
                [' ', 2100000], 
                [' ', 2200000], 
                [' ', 2300000], 
                [' ', 2400000],  
                ['7', 2500000],
                [' ', 2600000], 
                [' ', 2700000], 
                [' ', 2800000], 
                ['8', 2900000],
                [' ', 3000000],
                ['9', 3100000], 
                ['0', 3200000]
            ]



msj1 = ".--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- / .--. .-. --- -- . - . -- . / .- .-.. --. --- /--.- ..- . / ...- .- / ... . --. ..- .. .-. / ... .. . -. -.. --- / ..- ... - . -.. / -. --- / ..- -. / ... --- .-.. -.. .- -.. --- / .--. . .-. ..-. . -.-. - --- / ... .. -. --- / ..- -. / -... ..- . -. /.... --- -- -... .-. . .-.-."
msj2 = "-. --- ... --- - .-. --- ... / ... --- -- --- ... / .-.. --- ... / -- .- .-.. -.. .. - --- ... / --. ..- .- .-. -.. .. .- -. . ... / -.. . / .-.. .- / --. .- .-.. .- -..- .. .- .-.-."
msj3 = "-.-- --- / ... --- .-.. --- / .- -.-. - ..- --- / -.-. --- -- --- / ... .. / . -. / ...- . .-. -.. .- -.. / .-.. --- / ... ..- .--. .. . .-. .- / - --- -.. --- .-.-."
msj4 = "-.-. .... .. -.-. --- ... / . ... - --- -.-- / .-.. .-.. . ...- .- -. -.. --- / .-.. .- / ..-. .. . ... - .- / .... .- -.-. .. .- / ..- ... - . -.. . ... .-.-."
msj5 = ".--. --- -.. .-. .. .- / .... .-  -.-. . .-. / . ... - --- / - --- -.. --- / . .-.. / -.. .. .- .-.-."


arbol = arbolMorse(lista_morse)

print("Mensaje 1:", decodMsj(arbol, msj1))
print("Mensaje 2:", decodMsj(arbol, msj2))
print("Mensaje 3:", decodMsj(arbol, msj3))
print("Mensaje 4:", decodMsj(arbol, msj4))
print("Mensaje 5:", decodMsj(arbol, msj5))

 """

# EJERCICIO 14

# ruta = "./Tp's 7 - Arbol/personajesSW/personajesStarWars"

# Utilizado para inicial el archivo, en caso de que no esté cargado, o recargarlo
# initArchivoPersonajes(ruta)


# A

# arbol_nombres = generarArbolPersonajesNombre(ruta)
# B

# arbol_nombres = altaPersonaje(arbol_nombres, ruta)
# arbol_nombres = modificarPersonaje(arbol_nombres, ruta)
# arbol_nombres = bajaPeronsaje(arbol_nombres, ruta)


# C
""" 
print("Información de Yoda")
consultaPersonaje(arbol_nombres, "Yoda", ruta)
print("Información de Boba Fett")
consultaPersonaje(arbol_nombres, "Boba Fett", ruta)
 """

# D
""" 
archivo = abrir(ruta)
print("Personajes que miden mas de un metro")
listadoIndicesAltura(arbol_nombres, archivo)
print()

# E
print("Personajes que pesan menos de 75kg")
listadoIndicesPeso(arbol_nombres, archivo)
 """


# EJERCICIO 15

tabla = [
            [0.22, "Despejado"],
            [0.15, "Nublado"],
            [0.03, "Lluvia"],
            [0.26, "Baja"],
            [0.14, "Alta"],
            [0.05, "1"],
            [0.01, "2"],
            [0.035, "3"],
            [0.06, "5"],
            [0.02, "7"],
            [0.025, "8"]
        ]

# B 
raiz = crearArbolHuffman(tabla)

# Para controlar
"""
dic = {}
huffmanToDicCodificaciones(raiz, dic)
print(dic)
"""

# C 
""" 
msj_original = nanoMensaje()
msj_comprimido = comprimirMedicion(raiz, msj_original)
msj_descomprimido = descomprimirMedicion(raiz, msj_comprimido)


print()
print("Mensaje original:", msj_original)
print("Mensaje comprimido:", msj_comprimido)
print("Mensaje descomprimido:", msj_descomprimido)
 """

# D
""" 
print("Diferencia en tamaño de memoria ocupada entre mensaje")
print("comprimido y descomprimido:")
print(diferenciaTamano(msj_original, msj_comprimido))
 """



# EJERCICIO 16

""" 
def obtenerDebilidades(pokemon):
                            
    return type(keys)
 """

# initFilePokemon()

# ruta_file = "Pokemons/pokemons"

# A
""" 
arbolPokeNombre = generarArbolPoke(ruta_file, "nombre")  # Generado por campo 0 = Nombre
arbolPokeNro = generarArbolPoke(ruta_file, "nro")  # Generado por campo 1 = Nro
arbolPokeTipo = generarArbolPoke(ruta_file, "tipo")  # # Generado por campo 2 = Tipo
 """

# B - listar por nombre buscado
""" 
buscado = "Bul"
print("Pokemons encontrados que comiencen o contengan:", buscado)
lista_poke = listaPokemonsNombre(ruta_file, arbolPokeNombre, buscado)

for pokemon in lista_poke:
        print(pokemon)
 """

# B - mostrar dato a partir de número
""" 
buscado = 135
print("Pokemon encontrado con el id de pokedex solicitado:", buscado)

poke_encontrado = busquedaNroPoke(ruta_file, arbolPokeNro, buscado)

if poke_encontrado:
    print(poke_encontrado)
else:
    print("El pokemon con nro", buscado, "ingresado no se encuentra en nuestra pokedex")
 """

# C
""" 
tipo_buscado = "fire"
pokemons_tipo = listaBusquedaTipoArbol(ruta_file, arbolPokeTipo, tipo_buscado)

print("Todos los pokemons de que tengan tipo ", tipo_buscado, " como principal o secundario")
for pokemon in pokemons_tipo:
    print(pokemon)
 """

# D
""" 

# Se buscan los datos de los tres pokemons, para poder extrae los tipos
lista_poke = listaPokemonsNombre(ruta_file, arbolPokeNombre, "Jolteon")
lista_poke += (listaPokemonsNombre(ruta_file, arbolPokeNombre, "Lycanroc"))
lista_poke += (listaPokemonsNombre(ruta_file, arbolPokeNombre, "Tyrantrum"))

# Se extraen los tipos de todo en una lista
tipos_a_buscar = []
for poke in lista_poke:
    t1 = poke.tipos[0]
    t2 = poke.tipos[1]
    tipos_a_buscar.append(t1)
    if t2 != "":
        tipos_a_buscar.append(t2)

# Eliminar repetidos
tipos_a_buscar = list(set(tipos_a_buscar))
 
# Como el ejercicio no pedía arbol de debilidades, se deduce que se leerá directamente desde el
# archivo para encontrar cuáles cumplen esta condición
#  
data_pokemons = fileToArray(ruta_file)

for pokemon in data_pokemons:
    datos = pokemon[0]
    for tipo in tipos_a_buscar:
        if tipo in datos.tipos:
            print(datos)
            break
"""


# E
""" 
tipos = ["bug","dark","dragon","electric","fairy","fight","fire","flying","ghost","grass","ground","ice","normal","poison","psychic","rock","steel","water"]

for tipo in tipos:
    pokemons_tipo = listaBusquedaTipoArbol(ruta_file, arbolPokeTipo, tipo)
    print("Hay", len(pokemons_tipo), "pokemons de tipo", tipo)
 """




# EJERCICIO 17

# 0: general
# 1: fecha
# 2: codigo
# 3: estado
# 4: tipo_soldado


# B (Necesario generarlo para otros puntos)
""" 
arbolNombreSW, arbolFechaSW, arbolCodigoSW = None, None, None

for i in range(1000):
    reporte = generarReporteAleatorio(i)
    
    arbolNombreSW = insertarCampo(arbolNombreSW, reporte, 0)
    arbolFechaSW = insertarCampo(arbolFechaSW, reporte, 1)
    arbolCodigoSW = insertarCampo(arbolCodigoSW, reporte, 2)
 """
# C
""" 
armasFalladasPorGeneral(arbolNombreSW)
 """

# D
""" 
print("Cantidad de soldados por cada tipo en las misiones de Kylo Ren")
soldadosCantidadPorGeneral(arbolNombreSW, "Kylo Ren")
 """


# E
""" 
determinarSithyFallas(arbolNombreSW)
 """

# F
""" 
codigoDeMisionesFecha(arbolFechaSW, "1/02/2019")
 """


# G 
# Se ingresa un nuevo reporte con el código solicitado, para poder buscarlo.
# En este caso solo a arbol de código, ya que los demás no es necesario, pero debería hacerse
""" 
print()
codigo_buscado = 75951380
reporte = generarReporteAleatorio(codigo_buscado)

arbolCodigoSW = insertarCampo(arbolCodigoSW, reporte, 2)

encontrado = (busquedaCampo(arbolCodigoSW, codigo_buscado, 2))
if encontrado:
    print(encontrado.info)
else:
    print("No se encontro datos de la blaster con codigo", codigo_buscado, "en alguna mision")
 """


# EJERCICIO 18


# A Se cargan 100 libros
""" 
ruta_file = "Libros/libros"
initFileLibros()
 """

# B
""" 
arbolTitulo = generarArbolLibro(ruta_file, "titulo")
arbolISBN = generarArbolLibro(ruta_file, "isbn")
arbolAutores = generarArbolLibro(ruta_file, "autores")
 """
# imprimirArbol(arbolTitulo)
# imprimirArbol(arbolISBN)
# imprimirArbol(arbolAutores)


# D
# D - i
""" 
isbn_buscado = 10
res = busquedaPorISBN(arbolISBN, isbn_buscado)

if res:
    indice = res[1]

    archivo = abrir(ruta_file)
    libro = leer(archivo, indice)
    cerrar(archivo)
    
    print(libro)
else:
    print("Libro con ISBN", isbn_buscado, "no encontrado")
 """

# D - ii
""" 
autor_buscado = "autor3"
res = busquedaPorAutor(arbolAutores, autor_buscado)

if len(res) > 0:
    print("Lista de libros que tienen de autor a", autor_buscado)

    archivo = abrir(ruta_file)
    for item in res:
        indice = item[1]
        libro = leer(archivo, indice)
        print(libro)
    cerrar(archivo)
else:
    print("No se encontraron libros con ese autor")
 """

# D - iii
""" 
inicio_nombre_buscado = "alg"
imprimirArbol(arbolTitulo)
res = busquedaPorCoincidenciaTitulo(arbolTitulo, inicio_nombre_buscado)

print(res)
 """

# A
""" 
# Se busca en el arbol todos los libros de los autores deseados
libros_tanenbaum = busquedaPorAutor(arbolAutores, "Tanenbaum")
libros_connolly = busquedaPorAutor(arbolAutores, "Connolly")
libros_rowling = busquedaPorAutor(arbolAutores, "Rowling")
libros_roirdan = busquedaPorAutor(arbolAutores, "Roirdan")

libros_a_buscar = libros_tanenbaum + libros_connolly + libros_rowling + libros_roirdan

# De la lista anterior se extrane solo los indices, para realizar la búsqueda futura en archivo
indices = set()
for libro in libros_a_buscar:
    indices.add(libro[1])

# Se trae los datos desde el archivo de los libros mencionados anteriormente
archivo = abrir(ruta_file)
libros_deseados = leerIndices(archivo, indices)
cerrar(archivo)

# Muestra dato de todos los libros obtenidos
for libro in libros_deseados:
    print(libro)

 """

 # B

""" 
libros_mineria = busquedaPorCoincidenciaTitulo(arbolTitulo, "Mineria de Datos")
libros_algoritmos = busquedaPorCoincidenciaTitulo(arbolTitulo, "Algoritmos")
libros_bbdd = busquedaPorCoincidenciaTitulo(arbolTitulo, "Base de Datos")

libros_a_buscar = libros_mineria + libros_algoritmos + libros_bbdd

# De la lista anterior se extrae solo los indices, para realizar la búsqueda futura en archivo
indices = set()
for libro in libros_a_buscar:
    indices.add(libro[1])

# Se trae los datos desde el archivo de los libros mencionados anteriormente
archivo = abrir(ruta_file)
libros_deseados = leerIndices(archivo, indices)
cerrar(archivo)

print("Libros de Mineria de Datos, Algoritmos y Base de Datos:")
for libro in libros_deseados:
    print(libro)
 """


# C
""" 
# Creación arbol páginas para que sea más eficiente la búsqueda
arbolPaginas = generarArbolLibro(ruta_file, "paginas")
paginas_deseadas = 873

# Se extrae del arbol, los indices de todos aquellos que tengan más de 873
indices_a_buscar = []
busqPag(arbolPaginas, paginas_deseadas, indices_a_buscar)

# Lista libros extraída de archivo
libros = []
archivo = abrir(ruta_file)
for indice in indices_a_buscar:
    libros.append(leer(archivo, indice))
cerrar(archivo)

print("Libros con más de", paginas_deseadas)
for libro in libros:
    print(libro)
 """


# D
""" 
isbn_buscado = 9788420546391
# Carga libro con ISBN especifico, inserta en archivo y actualiza los arboles
nuevo_libro = Libro("PuntoD", isbn_buscado, ["autorRandom"], "edit2", 203)

archivo = abrir(ruta_file)
guardar(archivo, nuevo_libro)
cerrar(archivo)

arbolTitulo = generarArbolLibro(ruta_file, "titulo")
arbolISBN = generarArbolLibro(ruta_file, "isbn")
arbolAutores = generarArbolLibro(ruta_file, "autores")

# Busqueda en el arbol
res = busquedaPorISBN(arbolISBN, isbn_buscado)

# Busqueda en archivo
if res:
    indice = res[1]

    archivo = abrir(ruta_file)
    libro = leer(archivo, indice)
    cerrar(archivo)
    
    print(libro)
else:
    print("Libro con ISBN", isbn_buscado, "no encontrado")
 """

# E
""" 
# Carga libro con ISBN especifico, inserta en archivo y actualiza los arboles
nuevo_libro = Libro("NoSQL for Mere Mortals", 654654654, ["autorRandom"], "edit2", 5071)

archivo = abrir(ruta_file)
guardar(archivo, nuevo_libro)
cerrar(archivo)

arbolTitulo = generarArbolLibro(ruta_file, "titulo")
arbolISBN = generarArbolLibro(ruta_file, "isbn")
arbolAutores = generarArbolLibro(ruta_file, "autores")

# busqueda por titulo NoSQL
libros_nosql = busquedaPorCoincidenciaTitulo(arbolTitulo, "NoSQL for Mere Mortals")
indice_nosql = libros_nosql[0][1]


if len(libros_nosql) > 0:
    archivo = abrir(ruta_file)
    libro = leer(archivo, indice_nosql)
    cerrar(archivo)

    print("Autor/es de NoSQL for Mere Mortals")
    print(libro.autores)
else:
    print("No se encontró el libror NoSQL for Mere Mortals")
 """



# EJERCICIO 19
""" 
arbolRegistros = genArbolMeteorologico()

registro = genRegistroMeteorologico()
print("Registro analizado:", registro)
pronostico = definirPronostico(arbolRegistros, registro)
print("Pronostico:", pronostico)
 """

# EJERCICIO 20
# 0: Criatura
# 1: Derrotado por
# 2: descripcion
""" 
criatura_derrotado = [
            ['Ceto', '', ''],
            ['Tifon', 'Zeus', ''],
            ['Equidna', 'Argos Panoptes', ''],
            ['Dino', '', ''],
            ['Pefredo', '', ''],
            ['Enio', '', ''],
            ['Escila', '', ''],
            ['Caribdis', '', ''],
            ['Euriale', '', ''],
            ['Esteno', '', ''],
            ['Medusa', 'Perseo', ''],
            ['Ladon', 'Heracles', ''],
            ['Aguila del Caucaso', '', ''],
            ['Quimera', 'Belerofonte', ''],
            ['Hidra de Lerna', 'Heracles', ''],
            ['Leon de Nemea', 'Heracles', ''],
            ['Esfinge', 'Edipo', ''],
            ['Dragon de la Colquida', '', ''],
            ['Cerbero', '', ''],
            ['Cerda de Cromion', 'Teseo', ''],
            ['Ortro', 'Heracles', ''],
            ['Toro de Creta', 'Teseo', ''],
            ['Jabali de Calidon', 'Atalanta', ''],
            ['Carcinos ', '', ''],
            ['Gerion', 'Heracles', ''],
            ['Cloto', '', ''],
            ['Laquesis', '', ''],
            ['Atropos', '', ''],
            ['Minotauro de Creta', 'Teseo', ''],
            ['Harpias', '', ''],
            ['Argos Panoptes', 'Hermes', ''],
            ['Aves del Estinfalo', '', ''],
            ['Talos', 'Medea', ''],
            ['Sirenas', '', ''],
            ['Piton', 'Apolo', ''],
            ['Cierva de Cerinea', '', ''],
            ['Basilisco', '', ''],
            ['Jabali de Erimanto', '', '']
        ]

arbolCriaturas = None
for criatura in criatura_derrotado:
    arbolCriaturas = insertarCampo(arbolCriaturas, criatura, 0)
 """
# A
""" 
inorden(arbolCriaturas)
 """
# B
""" 
criatura = "Dino"
print("Antes de agregar la descripcion")

res = busquedaCampo(arbolCriaturas, criatura, 0)
print("Nombre:", res.info[0])
print("Derrotado por:", res.info[1])
print("Descripcion:", res.info[2])

agregarDescripcion(arbolCriaturas, criatura, "Descripcon random")
print()

print("Despues de agregar la descripcion")
res = busquedaCampo(arbolCriaturas, criatura, 0)
print("Nombre:", res.info[0])
print("Derrotado por:", res.info[1])
print("Descripcion:", res.info[2])
 """
# C
""" 
nombre_criatura = "Talos"
res = busquedaCampo(arbolCriaturas, nombre_criatura, 0)
print()
if res:
    print("Nombre:", res.info[0])
    print("Derrotado por:", res.info[1])
    print("Descripcion:", res.info[2])
else:
    print("No se encontró datos de la criatura", nombre_criatura)
 """    


# D 
""" 
# Lista de todos los vencedores (repetidos)  
lista_vencedores = vencedores(arbolCriaturas)
# Vencedores ordenados por cantidad de apariciones/victorias
vencedores = sorted(lista_vencedores, key=lambda x: lista_vencedores.count(x), reverse=True)
# Lista sin duplicados
mayores_vencedores = eliminarDuplicados(vencedores)

print("Mayores 3 heroes/dioses vencedores")
for i in range(3):
    print(mayores_vencedores[i])
 """


# E
""" 
nombre = "Heracles"

criaturas_derrotadas_heroe = []
criaturasDerrotadasPor(arbolCriaturas, nombre, criaturas_derrotadas_heroe)

print("Criaturas derrotadas por Hermes:")
for criatura in criaturas_derrotadas_heroe:
    print(criatura[0])
 """
# F
""" 
no_derrotadas = []
criaturasDerrotadasPor(arbolCriaturas, "", no_derrotadas)

print("Criaturas no derrotadas")
for criatura in no_derrotadas:
    print(criatura[0])
 """

# G
""" 
nombre_criatura = "tr"

criaturas_encontradas = []
busquedaProximidadCriatura(arbolCriaturas, nombre_criatura, criaturas_encontradas)

print("Lista de criatura coincidentes con '{}'".format(nombre_criatura))
for criatura in criaturas_encontradas:
    print(criatura[0])
 """

# H
""" 
print("Antes de elimar Basilisco y Sirenas")
imprimirArbol(arbolCriaturas)

arbolCriaturas, data_basilisco = eliminarCampo(arbolCriaturas, "Basilisco", 0)
arbolCriaturas, data_sirenas = eliminarCampo(arbolCriaturas, "Sirenas", 0)

print()
print("Despues de eliminarlos:")

imprimirArbol(arbolCriaturas)
 """

# I
""" 
print("Antes de modificar el derrotado por de Aves del Estinfalo")
imprimirArbol(arbolCriaturas)

modificarDerrotadoPor(arbolCriaturas, "Aves del Estinfalo", "Heracles")
print()

print("Despues de modificar el derrotado por de Aves del Estinfalo")
imprimirArbol(arbolCriaturas)
 """

# J
""" 
modificarnombreCriatura(arbolCriaturas, "Ladon", "Dragon Ladon")

print("Se modificó Ladon por Dragon Ladon")
imprimirArbol(arbolCriaturas)
 """


# EJERICIO 22
# A
""" 
tabla = [
    ["A", 11, 0],
    ["B", 2, 0],
    ["C", 4, 0],
    ["D", 3, 0],
    ["E", 14, 0],
    ["G", 3, 0],
    ["I", 6, 0],
    ["L", 6, 0],
    ["M", 3, 0],
    ["N", 6, 0],
    ["O", 7, 0],
    ["P", 4, 0],
    ["Q", 1, 0],
    ["R", 10, 0],
    ["S", 4, 0],
    ["T", 3, 0],
    ["U", 4, 0],
    ["V", 2, 0],
    [" ", 17, 0],
    [",", 2, 0]
]

asignarFrecuencias(tabla)

# Creamos la tabla con el formato que necesita el arbol de Huffman para crease y el orden
tabla_para_huffman = formatearTablaParaHuffman(tabla)

arbol_huffman = crearArbolHuffman(tabla_para_huffman)
 """
# B
""" 
msj1 = '10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100'
msj2 = '0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010'

print("Msj1:")
msj1_decodificado = decodificar(arbol_huffman, msj1)
print(msj1_decodificado)

print("Msj2:")
msj2_decodificado = decodificar2(arbol_huffman, msj2)
print(msj2_decodificado)
 """
# C
""" 
print()
print("Diferencia tamano entre msj1 comprimido y sin comprimir:")
print(diferenciaTamano(msj1, msj1_decodificado))
print("Diferencia tamano entre msj2 comprimido y sin comprimir:")
print(diferenciaTamano(msj2, msj2_decodificado))
 """









































print()
print("FIN ARCHIVO")