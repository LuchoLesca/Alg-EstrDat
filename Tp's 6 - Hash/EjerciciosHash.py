from TDA_Lista import *
from random import choice, randint


def crearTablaAbierta(tamanio):
    '''Crea un tabla hash del tamanio ingresado'''
    tabla = []
    for i in range(0, tamanio):
        tabla.append(Lista())
    return tabla


def crearTablaCerrada(tamanio):
    '''Crea un tabla hash del tamanio ingresado'''
    tabla = []
    for i in range(0, tamanio):
        tabla.append(None)
    return tabla


def barridoHashAbierta(tabla):
    '''Realiza un barrido total de la tabla con su contenido'''
    for lista in tabla:
        if lista.tamanio != 0:
            barridoLista(lista)


def barridoHashCerrada(tabla):
    '''Realiza un barrido total de la tabla con su contenido'''
    for elemento in tabla:
        if elemento is not None:
            print(elemento)


def rehash(tabla, original):
    indice = original + 1
    if indice == len(tabla):
        indice = 0
    while (tabla[indice] is not None) and (indice != original):
        indice += 1
        if indice == len(tabla):
            indice = 0

    if indice == original:
        indice = None

    return indice


# EJERCICIO 1
"""
tabla = crearTablaAbierta(28)


def hash(palabra):
    if len(palabra) > 0:
        clave = ord(palabra[0].capitalize()) - 65

        return clave


def insertarPalabra(tabla, palabra, descripcion):
    clave = hash(palabra)
    indice = clave % len(tabla)
    inserCampo(tabla[indice], [palabra, descripcion], 0)


def busquedaPalabra(tabla, palabra):
    indice = hash(palabra)

    return busquedaListaCampo(tabla[indice], palabra, 0)


def eliminarPalabra(tabla, palabra):
    indice = hash(palabra)

    if busquedaListaCampo(tabla[indice], palabra, 0) is not None:
        eliminarCampo(tabla[indice], palabra, 0)


# A, B y C

# Insersión de palabras
insertarPalabra(tabla, "Casa", "Descripcion de Casa")
insertarPalabra(tabla, "Añejo", "Descripcion de Añejo.")

print("DICICONARIO COMPLETO:")
barridoHashAbierta(tabla)
print()

# Busqueda de palabras
print("BUSQUEDA:")

encontrado = busquedaPalabra(tabla, "Añejo")
if encontrado is not None:
    print("Palabra encontrada: " + str(encontrado.info))
else:
    print("La palabra Añejo no se encontró")

encontrado = busquedaPalabra(tabla, "Alan")
if encontrado is not None:
    print("Palabra encontrada: " + str(encontrado.info))
else:
    print("La palabra Alan no se encontró")

# Eliminación de palabras
print()
print("Luego de intentar eliminar Añejo y Palo del diccionario:")
eliminarPalabra(tabla, "Añejo")
eliminarPalabra(tabla, "Palo")
print("DICCIONARIO ACTUALIZADO:")
barridoHashAbierta(tabla)
"""


# EJERCICIO 2
"""
tabla = crearTablaAbierta(97)

# telefono = 0, apellido y nombre = 1, dir = 2


def telefonoRandom():
    caracteristica, numero = "", ""

    for i in range(0, randint(3, 5)):
        caracteristica += str(randint(0, 9))
    for i in range(0, randint(6, 8)):
        numero += str(randint(0, 9))
    telefono = caracteristica + "-" + numero

    return telefono


def hash(telefono):
    area, numero = telefono.split("-")
    area = int(area)
    numero = int(numero)
    return (area + numero)


def insertarTelefono(tabla, telefono, nom_y_ap, direccion):
    clave = hash(telefono)
    indice = clave % len(tabla)
    inserCampo(tabla[indice], [telefono, nom_y_ap, direccion], 0)


for i in range(0, 50):
    insertarTelefono(tabla, telefonoRandom(), "Persona" +
                     str(randint(0, 10)), "Dir" + str(randint(0, 10)))


for i in range(0, len(tabla)):
    if tabla[i].tamanio > 0:
        print("En indice " + str(i) + " hay " + str(tabla[i].tamanio) +
              "numeros")
"""

# EJERICICO 3

"""
def cantidadCargados(tabla):
    cont = 0
    for elemento in tabla:
        if elemento is not None:
            cont += 1
    return cont


def buscarCatedra(tabla, catedra):
    clave = hash(catedra[0])
    indice = clave % len(tabla)
    if tabla[indice][1] != catedra[1]:
        indice = rehash(tabla, indice)

    return indice


def nuevaCatedra():
    docentes = Lista()
    codigo = randint(0, 100)
    nom_catedra = "Cátedra" + str(randint(0, 150))
    modalidad = choice(["Anual", "Cuatrimestral"])
    cant_horas = randint(1, 20)
    catedra = [codigo, nom_catedra, modalidad, cant_horas, docentes]

    return catedra


def agregarDocenteRandom(tabla, catedra):
    nombre = "Docente" + str(randint(0, 20))
    anios_catedra = randint(0, 10)

    docente = [nombre, amios_catedra]

    indice = buscarCatedra(tabla, catedra)

    if indice is not None:
        insertar(tabla[indice][4], docente)


# Código = 0 cátedra = 1, modalidad = 2, horas = 3 docentes = 4
# Nombre = 0, anios_catedra = 1


tabla = crearTablaCerrada(97)


def hash(codigo):
    return codigo*3


def insertarCatedra(tabla, dato):
    clave = hash(dato[0])
    indice = clave % len(tabla)
    if tabla[indice] is None:
        tabla[indice] = dato
    else:
        indice = rehash(tabla, indice)
        if indice is not None:
            tabla[indice] = dato
        else:
            print("No hay más lugares en la tabla")


cantidad_insertar = 50
for i in range(0, cantidad_insertar):
    catedra = nuevaCatedra()
    insertarCatedra(tabla, catedra)

barridoHashCerrada(tabla)
print("Cantidad de lugares ocupados: " + str(cantidadCargados(tabla)))
"""


# EJERCICIO 4
"""

def hash(clave):
    indice = 0
    for elemento in clave:
        indice += ord(elemento)
    return indice


def factorCarga(tabla):
    espacios_ocupados = 0
    for personaje in tabla:
        if personaje is not None:
            espacios_ocupados += 1

    factor = (espacios_ocupados*100) / len(tabla)
    return factor


def expandirTabla(tabla):
    nueva_tabla = crearTablaCerrada(len(tabla)*2)

    for personaje in tabla:
        if personaje is not None:
            insertarPersonaje(nueva_tabla, personaje)

    return nueva_tabla


def insertarPersonaje(tabla, personaje):
    indice = hash(personaje)
    indice = indice % len(tabla)

    if tabla[indice] is not None:
        indice = rehash(tabla, indice)

    tabla[indice] = personaje

    if factorCarga(tabla) > 75:
        tabla = expandirTabla(tabla)

    return tabla


personajes = crearTablaCerrada(20)

for i in range(0, 15):
    personajes = insertarPersonaje(personajes, "Personaje" + str(i))

# Con 15 personajes, esta tabla de 20 posiciones tiene el factor de carga de 75
print(len(personajes))

# Al agregar 2, se excede el factor de carga, por lo que la tabla se expande
personajes = insertarPersonaje(personajes, "PjRandom1")
personajes = insertarPersonaje(personajes, "PjRandom2")

print(len(personajes))
"""


# EJERCICIO 5
"""
# nombre = 0, apellido = 1, email = 2
contactos = crearTablaCerrada(97)

cant_contactos = 78


def insertarContacto(tabla, contacto):
    indice = hash(contacto[0] + contacto[1])
    indice = indice % len(tabla)
    if tabla[indice] is None:
        tabla[indice] = contacto
    else:
        indice = rehash(tabla, indice)
        if indice is not None:
            tabla[indice] = contacto
        else:
            print("No hay más lugares en la tabla")


for i in range(0, cant_contactos):
    nombre = "Nombre" + str(randint(0, 100))
    apellido = "Apellido" + str(randint(0, 100))
    email = "Email" + str(randint(0, 50))

    insertarContacto(contactos, [nombre, apellido, email])


barridoHashCerrada(contactos)

cantidad = 0
for contacto in contactos:
    if contacto is not None:
        cantidad += 1
print("Cantidad cargados: " + str(cantidad))
"""

# EJERCICIO 6
"""
tamanio_tablas = 5000
troopers_digitos = crearTablaAbierta(tamanio_tablas)
troopers_legion = crearTablaAbierta(tamanio_tablas)

legiones = ["FL", "TF", "TK", "CT", "FN", "FO"]


def hash(clave):
    indice = 0
    if len(clave) == 2:
        indice = (ord(clave[0])*3) + (ord(clave[1])*7)
    else:
        indice = ((ord(clave[0]) * ord(clave[1])) + ord(clave[2]))
    return indice


def busquedaTrooper(tabla, digitos):
    indice = hash(digitos)
    indice = indice % len(tabla)
    return tabla[indice]


def nuevoTrooper():
    legion = choice(legiones)
    cohoerte = str(randint(0, 9))
    siglo = str(randint(0, 9))
    escuadra = str(randint(0, 9))
    id_trooper = str(randint(0, 9))

    trooper = legion + "-" + cohoerte + siglo + escuadra + id_trooper
    return trooper


def insertarTrooperLegion(tabla, trooper):
    legion, codigo = trooper.split("-")

    indice = hash(legion)
    indice = indice % len(tabla)
    insertar(tabla[indice], trooper)


def insertarTrooperDigitos(tabla, trooper):
    legion, codigo = trooper.split("-")
    indice = hash(codigo[1:len(codigo)])
    indice = indice % len(tabla)
    insertar(tabla[indice], trooper)


def agregarTrooper(trooper):
    insertarTrooperLegion(troopers_legion, trooper)
    insertarTrooperDigitos(troopers_digitos, trooper)


for i in range(0, 2000):
    agregarTrooper(nuevoTrooper())
"""
# barridoHashAbierta(troopers_legion)
# print()
# barridoHashAbierta(troopers_digitos)

# C
"""
mision_asalto = []
mision_exploracion = []

buscado = busquedaTrooper(troopers_digitos, "781")
if buscado.tamanio > 0:
    aux = buscado.inicio
    while aux is not None:
        if aux.info[4:] == "781":
            mision_asalto.append(aux.info)
        aux = aux.sig

buscado = busquedaTrooper(troopers_digitos, "537")
if buscado.tamanio > 0:
    aux = buscado.inicio
    while aux is not None:
        if aux.info[4:] == "537":
            mision_exploracion.append(aux.info)
        aux = aux.sig


print("Troopers asignados a misión de asalto (terminados en 781):")
print(mision_asalto)
print()
print("Troopers asignados a misión de exploración (terminados en 537):")
print(mision_exploracion)
print()
"""
# D
"""
mision_holt = []
mision_endor = []

buscado = busquedaTrooper(troopers_legion, "CT")
if buscado.tamanio > 0:
    aux = buscado.inicio
    while aux is not None:
        if aux.info[:2] == "CT":
            mision_holt.append(aux.info)
        aux = aux.sig

buscado = busquedaTrooper(troopers_legion, "TF")
if buscado.tamanio > 0:
    aux = buscado.inicio
    while aux is not None:
        if aux.info[0:2] == "TF":
            mision_endor.append(aux.info)
        aux = aux.sig


print("Troopers asignados a misión en Holt (CT):")
print(mision_holt)
print()
print("Troopers asignados a misión en Endor (TF):")
print(mision_endor)
"""
