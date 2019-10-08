from TDA_Lista import *
from random import choice, randint
from math import pow, sqrt


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


# EJERICICO 7
# POKEMON SE CONOCE:
# numero = 0, nombre = 1, tipo = 2, nivel = 3
"""
tipos = ["Normal", "Lucha", "Volador", "Veneno", "Tierra", "Roca", "Bicho",
         "Fantasma", "Acero", "Fuego", "Agua", "Planta", "Electrico", "Hielo",
         "Psiquico", "Dragon", "Hada", "Siniestro"]

tabla_tipos = crearTablaCerrada(29)  # Tipos (hay 18)


def nuevoPokemon(numero=0):
    numero = numero
    nombre = "Nombre"+str(numero)
    cant_tipo = randint(1, 2)
    tipo = choice(tipos)
    if cant_tipo == 2:
        tipo += "/" + choice(tipos)
    nivel = randint(1, 200)
    return [numero, nombre, tipo, nivel]


def hash(clave):
    if type(clave) is int:
        clave = str(clave)
    indice = 0
    for elemento in clave:
        indice += ord(elemento)
    return indice


def sondeoTipo(tabla, tipo, indice):
    while (tabla[indice] is not None) and (tabla[indice][0] != tipo):
        indice += 1
        if indice == len(tabla):
            indice = 0

    return indice


def insertarEnTablaNumeros(tabla, pokemon):
    indice = hash(pokemon[0]) % len(tabla)
    inserCampo(tabla[indice], pokemon, 0)


def insertarEnTablaTipos(tabla_tipos, pokemon):
    tippos = pokemon[2].split("/")

    for tipo in tippos:

        indice = hash(tipo) % len(tabla_tipos)

        if tabla_tipos[indice] is None:

            tabla_tipos[indice] = [tipo, crearTablaAbierta(15)]
            insertarEnTablaNumeros(tabla_tipos[indice][1], pokemon)

        else:

            if tabla_tipos[indice][0] == tipo:
                insertarEnTablaNumeros(tabla_tipos[indice][1], pokemon)

            else:
                indice = sondeoTipo(tabla_tipos, tipo, indice)

                if tabla_tipos[indice] is None:
                    tabla_tipos[indice] = [tipo, crearTablaAbierta(15)]
                insertarEnTablaNumeros(tabla_tipos[indice][1], pokemon)


print("Pokemons ingresados: ")
for i in range(30):
    pokemon = nuevoPokemon(i)
    print(pokemon)
    insertarEnTablaTipos(tabla_tipos, pokemon)

print()
print("Tipos que fueron ingresados en la tabla")
for elemento in tabla_tipos:
    if elemento is not None:
        print(elemento[0])

print()
tipo_busq = choice(tipos)
print("Pokemons tipo {0}, {0}/?, o ?/{0}:".format(tipo_busq))
indice = hash(tipo_busq) % len(tabla_tipos)

if (tabla_tipos[indice] is not None) and (tabla_tipos[indice][0] == tipo_busq):
    barridoHashAbierta(tabla_tipos[indice][1])
else:
    indice = sondeoTipo(tabla_tipos, tipo_busq, indice)
    if tabla_tipos[indice] is not None:
        barridoHashAbierta(tabla_tipos[indice][1])
    else:
        print("No hay pokemons de tipos " + tipo_busq + " agregados")
"""


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


# EJERCICIO 10   <<<< Flta agregarle que trabaje con la tabla ascii


def hash_djb2(string):
    hash = 5381
    for caracter in string:
        hash = ((hash << 5) + hash) + ord(caracter)
    return hash & 0xFFFFFFFF


def calcComplemento(caracter):
    if ord(caracter) <= 78:
        return 79 + ord(caracter) - 32
    else:
        return 32 + ord(caracter) - 79


def chrTo5Chrs(caracter):
    caracteres = ""
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
        num = pow(digito, 2) + complemento
        caracter = chr(int(num))
        caracteres += caracter
    # iv
    caracteres += chr(complemento)
    return caracteres


def chrsTo1Chr(segmento):
    num_cuatro_digitos = ""

    pri_chr = segmento[:4]
    ult_chr = segmento[4]

    complemento = ord(ult_chr)

    for elemento in pri_chr:
        elemento = ord(elemento) - complemento
        elemento = int(sqrt(elemento))
        elemento = str(elemento)
        num_cuatro_digitos += elemento

    num_cuatro_digitos = int(num_cuatro_digitos)
    chr_ascii = int(num_cuatro_digitos/37)
    caracter = chr(chr_ascii)

    return caracter


def decodificarMensaje(mensaje):
    oracion = ""
    i = 0

    while i < len(mensaje):
        segmento = mensaje[i:i+5]
        caracter = chrsTo1Chr(segmento)

        oracion += caracter

        i += 5

    return oracion


def sondeo(tabla, indice, codigo):
    while (tabla[indice] is not None) and (tabla[indice] != codigo):
        indice += 1
        if indice == len(tabla):
            indice = 0

    return indice

"""
def codificarMensaje(texto):
    oracion_codificada = ""
    for caracter in texto:
        codigo = chrTo5Chrs(caracter)
        oracion_codificada += codigo

    return oracion_codificada
"""

"""
mensaje_original = "Mensaje de prueba de codificación"
mensaje_codificado = codificarMensaje(mensaje_original)
mensaje_decodificado = decodificarMensaje(mensaje_codificado)

print("Mensaje original:")
print(mensaje_original)
print()
print("Mensaje codificado:")
print(mensaje_codificado)
print()
print("Mensaje decodificado:")
print(mensaje_decodificado)
print()
"""
tabla = crearTablaCerrada(200)

mensaje_codificado = "x}tFa=PP_OAx998SGDC;Kr2O?p??PP_OQBQQAPA@q@>f555?g?g6SGDCPP_OTH]]DCzzS:?g?g6N>GG>QBQQASGDC?g?g6PP_OByIy9;Kr2PP_OPA@q@@hhG7VOJFTH]]D=XX=4;Kr2>f555PA@q@PP_O;Kr2Fa=PP_OByIy9PA@q@N>GG><W7W3SGDC?g?g6PP_OQBQQASGDCCzzS:N>GG>CzzS:UIIECzzS:WPkkGPA@q@\_[PP_O{w3.{3*wts,#,3#tppPP_O?g?g6TH]]DUIIEò»¶Ë²PP_OSGDC?g?g6VOJFO?p??CzzS:?g?g6O?p??>f555PA@q@PP_OVOJFO?p??PP_O;Kr2SGDCTH]]D?g?g6O?p??;Kr2Fa=PP_OQBQQA;Kr2SGDC;Kr2PP_O>f555?g?g6TH]]DUIIESGDCVOJFCzzS:SGDCPP_O;Kr2PP_ON>GG>CzzS:TH]]DPP_O?g?g6O?p???g?g6N>GG>CzzS:Ax998PA@q@TH]]DPP_O>f555?g?g6PP_OVOJFO?p??PP_OTH]]DPA@q@Fa=PA@q@PP_OAx998PA@q@Fa=QBQQA?g?g6\_[PP_O?g?g6TH]]DUIIEúÞ¾»ºO?p??PP_O>f555PA@q@O?p??>f555?g?g6PP_O?g?g6TH]]DUIIEúÞ¾»ºO?p??PP_OTH]]DCzzS:O?p??PP_OCzzS:N>GG>QBQQAPA@q@SGDCUIIE;Kr2SGDCPP_OFa=PA@q@TH]]DPP_O?g?g6@hhG7?g?g6=XX=4UIIECzzS:WPkkGPA@q@TH]]DPP_ORCCBVOJF?g?g6PP_OQBQQAPA@q@TH]]D?g?g6;Kr2O?p??PP_OZZ{{JPP_O?g?g6O?p??PP_O=XX=4VOJF?g?g6TH]]DUIIECzzS:ĄĕĕÅÄO?p??PP_O>f555?g?g6PP_OByIy9PA@q@SGDC;Kr2TH]]D^]a]PP_OtppTH]]Dþïâď¾PP_O>f555?g?g6PP_OTH]]DCzzS:N>GG>QBQQAFa=?g?g6PP_O=XX=4;Kr2<W7W3;Kr2Fa=Fa=?g?g6SGDCPA@q@TH]]DPP_OByIy9?g?g6PP_OFa=PA@q@Ax998SGDC;Kr2>f555PA@q@PP_OUIIEPA@q@N>GG>;Kr2SGDCPP_O?g?g6Fa=PP_OQBQQAPA@q@>f555?g?g6SGDCPP_O>f555?g?g6PP_OFa=PA@q@TH]]DPP_OwtsCzzS:PA@q@TH]]D?g?g6TH]]D^]a]"

mensaje_decodificado = decodificarMensaje(mensaje_codificado)

print("Mensaje 1:")
print(mensaje_decodificado)
print()


'''
mensaje_codificado = "x}tFa=PP_ON>GG>CzzS:úÞ¾»ºSGDC=XX=4PA@q@Fa=?g?g6TH]]DPP_Oc¢¢bPP_O>f555?g?g6PP_O;Kr2Ax998PA@q@TH]]DUIIEPA@q@\_[PP_OQBQQA;Kr2SGDCUIIECzzS:SGDCò»¶Ë²PP_OVOJFO?p??PP_O=XX=4;Kr2SGDCAx998;Kr2N>GG>?g?g6O?p??UIIEPA@q@PP_O>f555?g?g6PP_OSGDCCzzS:@hhG7Fa=?g?g6TH]]DPP_O>f555?g?g6PP_O;Kr2TH]]D;Kr2Fa=UIIEPA@q@PP_O>f555?g?g6PP_O?g?g6O?p???g?g6SGDCAx998þïâď¾;Kr2\_[PP_O>f555?g?g6PP_OFa=PA@q@TH]]DPP_OeµedPP_O=XX=4;Kr2N>GG>CzzS:PA@q@O?p???g?g6TH]]DPP_OFa=PA@q@TH]]DPP_OUIIESGDC?g?g6TH]]DPP_OQBQQASGDCCzzS:N>GG>?g?g6SGDCPA@q@TH]]DPP_OTH]]D?g?g6SGDCò»¶Ë²O?p??PP_OQBQQA;Kr2SGDC;Kr2PP_O>f555CzzS:TH]]DUIIESGDC;Kr2?g?g6SGDCPP_O;Kr2PP_OFa=PA@q@TH]]DPP_O;Kr2Fa=CzzS:;Kr2>f555PA@q@TH]]D\_[PP_OFa=PA@q@TH]]DPP_O>f555PA@q@TH]]DPP_OĜÏäËËFa=UIIECzzS:N>GG>PA@q@TH]]DPP_OTH]]DCzzS:N>GG>VOJFFa=;Kr2SGDCò»¶Ë²O?p??PP_OQBQQASGDCPA@q@<W7W3Fa=?g?g6N>GG>;Kr2TH]]DPP_ON>GG>?g?g6=XX=4ò»¶Ë²O?p??CzzS:=XX=4PA@q@TH]]DPP_OZZ{{JPP_OTH]]D?g?g6PP_O>f555?g?g6TH]]DWPkkGCzzS:;Kr2SGDCò»¶Ë²O?p??PP_O?g?g6O?p??PP_OFa=;Kr2PP_OUIIE?g?g6SGDC=XX=4?g?g6SGDCPP_OTH]]D;Kr2Fa=CzzS:>f555;Kr2PP_OSGDCVOJFN>GG><W7W3PA@q@PP_O;Kr2Fa=PP_OO?p??PA@q@SGDCPA@q@?g?g6TH]]DUIIE?g?g6PP_OQTTQP{w;Kr2CzzS:Fa=PP_O{wZZ{{J>f555SGDC;Kr2QTTQP"
mensaje_decodificado = decodificarMensaje(mensaje_codificado)
print("Mensaje 3:")
print(mensaje_decodificado)
print()
'''
'''
mensaje_codificado = 'x}tFa=PP_O=XX=4PA@q@N>GG>;Kr2O?p??>f555;Kr2O?p??UIIE?g?g6PP_O,#,3#?g?g6>f555PP_O-$U%$EU<VOJFFa=Fa=PP_OUIIESGDC;Kr2O?p??TH]]DQBQQAPA@q@SGDCUIIE;Kr2SGDCò»¶Ë²PP_O?g?g6Fa=PP_O.&%e%?g?g6TH]]D?g?g6SGDC;Kr2=XX=4UIIEPA@q@PP_O?g?g6O?p??PP_OTH]]DVOJFPP_OO?p??;Kr2WPkkG?g?g6PP_OyÆuu2-BM)&ssS".&%e%.&%e%]u\f¶¶¥ef¶¶¥ef¶¶¥ePP_OByIy9;Kr2TH]]DUIIE;Kr2PP_OFa=;Kr2PP_OO?p??VOJF?g?g6WPkkG;Kr2PP_O<W7W3;Kr2TH]]D?g?g6PP_O?g?g6O?p??PP_Ouuq?g?g6SGDCFa=þïâď¾O?p??\_[PP_OFa=Fa=?g?g6WPkkG;Kr2SGDCò»¶Ë²PP_OVOJFO?p??;Kr2PP_O=XX=4VOJFTH]]DUIIEPA@q@>f555CzzS:;Kr2PP_OQBQQA?g?g6SGDCTH]]DPA@q@O?p??;Kr2Fa=PP_O>f555?g?g6PP_Oa ai`eµedPP_OAx998VOJF;Kr2SGDC>f555CzzS:;Kr2TH]]D\_[PP_O>f555PA@q@O?p??>f555?g?g6PP_OTH]]D?g?g6SGDCò»¶Ë²PP_OSGDC?g?g6=XX=4CzzS:<W7W3CzzS:>f555PA@q@PP_OQBQQAPA@q@SGDCPP_O?g?g6Fa=PP_OAx998?g?g6O?p???g?g6SGDC;Kr2Fa=PP_OZZ{{JPP_OFa=VOJF?g?g6Ax998PA@q@PP_OTH]]D?g?g6SGDCò»¶Ë²PP_O?g?g6TH]]D=XX=4PA@q@Fa=UIIE;Kr2>f555PA@q@PP_OQBQQAPA@q@SGDCPP_O=XX=4VOJF;Kr2UIIESGDCPA@q@PP_OUIIE;Kr2O?p??RCCBVOJF?g?g6TH]]DPP_O.&%e%2-BM)]u\d´gsckgkg`_444++^]a]PP_Ox}tFa=PP_O=XX=4VOJF<W7W3PA@q@PP_OTH]]D?g?g6SGDCò»¶Ë²PP_OFa=Fa=?g?g6WPkkG;Kr2>f555PA@q@PP_O;Kr2Fa=PP_OFa=;Kr2<W7W3PA@q@SGDC;Kr2UIIEPA@q@SGDCCzzS:PA@q@PP_OQBQQA;Kr2SGDC;Kr2PP_OFa=;Kr2PP_OQBQQASGDCPA@q@>f555VOJF=XX=4=XX=4CzzS:ĄĕĕÅÄO?p??PP_O>f555?g?g6PP_O;Kr2SGDCN>GG>;Kr2TH]]DPP_O>f555?g?g6PP_O?g?g6O?p???g?g6SGDCAx998þïâď¾;Kr2^]a]PP_O»|{;Kr2PP_OO?p??;Kr2WPkkG?g?g6PP_O>f555?g?g6Fa=PP_O=XX=4PA@q@N>GG>;Kr2O?p??>f555;Kr2O?p??UIIE?g?g6PP_OUIIECzzS:?g?g6O?p???g?g6PP_OVOJFO?p??PP_O?g?g6TH]]D=XX=4VOJF>f555PA@q@PP_O>f555?g?g6PP_OCzzS:O?p??WPkkGCzzS:TH]]DCzzS:<W7W3CzzS:Fa=CzzS:>f555;Kr2>f555PP_OQBQQA?g?g6SGDCPA@q@PP_OTH]]D?g?g6SGDCò»¶Ë²PP_ON>GG>PA@q@O?p??CzzS:UIIEPA@q@SGDC?g?g6;Kr2>f555;Kr2PP_O;Kr2PP_OUIIESGDC;Kr2WPkkGúÞ¾»ºTH]]DPP_O>f555?g?g6PP_OFa=;Kr2PP_O@hhG7SGDC?g?g6=XX=4VOJF?g?g6O?p??=XX=4CzzS:;Kr2PP_Od´gscc¢¢bc¢¢b{w[dL[K^]a]PP_OÃ£r{w;Kr2CzzS:Fa=PP_O{wZZ{{J>f555SGDC;Kr2QTTQP'
mensaje_decodificado = decodificarMensaje(mensaje_codificado)
print("Mensaje 2:")
print(mensaje_decodificado)
print()
'''
