import shelve
from os import remove


def abrir(ruta):
    return shelve.open(ruta)


def cerrar(archivo):
    archivo.close()


def leer(archivo, pos):
    try:
        return archivo[str(pos)]
    except Exception:
        return None

def guardar(archivo, dato):
    try:
        archivo[str(len(archivo))] = dato
    except Exception:
        raise None


def modificar(archivo, dato, pos):
    try:
        archivo[str(pos)] = dato
        return True
    except Exception:
        raise None


def barridoArchivo(archivo):
    '''Imprime el dato de cada posición'''
    pos = 0
    while pos < len(archivo):
        print(leer(archivo, pos))
        pos += 1


def fileToArray(ruta):
    '''Devuelve array de elementos'''
    archivo = abrir(ruta)
    array = []
    pos = 0
    while pos < len(archivo):
        array.append(leer(archivo, pos))
        pos += 1

    return array


def txtToDat(rutatxt="", rutadat=""):
    '''Crea archivo.dat a partir de .txt'''
    # Abrir archivo dir
    archivodat = abrir(rutadat)
    # Abre archivo txt
    archivotxt = open(rutatxt, "r")

    for linea in archivotxt:
        if len(linea) > 1:
            guardar(archivodat, linea)


def limpiar(archivo):
    try:
        archivo.clear()
        return True
    except Exception:
        raise None
