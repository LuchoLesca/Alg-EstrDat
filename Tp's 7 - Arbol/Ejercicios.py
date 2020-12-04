from string import ascii_uppercase, digits
from TDA_Arbol import *
from random import randint, choice
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
# EJERCICIO 1  HECHO

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
 """
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
'''
a_indices = abrir("Indices/indice_summerville")
aknuth = fileToBinaryTree(a_indices)
cerrar(a_indices)

# A

barridoKnuth(aknuth)


# B


def busquedaKnuthCampo(raiz, buscado, campo):
    pass

'''




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
""" print("Previo a busqueda y modificacion")
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
# EJERCICIO 6 <<<<<<<<<<<<<<<<<

""" 
indice_archivos = [["arduino"], ["documentos"], ["libros"], ["escritorio"],
                   ["imagenes"], ["musica"], ["nodeProjects"], ["plantillas"],
                   ["prueba_cluster"], ["PythonProyects"]

]
 """

# EJERCICIO 7   HECHO
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

# A

raiz = crearArbolHuffman(tabla)
imprimirArbol(raiz)
print()

# B

msj_in = "AF130M3TF"
msj_cod = comprimir(raiz, msj_in)
print("Mensaje original: ", msj_in)
print("Mensaje codificado: ", msj_cod)
msj_dec = decodificar(raiz, msj_cod)
print("Mensaje decodificado: ", msj_dec)
 """



# EJERCICIO 9

""" 
def calcNodosNivel(nivel):
    '''Calcula la cantidad de nodos que debería haber en el nivel para que
    esté completo'''
    return pow(2, nivel)

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
def mostrarHojas(raiz):
    if raiz is not None:
        mostrarHojas(raiz.izq)
        if esHoja(raiz):
            print(raiz.info)
        mostrarHojas(raiz.der)


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


def arbolDeci():
    ''' Genera arbol de decisiones para este ejercicio '''
    arbol = None
    for item in ASIGNACIONES:
        # Inserta pregunta
        arbol = insertarArbol2(arbol, item.get("mision"), item.get("peso"))
        # Inserta respuesta de si
        arbol = insertarArbol2(arbol, item.get("asignado"), item.get("peso")-500)

    return arbol

# imprimirArbol(arbolDeci())

def busquedaHeroes(raiz, mision):
    aux = None

    if raiz is not None:
        if raiz.info == mision:
            aux = raiz.izq.info
        else:
            aux = busquedaHeroes(raiz.der, mision)
        
    return aux

def asignarHeroe(mision):
    arbol_dec = arbolDeci()
    resultados = busquedaHeroes(arbol_dec, mision)

    return resultados

heroes = asignarHeroe("Destructivo")
if heroes:
    print(heroes)
else:
    print("Tipo de misión inexistente")

 """


# EJERCICIO 13

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

def arbolMorse():
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

def decodSegm(segmento):
    arbol = arbolMorse()
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


def decodMsj(codigo):
    msj_decod = ""
    segmentos = codigo.split("/")

    for segmento in segmentos:
        msj_decod += decodSegm(segmento)

    return msj_decod


msj1 = ".--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- / .--. .-. --- -- . - . -- . / .- .-.. --. --- /--.- ..- . / ...- .- / ... . --. ..- .. .-. / ... .. . -. -.. --- / ..- ... - . -.. / -. --- / ..- -. / ... --- .-.. -.. .- -.. --- / .--. . .-. ..-. . -.-. - --- / ... .. -. --- / ..- -. / -... ..- . -. /.... --- -- -... .-. . .-.-."
msj2 = "-. --- ... --- - .-. --- ... / ... --- -- --- ... / .-.. --- ... / -- .- .-.. -.. .. - --- ... / --. ..- .- .-. -.. .. .- -. . ... / -.. . / .-.. .- / --. .- .-.. .- -..- .. .- .-.-."
msj3 = "-.-- --- / ... --- .-.. --- / .- -.-. - ..- --- / -.-. --- -- --- / ... .. / . -. / ...- . .-. -.. .- -.. / .-.. --- / ... ..- .--. .. . .-. .- / - --- -.. --- .-.-."
msj4 = "-.-. .... .. -.-. --- ... / . ... - --- -.-- / .-.. .-.. . ...- .- -. -.. --- / .-.. .- / ..-. .. . ... - .- / .... .- -.-. .. .- / ..- ... - . -.. . ... .-.-."
msj5 = ".--. --- -.. .-. .. .- / .... .-  -.-. . .-. / . ... - --- / - --- -.. --- / . .-.. / -.. .. .- .-.-."

arbol = arbolMorse()

print("Mensaje 1:", decodMsj(msj1))
print("Mensaje 2:", decodMsj(msj2))
print("Mensaje 3:", decodMsj(msj3))
print("Mensaje 4:", decodMsj(msj4))
print("Mensaje 5:", decodMsj(msj5))






print("FIN ARCHIVO")