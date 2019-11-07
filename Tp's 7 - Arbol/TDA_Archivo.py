import shelve
# El indice de estos archivos no es numérico, es string. Hay que transformar de
# string a int


def abrir(ruta):
    return shelve.open(ruta)


def cerrar(archivo):
    archivo.close()


def leer(archivo, pos):
    try:
        return archivo[str(pos)]
    except Exception:
        raise None


def guardar(archivo, dato):
    try:
        archivo[str(len(archivo))] = dato
        return True
    except Exception:
        raise None


def modificar(archivo, dato, pos):
    try:
        archivo[str(pos)] = dato
        return True
    except Exception:
        raise None


def barridoArchivo(archivo):
    pos = 0
    while pos < len(archivo):
        print(leer(archivo, pos))
        pos += 1
