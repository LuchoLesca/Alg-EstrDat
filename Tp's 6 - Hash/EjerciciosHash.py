from TDA_Lista import *
from random import choice, randint


def crearTabla(tamanio):
    '''Crea un tabla hash del tamanio ingresado'''
    tabla = []
    for i in range(0, tamanio):
        tabla.append(Lista())
    return tabla


def barridoHash(tabla):
    '''Realiza un barrido total de la tabla con su contenido'''
    for lista in tabla:
        if lista.tamanio != 0:
            barridoLista(lista)


# EJERCICIO 1
"""
tabla = crearTabla(28)


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
barridoHash(tabla)
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
barridoHash(tabla)
"""


# EJERCICIO 2
"""
tabla = crearTabla(97)

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
