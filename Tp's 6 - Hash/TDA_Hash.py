from TDA_Lista import *


class TablaHash():

    def __init__(self, tamanio):
        tabla = []
        for i in range(0, tamanio):
            tabla.append(Lista())
