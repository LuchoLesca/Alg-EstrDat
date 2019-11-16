import shelve


def abrir_lectura(ruta):
    return shelve.open(ruta, "r")


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
