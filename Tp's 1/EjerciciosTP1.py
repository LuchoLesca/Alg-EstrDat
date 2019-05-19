from Funciones import fibonacci, suma, producto, potencia, invertir_str, serie
from Funciones import ent_bin, logaritmo, cant_dig, invertir_num
from Funciones import euclidesmcd, euclidesmcm, suma_dig, raiz, recorrermat
from Funciones import bbin_R, laber, moverTorre, quicksort, mergesort, sucesion

"""
# EJERCICIO 1

x = int(input('Ingrese un numero: '))
print('La secuencia de fibonacci es: ' + str(fibonacci(x)))


# EJERCICIO 2

numero = int(input('Ingrese un numero positivo: '))
print(str(suma(numero)))


# EJERCICIO 3

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
print('el producto es: ' + str(producto(n1, n2)))


# EJERCICIO 4

base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))
print('El resultado es: ' + str(potencia(base, exponente)))


# EJERCICIO 5

pal = input('ingrese una palabra: ')
print('Palabra invertida: ' + invertir_str(pal))


# EJERCICIO 6

numero = int(input('Ingrese un numero: '))
print('La sumatoria es: ' + str(serie(numero)))


# EJERCICIO 7

numero = 20
print('El numero ' + str(numero) + ' en binario es: ' + ent_bin(numero))


# EJERCICIO 8
n = 32
b = 2
print('El logaritmo de ' + str(n) + ' en base ' + str(b) + ' es: ' + str(logaritmo(n, b)))


# EJERCICIO 9

numero = 999
print('La cantidad de dígitos de ' + str(numero) + ' número es: ' + str(cant_dig(numero)))


# EJERCICIO 10

print(invertir_num(123))


# EJERCICIO 11

a = 500
b = 120

print(euclidesmcd(500, 120))


# EJERCICIO 12

print('MCD(' + str(a) + ', ' + str(b) + '): ' + str(euclidesmcd(1000, 625)))
print('mcm(' + str(a) + ', ' + str(b) + '): ' + str(euclidesmcm(1000, 625)))


# EJERCICIO 13

print('La suma de los digitos del numero es: ' + str(suma_dig(341)))


# EJERCICIO 14

print('La raiz cuadrada de ' + str(num) + ' es ' + str(raiz(0, 7)))


# EJERCICIO 15

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
recorrermat(matriz, 2, 3)


# EJERCICIO 16 (Orden Quicksort)

lista = [6, 45, 2, 11, 1]
quicksort(lista, 0, len(lista) - 1)
for elemento in lista:
    print(str(elemento))


# EJERCICIO 17

lista = [1, 10, 15, 22, 47, 55]
primero = lista[0]
ultimo = len(lista)
pos = bbin_R(lista, primero, ultimo, 55)

if pos == -1:
    print('Buscado no se encuentra en la lista')
else:
    print('Buscado está en la posición ' + str(pos) + ' de la lista')


# EJERCICIO 18 (Laberinto)

laberinto = [[1, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 1, 0, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 0, 1, 0, 0, 0, 0],
             [0, 1, 0, 1, 1, 1, 0, 0],
             [0, 0, 0, 1, 0, 1, 1, 0],
             [0, 2, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

camino = []
laber(laberinto, 0, 0, camino)


# EJERCICIO 19 (Torre de Hanoi)

moverTorre(3, 'Torre 1', 'Torre 2', 'Torre 3')


# EJERCICIO 20

print(sucesion(5))
"""
