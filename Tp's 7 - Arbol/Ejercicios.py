from TDA_Arbol import *
from random import randint


r = None
"""
lista_numeros = []

for i in range(randint(5, 10)):
    num = randint(0, 50)
    lista_numeros.append(num)
    r = insertar(r, num)

print("Lista de números ingresados", lista_numeros)

print()
preorden(r)
print()
inorden(r)
print()
postorden(r)

print()
print("Cantidad de nodos", str(cantidadNodos(r)))
print("Cantidad de hojas", str(cantidadHojas(r)))
nivel = 3
print("Cantidad de nodos en nivel " + str(nivel), nodosEnNivel(r, nivel))
"""

# EJERCICIO 2  <<<<< Falta hacer que relice la operación

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

print()
print(operar(r))
