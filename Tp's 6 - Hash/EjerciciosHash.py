from TDA_Lista import *
from random import choice, randint
from math import pow


def crearTablaAbierta(tamanio):
    '''Crea un tabla hash abierta del tamanio ingresado'''
    tabla = []
    for i in range(0, tamanio):
        tabla.append(Lista())
    return tabla


def crearTablaCerrada(tamanio):
    '''Crea un tabla hash cerrada del tamanio ingresado'''
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
    indice = hash(telefono) % len(tabla)
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


# EJERICICO 7   <<<<<<<<< FALLTA HACER ESTE
# POKEMON SE CONOCE:
# numero = 0, nombre = 1, tipo = 2, nivel = 3

tipos = ["Normal", "Lucha", "Volador", "Veneno", "Tierra", "Roca", "Bicho",
         "Fantasma", "Acero", "Fuego", "Agua", "Planta", "Electrico", "Hielo",
         "Psiquico", "Dragon", "Hada", "Siniestro"]

tabla_tipos = crearTablaCerrada(29)  # Tipos (hay 18)


def nuevoPokemon(numero=0):
    numero = numero
    nombre = "Nombre"+str(numero)
    # cant_tipo = randint(1, 2)
    cant_tipo = 1
    tipo = choice(tipos)
    if cant_tipo == 2:
        tipo += "/" + choice(tipos)
    nivel = randint(1, 200)
    return [numero, nombre, tipo, nivel]


def hash(clave):  # Tipo de pokemon
    if type(clave) is int:
        clave = str(clave)
    indice = 0
    for elemento in clave:
        indice += ord(elemento)
    return indice


def comprobarTipoHashAbierta(tabla):
    tipo = None
    for elemento in tabla:
        if elemento.tamanio > 0:
            tipo = elemento.inicio.info[2]
            break
    return tipo


def sondeoTipo(tabla, tipo, indice):
    while (tabla[indice] is not None) and (comprobarTipoHashAbierta(tabla[indice]) != tipo):
        indice += 1
        if indice == len(tabla):
            indice = 0

    return indice


def insertarEnTablaNumeros(tabla, pokemon):
    indice = hash(pokemon[0]) % len(tabla)
    inserCampo(tabla[indice], pokemon, 0)


def insertarEnTablaTipos(tabla_tipos, pokemon):
    tipo = pokemon[2]

    indice = hash(tipo) % len(tabla_tipos)

    if tabla_tipos[indice] is None:

        tabla_tipos[indice] = crearTablaAbierta(15)
        insertarEnTablaNumeros(tabla_tipos[indice], pokemon)
    else:

        if comprobarTipoHashAbierta(tabla_tipos[indice]) == tipo:
            insertarEnTablaNumeros(tabla_tipos[indice], pokemon)

        else:
            indice = sondeoTipo(tabla_tipos, tipo, indice)

            if tabla_tipos[indice] is None:
                tabla_tipos[indice] = crearTablaAbierta(15)
            insertarEnTablaNumeros(tabla_tipos[indice], pokemon)


pokemons_ingresados = []

for i in range(100):
    pokemon = nuevoPokemon(i)
    pokemons_ingresados.append(pokemon)
    insertarEnTablaTipos(tabla_tipos, pokemon)


print("Lista de pokemons ingresados")
for p in pokemons_ingresados:
    print(p)
print()

print("Elementos que hay cargados en la tabla")
for elemento in tabla_tipos:
    if elemento is not None:
        print(comprobarTipoHashAbierta(elemento))

print()
print()


# EJERCICIO 8
"""
def cifrar(oracion):
    clave = ""
    for letra in oracion:
        parte1 = str(ord(letra)*37)
        parte2 = hex(ord(letra)*2)
        clave += parte1[0] + parte2[1] + parte2[3] + parte1[1] + parte1[2] + parte2[0] + parte1[3] + parte2[2]
    return clave


def descifrar(clave):
    oracion = ""
    while len(clave) > 0:
        caracter = ""
        caracter += clave[0] + clave[3] + clave[4] + clave[6]
        clave = clave[8:]

        caracter = int(caracter)
        caracter = int(caracter/37)
        caracter = chr(caracter)
        oracion += caracter
    return oracion


para_cifrar = "Los hash son usados ampliamente en toda {internet}, los hash nos permiten cifrar los datos con mucha seguridad, ya que si una persona intercepta el código hash, no sabrá el valor original de los datos."
print("Oracion original:")
print(para_cifrar)
print()

cifrado = cifrar(para_cifrar)
print("Mensaje cifrado:")
print(cifrado)
print()

descifrado = descifrar(cifrado)
print("Mensaje descifrado:")
print(descifrado)
"""


# EJERCICIO 9
"""
tabla_codif = crearTablaCerrada(10)

tabla_codif[0] = "#?&"
tabla_codif[1] = "abc"
tabla_codif[2] = "def"
tabla_codif[3] = "ghi"
tabla_codif[4] = "jkl"
tabla_codif[5] = "mnñ"
tabla_codif[6] = "opq"
tabla_codif[7] = "rst"
tabla_codif[8] = "uvw"
tabla_codif[9] = "xyz"


def hash(caracter):
    cadena = ""
    ascii = ord(caracter)
    ascii = str(ascii)
    for digito in ascii:
        dig = int(digito)
        clave = tabla_codif[dig]
        cadena += clave
    cadena += "%"
    return cadena


def codificar(mensaje):
    cadena = ""
    for letra in mensaje:
        cadena += hash(letra)
    return cadena


def decodificar(codigo):
    mensaje = ""
    codigo_div = codigo.split("%")
    for segmento in codigo_div:
        if len(segmento) > 0:
            digitos = ""
            for i in range(0, len(segmento), 3):
                if segmento[i] == "#":
                    digitos += "0"
                elif segmento[i] == "a":
                    digitos += "1"
                elif segmento[i] == "d":
                    digitos += "2"
                elif segmento[i] == "g":
                    digitos += "3"
                elif segmento[i] == "j":
                    digitos += "4"
                elif segmento[i] == "m":
                    digitos += "5"
                elif segmento[i] == "o":
                    digitos += "6"
                elif segmento[i] == "r":
                    digitos += "7"
                elif segmento[i] == "u":
                    digitos += "8"
                elif segmento[i] == "x":
                    digitos += "9"
            digitos = int(digitos)

            mensaje += chr(digitos)

    return mensaje


oracion = "Se debe utilizar una tabla hash para guardar los valores de codificacion y decodificacion respectivamente que se vayan utilizando"
print("Oración original")
print(oracion)
print()

print("Mensaje codificado:")
msj_codificado = codificar(oracion)
print(msj_codificado)
print()

print("Mensaje decodificado:")
msj_decodificado = decodificar(msj_codificado)
print(msj_decodificado)
"""


# EJERCICIO 10   <<<<<<< FALTA TEMRINAR

"""
def hash_djb2(string):
    hash = 5381
    for caracter in string:
        hash = ((hash << 5) + hash) + ord(caracter)
    return hash & 0xFFFFFFFF


tabla = crearTablaCerrada(100)


def calcComplemento(caracter):
    if ord(caracter) <= 78:
        return 79 + ord(caracter) - 32
    else:
        return 32 + ord(caracter) - 79


def chrTo5Chrs(caracter):
    devuelve = ""
    # i
    caracter_ascii = ord(caracter)
    caracter_ascii *= 37
    # print(caracter_ascii)
    # ii
    complemento = calcComplemento(caracter)
    # iii
    caracter_ascii = str(caracter_ascii)
    for digito in caracter_ascii:
        digito = int(digito)
        num = pow(digito, 2) + 35
        caracter = chr(int(num))
        devuelve += caracter
    # iv
    devuelve += chr(complemento)
    return devuelve


def codificar(oracion):
    oracion_codificada = ""
    for caracter in oracion:
        clave = chrTo5Chrs(caracter)
        oracion_codificada += clave

    return oracion_codificada


mensaje_a_codificar = "Esta es la prueba de una oracion larga. Al realizar esta prueba, se comprueba la cantidad de código de 5 caracteres que puede almacenar la carotida"
mensaje_codificado = codificar(mensaje_a_codificar)
mensaje_codificado_2 = hash_djb2(mensaje_codificado)
# print((mensaje_codificado_2) % len(tabla))
"""
