from TDA_Arbol import *
from random import randint

r = None


# EJERCICIO 1

# A
lista_numeros = []
"""
for i in range(randint(5, 10)):
    num = randint(0, 50)
    lista_numeros.append(num)
    r = insertar(r, num)
"""
# print("Lista de números ingresados", lista_numeros)
# 20, 29, 11, 41, 32, 72, 99, 50, 65, 91
r = insertar(r, 20)
r = insertar(r, 29)
r = insertar(r, 11)
r = insertar(r, 41)
r = insertar(r, 32)
r = insertar(r, 72)
r = insertar(r, 99)
r = insertar(r, 50)
r = insertar(r, 65)
r = insertar(r, 91)


"""
print()
print("Preorden")
preorden(r)
print()

print("Inorden")
inorden(r)
print()

print("Postorden")
postorden(r)
print()


imprimirArbol(r)
"""
# B
"""
buscado = lista_numeros[0]
# buscado = 100

resultado = busqueda(r, buscado)

if resultado is None:
    print("El elemento " + str(buscado) + " no está en el arbol")
else:
    print("El elemento " + str(buscado) + " se encuentra en el arbol")
"""
# C
"""
print()
print("ELiminados: ")
for i in range(3):
    num = lista_numeros[i]
    eliminar(r, num)
    print(lista_numeros[i])

print()
print("Arbol inorden")
inorden(r)
"""

# D
"""
print("Altura de sub arbol izquierdo: ", altura(r.izq))
print("Altura de sub arbol derecho: ", altura(r.der))
"""

# E
"""
r = insertar(r, 20)
r = insertar(r, 29)
r = insertar(r, 11)

imprimirArbol(r)


def repetido(raiz):
    if raiz is not None:
        if busqueda(raiz.izq, raiz.info) is not None:
            print("Se repite", raiz.info)
        if busqueda(raiz.der, raiz.info) is not None:
            print("Se repite:", raiz.info)
        repetido(raiz.izq)
        repetido(raiz.der)


print()
repetido(r)
"""

# F   <<<<< Falta terminar
# HAY QUE HACER UNA FUNCION QUE PUEDA DEVOLVER LOS DOS AL MISMO TIEMPO
# Y NO DE A UNO A LA VEZ
"""
imprimirArbol(r)

pares, impares = 0, 0


def pares(raiz):
    if raiz is not None:
        if raiz.info % 2 == 0:
            return (1 + pares(raiz.izq) + pares(raiz.der))
        else:
            return (0 + pares(raiz.izq) + pares(raiz.der))
    else:
        return 0


def impares(raiz):
    if raiz is not None:
        if raiz.info % 2 == 0:
            return (0 + impares(raiz.izq) + impares(raiz.der))
        else:
            return (1 + impares(raiz.izq) + impares(raiz.der))
    else:
        return 0


print(pares(r))
print(impares(r))
"""


# EJERCICIO 2  <<<<< Falta hacer que relice la operación

# A


print("Expresión original: ((2 + 3) * 4) + 26")

r = Nodoarbol("+")
r.der = Nodoarbol(26)
r.izq = Nodoarbol("*")
r.izq.der = Nodoarbol(4)
r.izq.izq = Nodoarbol("+")
r.izq.izq.izq = Nodoarbol(2)
r.izq.izq.der = Nodoarbol(3)

print()
print("En forma de prefijo:")
preorden(r)
print()
print("En orden pero sin paréntesis")
inorden(r)
print()
print("En orden de postfijo")
postorden(r)

imprimirArbol(r)
