from TDA_Lista import *


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

tabla = crearTabla(28)


def hash(palabra):
    if len(palabra) > 0:
        inicial = palabra[0].capitalize()
        indice = ord(inicial) - 65

        return indice


def insertarPalabra(palabra, descripcion):
    indice = hash(palabra)
    inserCampo(tabla[indice], [palabra, descripcion], 0)


def busquedaPalabra(palabra):
    indice = hash(palabra)

    return busquedaListaCampo(tabla[indice], palabra, 0)


def eliminarPalabra(tabla, palabra):
    indice = hash(palabra)

    if busquedaListaCampo(tabla[indice], palabra, 0) is not None:
        eliminarCampo(tabla[indice], palabra, 0)


# A, B y C

# Insersión de palabras
insertarPalabra("Casa", "Descripcion de Casa")
insertarPalabra("Añejo", "Descripcion de Añejo.")

print("DICICONARIO COMPLETO:")
barridoHash(tabla)
print()

# Busqueda de palabras
print("BUSQUEDA:")

encontrado = busquedaPalabra("Añejo")
if encontrado is not None:
    print("Palabra encontrada: " + str(encontrado.info))
else:
    print("La palabra Añejo no se encontró")

encontrado = busquedaPalabra("Alan")
if encontrado is not None:
    print("Palabra encontrada: " + str(encontrado.info))
else:
    print("La palabra Alan no se encontró")

print()

# Eliminación de palabras
print("Luego de intentar eliminar Añejo y Palo del diccionario:")
eliminarPalabra(tabla, "Añejo")
eliminarPalabra(tabla, "Palo")
print("DICCIONARIO ACTUALIZADO:")
barridoHash(tabla)
