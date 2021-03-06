from TDA_Lista import *
import datetime
from random import randint, choice, random


# EJERCICIO 1
"""
lista = Lista()
for i in range(0, randint(0, 20)):
    insertar(lista, randint(-100, 100))

barridoLista(lista)
print()
print("Cantidad de elementos de lista con atributo tamanio: " +
      str(lista.tamanio))

aux = lista.inicio
cant = 0
while aux is not None:
    cant += 1
    aux = aux.sig
print()
print("Cantidad de elementos en lista con algoritmo de barrido: " + str(cant))
"""


# EJERCICIO 2
"""
lista = Lista()

cargaAutoStrL(lista, 10)
insertar(lista, "A")
insertar(lista, "e")
insertar(lista, "o")

print("Lista de caracteres")
barridoLista(lista)
# print("Tamaño: " + str(lista.tamanio))

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for vocal in vocales:
    eliminarTodos(lista, vocal)

print()
print("Lista sin vocales")
barridoLista(lista)
# print("Tamaño: " + str(lista.tamanio))
"""

# EJERCICIO 3
"""
lista1, lista2, lista3 = Lista(), Lista(), Lista()
cargaAutoIntL(lista1, 15)

print("Lista Completa:")
barridoLista(lista1)

aux = lista1.inicio

while (aux is not None):
    if (aux.info % 2 == 0):
        insertar(lista2, aux.info)
    else:
        insertar(lista3, aux.info)
    aux = aux.sig

print()
print("Lista de números pares")
barridoLista(lista2)
# print("Tamaño: " + str(lista2.tamanio))


print()
print("Lista de números impares")
barridoLista(lista3)
# print("Tamaño: " + str(lista3.tamanio))
"""

# EJERCICIO 4
"""
lista = Lista()
pos = 3
dato = 10

cargaAutoIntL(lista, 10)

print("Lista original")
barridoLista(lista)

insertarEn(lista, dato, pos)
print()
print("Lista con " + str(dato) + " ingresado en posicion " + str(pos))
barridoLista(lista)
"""

# EJERCICIO 5
"""
lista = Lista()

# Carga números 4 primos aleatorios
while lista.tamanio < 4:
    num = randint(2, 100)
    if primo(num):
        insertar(lista, num)
# Carga 4 números compuestos aleatorios
while lista.tamanio < 8:
    num = randint(2, 100)
    if not primo(num):
        insertar(lista, num)

print("Lista original. Tamaño: " + str(lista.tamanio))
barridoLista(lista)

aux = lista.inicio

while (aux is not None):
    if primo(aux.info):
        eliminar(lista, aux.info)
    aux = aux.sig

print()
print("Lista sin números primos. Tamaño: " + str(lista.tamanio))
barridoLista(lista)
"""

# EJERCICIO 6
"""
lista = Lista()
lista2 = Lista()  # Copia de lista2, con heroes ordenados por fecha aparición

heroes = ["Linterna Verde", "Wolverine", "Ant-Man", "Batman",
          "Spider-man", "Ironman"]
anios = [1955, 1960, 1980, 1985, 1990, 1995]
casas = ["DC", "DC", "DC", "DC", "Marvel", "Marvel"]
biografias = ["None", "None", "Traje", "Traje", "Traje", "Armadura"]

for i in range(0, len(heroes)):
    heroe = [heroes[i], anios[i], casas[i], biografias[i]]
    inserCampo(lista, heroe, 0)
    inserCampo(lista2, heroe, 1)

print("Lista original:")
barridoLista(lista)
print()
"""
# A Elimina el nodo de linterna verde
"""
eliminarCampo(lista, "Linterna Verde", 0)

print("Barrido sin Linterna Verde")
barridoLista(lista)
print()
"""

# B Busca y muestra el año de apraricio de Wolverine
"""
aux = busquedaListaCampo(lista, "Wolverine", 0)
if aux is not None:
    print("Año aparicion Woverine: " + str(aux.info[1]))
else:
    print("Wolverine no estaba en la lista")
"""

# C Cambiar la casa de ant-man a Marvel
"""
aux = busquedaListaCampo(lista, "Ant-Man", 0)

if aux is not None:
    aux.info[2] = "Marvel"
    print("Casa de Ant-Man cambiada")
else:
    print("Ant-Man no se encontrava en la lista")

barridoLista(lista)
"""

# D Mostrar nombre de personajes que en biografia mencione traje o armadura
"""
aux = lista.inicio

while (aux is not None):
    if ("Traje" in aux.info[3]) or ("Armadura" in aux.info[3]):
        print(aux.info)
    aux = aux.sig
"""

# E Mostrar nombre y casa de heroes con aparicion anterior a 1963
"""
print()
print("Lista de heroes ordenada por año de aparición:")
barridoLista(lista2)
print()
print("Superhéroes con fecha de aparición menor a 1963:")

aux = lista2.inicio

while (aux is not None) and (aux.info[1] < 1963):
    print(aux.info)
    aux = aux.sig
"""

# EJERCICIO 7
"""
lista1, lista2 = Lista(), Lista()

for i in range(1, 6):
    insertar(lista1, i*2)
    insertar(lista2, i*4)

print("Lista1")
barridoLista(lista1)
print()
print("Lista2")
barridoLista(lista2)
"""

# A Concatenar una lista atrás de otra
"""
lista3 = copiarLista(lista1)  # Crea copia de la lista1, para no modificar esta
ultimoNodo(lista3).sig = lista2.inicio  # Concatena lista2 atrás de lista3

print()
print("Lista una atras de otra concatenadas:")
barridoLista(lista3)
"""

# B Concatear listas en 1 sola, omitiendo datos repetidos, manteniendo orden
"""
lista3 = union(lista1, lista2)
print("Lista concatenada sin repetir y ordenada")
barridoLista(lista3)
"""

# C
"""
lista3 = interseccion(lista1, lista2)
print()
print("Cantidad de elementos repetidos: " + str(lista3.tamanio))
barridoLista(lista3)
"""

# D
"""
print("A continuacion se eliminaran los elementos de la lista 1, uno a la vez")
print()
if (lista1.tamanio >= 0):
    while (lista1.tamanio > 1):
        ant = lista1.inicio
        act = ant.sig

        while (act.sig is not None):
            ant = ant.sig
            act = act.sig
        ant.sig = None
        lista1.tamanio -= 1

        barridoLista(lista1)
        print()

    lista1.inicio = None
    lista1.tamanio -= 1

    print("Todos los elementos de la lista eliminados. Tamaño: " +
          str(lista1.tamanio))
"""

# EJERCICIO 8
"""
lista = Lista()

cantidad_deseada = 30

while (lista.tamanio < cantidad_deseada):

    num = randint(-999, 999)

    if (lista.tamanio == 0):  # Tamaño 0
        insertar(lista, num)

    elif (lista.tamanio == 1):  # Tamaño 1
        if (primo(num)) and (abs(lista.inicio.info - num) > 14):
            insertar(lista, num)

        if (not primo(num)) and (num % 2 != 0) and ((lista.inicio.info % 2) == 0):
            insertar(lista, num)

    else:  # Si tamaño > 1
        ant = lista.inicio
        act = ant.sig

        while (act is not None) and (act.info < num):
            ant = ant.sig
            act = act.sig

        if act is None:  # Si llegó al final
            if (primo(num)) and (abs(ant.info - num) > 14):
                insertar(lista, num)

            if (not primo(num)) and (num % 2 != 0) and ((ant.info % 2) == 0):
                insertar(lista, num)
        else:
            if (primo(num)) and (abs(ant.info - num) > 14) and (abs(act.info - num) > 14):
                insertar(lista, num)

            if (not primo(num)) and (num % 2 != 0) and ((ant.info % 2) == 0) and ((act.info % 2) == 0):
                insertar(lista, num)

barridoLista(lista)
"""

# EJERCICIO 9
"""
# Nombre = 0    Artista = 1     Duracion = 2    Reproducciones = 3
abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

lista1 = Lista()  # Lista ordenada por artistas
lista2 = Lista()  # Lista ordenada por duración
lista3 = Lista()  # Lsita ordenada por reproducciones

for i in range(0, 5):
    nombre = "Nombre" + str(i)
    artista = "Arctic Monkeys"
    cancion = [nombre, artista, randint(60, 360), randint(0, 999)]
    inserCampo(lista1, cancion, 1)
    inserCampo(lista2, cancion, 2)
    inserCampo(lista3, cancion, 3)

for i in range(0, 15):
    nombre = "Nombre" + str(randint(1, 20))
    artista = choice(abc)
    cancion = [nombre, artista, randint(60, 360), randint(0, 999)]
    inserCampo(lista1, cancion, 1)
    inserCampo(lista2, cancion, 2)
    inserCampo(lista3, cancion, 3)
"""

# A
"""
barridoLista(lista2)
print()
print("Canción más larga")
print(ultimoNodo(lista2).info)
"""
# B
"""
barridoLista(lista3)
print()
top = 10

cont = lista3.tamanio - top

if (cont >= 0):
    aux = lista3.inicio
    for i in range(0, lista3.tamanio - top):
        aux = aux.sig
    while aux is not None:
        print(aux.info)
        aux = aux.sig
else:
    print("No se puede mostrar la cantidad de canciones solicitadas")
    print("A cambio, se muestran todas las canciones almacenadas: " +
          str(lista3.tamanio))
    aux = lista3.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig
"""

# C
"""
barridoLista(lista1)
print()

aux = busquedaListaCampo(lista1, "Arctic Monkeys", 1)
if aux is not None:
    while (aux is not None) and (aux.info[1] == "Arctic Monkeys"):
        print(aux.info)
        aux = aux.sig
"""

# EJERCICIO 10
"""
lista0 = Lista()  # Lista ordenada por nombre
lista1 = Lista()  # Lista ordenada por altura
lista2 = Lista()  # Lista ordenada por edad
lista3 = Lista()  # Lista ordenada por género
lista4 = Lista()  # Lista ordenada por especie
lista5 = Lista()  # Lista ordenada por planeta
lista6 = Lista()  # Lista ordenada por episodios


# Nombre=0, Altura=1, Edad=2, Género=3, Especie=4, Planeta=5, Episodio=6

nombres = ["Darth Vader", "Chewbacca", "Pj_A", "Pj_B", "Pj_C", "Pj_D"]
generos = ["M", "F"]
especies = ["Humano ", "Esp2", "Droide", "Droide", "Esp3", "Humano"]
planetas = ["Planet1", "Planet2", "Planet3", "Planet4", "Planet5", "Alderan"]

for i in range(0, 6):
    nombre = nombres[i]
    altura = randint(5, 250)
    edad = randint(5, 1100)
    genero = choice(generos)
    especie = especies[i]
    planeta = planetas[i]
    episodio = randint(1, 7)

    personaje = [nombre, altura, edad, genero, especie, planeta, episodio]
    inserCampo(lista0, personaje, 0)
    inserCampo(lista1, personaje, 1)
    inserCampo(lista2, personaje, 2)
    inserCampo(lista3, personaje, 3)
    inserCampo(lista4, personaje, 4)
    inserCampo(lista5, personaje, 5)
    inserCampo(lista6, personaje, 6)
"""

# A  Personajes femeninos
"""
barridoLista(lista3)
print()
print("Personajes de género femenino:")

aux = lista3.inicio
while (aux is not None) and (aux.info[3] != "F"):
    aux = aux.sig
if (aux is not None):
    while (aux is not None) and (aux.info[3] == "F"):
        print(aux.info)
        aux = aux.sig
else:
    print("La lista no tiene personajes mujeres")
"""

# B  Personajes droides
"""
barridoLista(lista4)
print()

aux = lista4.inicio
while (aux is not None) and (aux.info[4] != "Droide"):
    aux = aux.sig
if (aux is not None):
    while (aux is not None) and (aux.info[4] == "Droide"):
        if (aux.info[6] in [1, 2, 3, 4, 5, 6]):
            print(aux.info)
        aux = aux.sig
"""

# C  Info de Darth Vader
"""
barridoLista(lista0)
print()

nod = busquedaListaCampo(lista0, "Darth Vader", 0)

if nod is not None:
    print(nod.info)
else:
    print("Darth Vader no está en la lista")
"""

# D
"""
barridoLista(lista6)
print()

aux = lista6.inicio

while (aux is not None) and (aux.info[6] not in [4, 5, 6, 7]):
    aux = aux.sig
if (aux is not None):
    while (aux is not None) and (aux.info[6] in [4, 5, 6, 7]):
        print(aux.info)
        aux = aux.sig
"""

# E
"""
barridoLista(lista2)
print()
print("Personajes con más de 850 años:")

aux = lista2.inicio

while (aux is not None) and (aux.info[2] < 850):
    aux = aux.sig
if (aux is not None):
    while (aux is not None):
        print(aux.info)
        aux = aux.sig

print()
print("El personaje con mayor edad es: ")
print(ultimoNodo(lista2).info)
"""

# F
"""
barridoLista(lista6)
print()

if (lista6.tamanio == 1):
    if lista6.inicio.info[6] in [4, 5, 6]:
        lista6.inicio = lista6.inicio.sig
else:

    aux = lista6.inicio
    if aux.info[6] in [4, 5, 6]:
        while (aux is not None) and (aux.info[6] in [4, 5, 6]):
            aux = aux.sig
        lista6.inicio = aux
    else:
        ant = lista6.inicio
        act = ant.sig

        while (act is not None) and (act.info[6] not in [4, 5, 6]):
            ant = ant.sig
            act = act.sig
        if (act is not None):
            while (act is not None) and (act.info[6] in [4, 5, 6]):
                act = act.sig
            ant.sig = act

print("Personajes que no aparecieoon en episodio 4, 5 y 6:")
barridoLista(lista6)
"""

# G
"""
barridoLista(lista5)
print()
print("Personaje Humano de Alderan")
aux = lista5.inicio

while (aux is not None) and (aux.info[5] < "Alderan"):
    aux = aux.sig
if (aux is not None):
    while (aux is not None) and (aux.info[5] == "Alderan"):
        if (aux.info[4] == "Humano"):
            print(aux.info)
        aux = aux.sig
"""

# H
"""
barridoLista(lista1)
print()
print("Personaje con menos de 70cm de altura")

aux = lista1.inicio

while (aux is not None) and (aux.info[1] < 70):
    print(aux.info)
    aux = aux.sig
"""

# I
"""
lista1 = Lista()
for h in range(0, 3):
    insertar(lista1, h)

barridoLista(lista1)


if lista1.tamanio < 2:
    print("No existe elemento anteúltimo")
else:
    aux = lista1.inicio

    if lista1.tamanio == 2:
        lista1.inicio = aux.sig
    else:
        for i in range(0, lista1.tamanio - 3):
            aux = aux.sig
        aux.sig = aux.sig.sig

    print()
    # print("Lista con anteultimo eliminado")
    barridoLista(lista1)
"""

# J
"""
barridoLista(lista0)

print()

chewbacca = busquedaListaCampo(lista0, "Chewbacca", 0)
if chewbacca is not None:
    print(chewbacca.info)
"""


# EJERCICIO 14

"""
ENTRENADOR
nombres = 0
t_ganados = 1
b_perdidas = 2
b_ganadas = 3
pokemons = 4

POKEMON
nombre = 0
nivel = 1
tipo = 2
subtipo = 3
"""
tipos = ["Fuego", "Planta", "Agua", "Volador", "Tierra", "Eléctrico", "Hielo"]
entrenadores = ["Entr1", "Entr2", "Entr3", "Entre4"]
"""

def ListaPokemons(cant):

    aux = Lista()
    for i in range(0, cant):
        nombre = "Poke" + str(randint(0, 9))
        nivel = randint(1, 50)
        tipo = choice(tipos)
        subt = choice(tipos)
        while (subt == tipo):
            subt = choice(tipos)
        pokemon = [nombre, nivel, tipo, subt]

        inserCampo(aux, pokemon, 0)

    return aux


entrenadores = Lista()

for i in range(0, 9):
    nombre = "Entre" + str(i+1)
    t_ganados = randint(0, 20)
    b_perdidas = randint(0, 20)
    b_ganadas = randint(0, 20)
    lista_poke = ListaPokemons(randint(1, 5))

    entrenador = [nombre, t_ganados, b_perdidas, b_ganadas, lista_poke]

    inserCampo(entrenadores, entrenador, 0)

barridoLista(entrenadores)
print()
"""

# A
"""
buscado = "Entre1"
aux = busquedaListaCampo(entrenadores, buscado, 0)
if (aux is not None):
    print("Pokemons de entrenador " + buscado)
    barridoLista(aux.info[4])
else:
    print("El entrenador buscado no está en la lista")
"""

# B y C
"""
print("Entrenadores con más de 3 torneos ganados:")

if entrenadores.tamanio > 0:
    aux_entrenador = entrenadores.inicio

aux = entrenadores.inicio

while (aux is not None):
    if (aux.info[1] > 3):
        print(aux.info)
    if (aux.info[1] > aux_entrenador.info[1]):
        aux_entrenador = aux
    aux = aux.sig

print()
print("Entrenador con mas torneos ganados: " + str(aux_entrenador.info))

aux = aux_entrenador.info[4].inicio
aux_poke = aux
while (aux is not None):
    if (aux.info[1] > aux_poke.info[1]):
        aux_poke = aux
    aux = aux.sig

print("Su pokemon con mayor nivel es: " + str(aux_poke.info))
"""

# D
"""
print()
print("Entrenadores con más de 70% de batallas ganadas:")
aux = entrenadores.inicio

while (aux is not None):
    porcentaje_ganadas = (aux.info[3] * 100) / (aux.info[3] + aux.info[2])
    if (porcentaje_ganadas > 79):
        print(aux.info)
    aux = aux.sig
"""

# E
"""
print("Entrenadores con pokemon fuego/planta y/o agua/volador")
aux_entrenador = entrenadores.inicio

while (aux_entrenador is not None):
    aux_poke = aux_entrenador.info[4].inicio
    flag = False

    while (aux_poke is not None) and not flag:

        if ((aux_poke.info[2] == "Fuego") and (aux_poke.info[3] == "Planta")) or ((aux_poke.info[2] == "Agua") and (aux_poke.info[3] == "Volador")):
            flag = True

        aux_poke = aux_poke.sig

    if flag:
        print(aux_entrenador.info)


    aux_entrenador = aux_entrenador.sig
"""

# F
"""
entrenador_buscado = "Entre3"
encontrado = busquedaListaCampo(entrenadores, entrenador_buscado, 0)

if encontrado is None:
    print("El entrenador buscado no se encuentra")
else:
    promedio = 0

    pokemon = encontrado.info[4].inicio

    while (pokemon is not None):
        promedio += pokemon.info[1]
        pokemon = pokemon.sig

    promedio = promedio / encontrado.info[4].tamanio

    print("El promedio de niveles de sus pokemons es: " + str(promedio))
"""

# G
"""
cantidad = 0
pokemon = "Poke1"
print("Entrenadores que tengan de pokemon a " + pokemon)

aux_entrenador = entrenadores.inicio

while (aux_entrenador is not None):
    result = busquedaListaCampo(aux_entrenador.info[4], pokemon, 0)

    if result is not None:
        cantidad += 1
        print(aux_entrenador.info)

    aux_entrenador = aux_entrenador.sig

print("Total de entrenadores con el mismo pokemon: " + str(cantidad))
"""

# H
"""
print("Entrenadores que tienen pokemon repetidos: ")
aux_entrenador = entrenadores.inicio

while (aux_entrenador is not None):
    aux_poke = aux_entrenador.info[4].inicio
    repetido = False

    while (aux_poke.sig is not None) and (not repetido):

        if aux_poke.info[0] == aux_poke.sig.info[0]:
            print(aux_entrenador)
            print("Pokemon repetido: " + aux_poke.info[0])
            repetido = True

        aux_poke = aux_poke.sig

    aux_entrenador = aux_entrenador.sig
"""

# EJERCICIO 15
"""
costo = 0
tiempo = 1 (horas)
dia = 2
mes = 3
anio = 4
resp = 5
"""
"""
tareas = Lista()

for i in range(1, 11):
    costo = randint(10, 10000)
    tiempo = randint(1, 12)
    dia = randint(1, 29)
    mes = randint(1, 12)
    anio = randint(2017, 2019)
    resp = "Persona" + str(i)
    tarea = [costo, tiempo, dia, mes, anio, resp]

    inserCampo(tareas, tarea, 5)

barridoLista(tareas)
"""
# A y B
"""
tiempo_promedio = 0
costo_total = 0

aux = tareas.inicio

while (aux is not None):
    tiempo_promedio += aux.info[1]
    costo_total += aux.info[0]

    aux = aux.sig

tiempo_promedio = tiempo_promedio / tareas.tamanio
print()
print("Tiempo promedio de tareas: " + str(tiempo_promedio))
print("Costo total del proyecto: " + str(costo_total))
"""

# C
"""
persona_buscada = "Persona3"
inserCampo(tareas, [1000, 3, 5, 2, 2018, "Persona3"], 5)

print()
print("Actividades realizadas por " + persona_buscada)

buscado = busquedaListaCampo(tareas, persona_buscada, 5)

if (buscado is not None):
    aux = buscado

    while (aux.info[5] == persona_buscada) and (aux is not None):
        print(aux.info)
        aux = aux.sig
else:
    print("La persona buscada no se encuentra en la lista")
"""

# D
"""
barridoLista(tareas)


def enRango(dato, min, max):
    if (dato >= min) and (dato <= max):
        return True
    else:
        return False


fecha1 = [1, 1, 2018]
fecha2 = [29, 6, 2019]
print()
print("Tareas entres las fechas " + str(fecha1) + " y " + str(fecha2) + ":")

aux = tareas.inicio

while (aux is not None):
    if enRango(aux.info[4], fecha1[2], fecha2[2]) and enRango(aux.info[3], fecha1[1], fecha2[1]) and enRango(aux.info[2], fecha1[0], fecha2[0]):
        print(aux.info)
    aux = aux.sig
"""

# EJERCICIO 17
# Codigo = 0, precio = 1, tipo(nombre) = 2, marca = 3, modelo = 4, cantidad = 5

"""
def cargarStock(lista, cant, campo):

    while (lista.tamanio < cant):
        tipo = choice(tipos)
        if (busqueda(lista, tipo, campo) is None):
            codigo, precio, marca = articulos.get(tipo)
            modelo = "Modelo" + str(randint(1, 1000))
            cantidad = randint(1, 100)
            articulo = [codigo, precio, tipo, marca, modelo, cantidad]

            inserCampo(lista, articulo, campo)


local, provA, provB = Lista(), Lista(), Lista()

articulos = {
             "Pendrive": [125, 1000, "Kingston"],
             "Disco Solido": [12, 2000, "WD"],
             "Teclado Inalambrico": [3, 1500, "Aorus"],
             "Estabilizador": [11, 1800, "Sur Electric"],
             "Mouse": [77, 300, "Sentey"],
             "Cable USB": [59, 150, "Desconocido"]
}

tipos = ["Pendrive", "Disco Solido", "Teclado Inalambrico", "Estabilizador",
         "Mouse", "Cable USB"]

cargarStock(local, 2, 2)
cargarStock(provA, 4, 2)
cargarStock(provB, 3, 2)

print("Stock del local")
barridoLista(local)
print()
print("Proveedor A")
barridoLista(provA)
print()
print("Proveedor B")
barridoLista(provB)
print()
"""

# A y C
"""
aux = provA.inicio

while (aux is not None):
    art = busquedaListaCampo(local, aux.info[2], 2)
    if (art is None):
        inserCampo(local, aux.info, 2)
    else:
        art.info[5] += aux.info[5]
    aux = aux.sig

aux = provB.inicio

while (aux is not None):
    art = busquedaListaCampo(local, aux.info[2], 2)
    if (art is None):
        inserCampo(local, aux.info, 2)
    else:
        art.info[5] += aux.info[5]
    aux = aux.sig

print("Stock de local actualizada con proveedores:")
barridoLista(local)
print()
"""

# B
"""
if local.tamanio == 1:
    if (local.info[2] == "Pendrive") and (local.info[3] == "Kingston"):
        local.inicio = None
else:
    ant = local.inicio
    act = ant.sig
    while (act is not None) and ((act.info[2] != "Pendrive") or (act.info[3] != "Kingston")):
        ant = ant.sig
        act = act.sig

    if act is not None:
        ant.sig = act.sig

print()
print("Lista del local  con producto Pendrive Kingston eliminado")
barridoLista(local)
"""

# D Hay que haber ejecutado el punto A, ya que deja actualizada la lista local
"""
disco_duro = busquedaListaCampo(local, "Disco Solido", 2)
tecl_inalam = busquedaListaCampo(local, "Teclado Inalambrico", 2)

if disco_duro is not None:
    costo_existencia = disco_duro.info[1] * disco_duro.info[5]
    print("Costo de existencia de disco duro: " + str(costo_existencia))
else:
    print("No se encuentra disco duro en la lista de stock del local")

if tecl_inalam is not None:
    costo_existencia = tecl_inalam.info[1] * tecl_inalam.info[5]
    print("Costo de existencia de teclado inalambrico: " + str(costo_existencia))
else:
    print("No se encuentra teclado inalambrico en la lista de stock del local")
"""

# EJERCICIO 18

# Usuario: nombre = 0, commits = 1  -->  Ordenado por nombre
# Commit: fyh = 0, msj = 1, archivo = 2, lineas = 3  -->  Ordenador por lineas

"""
def gen_datetime(min_year=2012, max_year=datetime.datetime.now().year):
    # genera un datatime en formato yyyy-mm-dd hh:mm:ss.000000
    start = datetime.datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + datetime.timedelta(days=365 * years)
    return start + (end - start) * random()


usuarios = Lista()

for i in range(1, 10):  # Usuarios
    commits = Lista()
    nombre = "Usuario" + str(i)

    for j in range(0, randint(1, 11)):  # Commits
        fyh = gen_datetime()
        msj = "Mensaje" + str(i + j)
        archivo = choice(["Archivo" + str(randint(0, 10)), "Test.py"])
        cant_lineas = randint(0, 500)
        if (cant_lineas != 0):
            lineas = int(choice(["-", "+"]) + str(cant_lineas))
        else:
            lineas = cant_lineas
        commit = [fyh, msj, archivo, lineas]
        inserCampo(commits, commit, 3)

    usuario = [nombre, commits]
    inserCampo(usuarios, usuario, 0)
"""

# A
"""
aux = usuarios.inicio
max = aux

while aux is not None:
    if (aux.info[1].tamanio > max.info[1].tamanio):
        max = aux
    aux = aux.sig

usuarios_con_mayor_commit = [max]

aux = usuarios.inicio
while (aux is not None):
    if (aux.info[1].tamanio == max.info[1].tamanio):
        usuarios_con_mayor_commit.append(aux)
    aux = aux.sig

print("Usuario/s con mayor cantidad de commits (" + str(max.info[1].tamanio) +
      ")")
for usuario in usuarios_con_mayor_commit:
    print(usuario.info)
"""

# B
"""
aux_usuario = usuarios.inicio

user_agreg = aux_usuario
max = ultimoNodo(aux_usuario.info[1]).info[3]

user_elim = aux_usuario
min = aux_usuario.info[1].inicio.info[3]

while (aux_usuario is not None):
    # Lista de commits
    commits = aux_usuario.info[1]
    # Primero y último commit de la lista
    pri_commit = commits.inicio
    ult_commit = ultimoNodo(commits)
    # Cantidad de líneas de primer y último commit
    lineas_pri = pri_commit.info[3]
    lineas_ult = ultimoNodo(commits).info[3]

    if lineas_pri < 0:
        if (lineas_pri > min):
            min = lineas_pri
            user_elim = aux_usuario
    else:
        if (lineas_ult > max):
            max = lineas_ult
            user_agreg = aux_usuario

    aux_usuario = aux_usuario.sig

print("Usuario que agregó mayor cantidad de lineas: " + str(max))
print(user_agreg.info)
print("Usuario que eliminó menor cantidad de lineas: " + str(min))
print(user_elim.info )
"""

# C
"""
hora_limite = datetime.time(19, 45, 0)
print("Usuarios que han realizado cambios después de las 19:45")

aux_usuario = usuarios.inicio

while (aux_usuario is not None):
    aux_commit = aux_usuario.info[1].inicio

    while (aux_commit is not None):
        name_archivo = aux_commit.info[2]
        hora = aux_commit.info[0].time()

        if (aux_commit.info[3] != 0) and (name_archivo == "Test.py") and (hora > hora_limite):
            print(aux_usuario.info)
            break

        aux_commit = aux_commit.sig

    aux_usuario = aux_usuario.sig
"""

# D
"""
print("Usuarios que realizaron commits con cero lineas agregadas/eliminadas")
aux_usuario = usuarios.inicio

while (aux_usuario is not None):
    encontrado = busqueda(aux_usuario.info[1], 0, 3)
    if (encontrado is not None):
        print(aux_usuario.info)

    aux_usuario = aux_usuario.sig
"""

# EJERICIO 20

# nombre = 0, precio = 1, calificacion = 2
"""
productos = Lista()  # Ordenada por nombre
aux_productos = Lista()  # Ordenada por calificación

while productos.tamanio < 10:
    nombre = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if busquedaListaCampo(productos, nombre, 0) is None:
        precio = randint(10, 10000)
        calificacion = randint(1, 5)

        producto = [nombre, precio, calificacion]

        inserCampo(productos, producto, 0)
        inserCampo(aux_productos, producto, 2)

"""
# A
"""
producto_buscado = "A"

encontrado = busquedaListaCampo(productos, producto_buscado, 0)
if (encontrado is not None):
    print(encontrado.info)
else:
    print("El producto no se encuentra en la lista")
"""

# B
"""
lista_mostrada = productos

opcion = int(input("Ordenar lista por: 1-Nombre, 2-Calificación, Otro para salir"))

while (opcion == 1) or (opcion == 2):
    if opcion == 1:
        lista_mostrada = productos
        print("Lista ordenada por Nombre")
    else:
        lista_mostrada = aux_productos
        print("Lista ordenada por calificacion")
    barridoLista(lista_mostrada)
    print()

    opcion = int(input("Ordenar lista por: 1-Nombre, 2-Calificación, Otro para salir"))
"""

# C
"""
print("Lista ordenada por calificación:")
barridoLista(aux_productos)
"""

# D
"""
barridoLista(aux_productos)
print()

calificacion = 3

prod_min = None
precio_min = 0

aux = busquedaListaCampo(aux_productos, 3, 2)

if (aux is not None):
    prod_min = aux
    precio_min = prod_min.info[1]

    while (aux is not None) and (aux.info[2] == calificacion):
        if precio_min > aux.info[1]:
            prod_min = aux
            precio_min = prod_min.info[1]
        aux = aux.sig

if prod_min is None:
    print("No hay productos de calificación 3")
else:
    print("Producto más barato de calificación 3")
    print(prod_min.info)
"""

# E
"""
inserCampo(productos, ["Ha", 100, 3], 0)
inserCampo(productos, ["Hh", 700, 1], 0)
barridoLista(productos)
print()
print("A continuacion los precios de los productos que empiezan por H")

aux = productos.inicio

while (aux is not None) and (aux.info[0][0].capitalize() < "H"):
    aux = aux.sig
if aux is not None:
    while (aux is not None) and (aux.info[0][0].capitalize() == "H"):
        print("Precio: " + str(aux.info[1]))
        aux = aux.sig
"""
