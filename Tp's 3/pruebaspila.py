from TDA_Pila_Nodo import Pila, cargaAutoInt, cargaAutoStr, apilar, desapilar, cima
from TDA_Pila_Nodo import pila_llena, pila_vacia, tamanio, barrido, invertir, randString
from TDA_Pila_Nodo import stringToPila, ordenPilaCrec, ordenPilaDecr, factorialPila, fibonacciPila
from TDA_Pila_Nodo import quicksortPila, listaRandom, comprobarOrdenAsc
import random
import string

p = Pila()
p1 = Pila()
p2 = Pila()
p3 = Pila()
p4 = Pila()
cant = 10


# Ej1
"""cargaAutoInt(p, cant)
barrido(p)

num = 1
cont = 0

p1 = Pila()
while not pila_vacia(p):
    dato = desapilar(p)
    if (dato == num):
        cont += 1
    apilar(p1, dato)

print('El numero ' + str(num) + ' se encuentra ' + str(cont) +
      ' veces en la lista')
"""


# Ej2
"""cargaAutoInt(p, cant)
print("Todos:")
barrido(p)
while not pila_vacia(p):
    dato = desapilar(p)
    if (dato % 2 == 0):
        apilar(p1, dato)
p = invertir(p1)
print('Solo pares:')
barrido(p)
"""

# Ej3
"""num = 3
reemplazo = 100
cargaAutoInt(p, cant)
print("Pila:")
barrido(p)

while not pila_vacia(p):
    dato = desapilar(p)
    if dato == num:
        dato = reemplazo
    apilar(p1, dato)
p = invertir(p1)

print("Pila con el numero " + str(num) + " reemplazado por el " + str(reemplazo))
barrido(p)
"""


# Ej4
"""cargaAutoInt(p, cant)
barrido(p)
p = invertir(p)
print("Pila anterior invertida:")
barrido(p)
"""


# Ej5
"""palindr = True
palabra = 'Noi'
# palabra = 'non'
# palabra = randString(5)
for elemento in palabra:
    apilar(p, elemento)

while not pila_vacia(p):
    dato = desapilar(p)
    apilar(p1, dato)
    apilar(p2, dato)

p = invertir(p2)

while not pila_vacia(p):
    dato1 = desapilar(p)
    dato2 = desapilar(p1)
    if dato1 != dato2:
        palindr = False
    apilar(p2, dato2)

if palindr:
    print('Palindromo')
else:
    print('No palindromo')
"""


# Ej6
"""palabra = randString(5)
p = stringToPila(palabra)

print('Pila normal:')
barrido(p)

p1 = invertir(p)
print('Pila invertida')
barrido(p1)
"""


# Ej7
"""cargaAutoInt(p, cant)
i = 3
print('Pila:')
barrido(p)

if (i <= tamanio(p)):
    while not pila_vacia(p):
        aux = desapilar(p)
        if i != tamanio(p):
            apilar(p1, aux)

    p = invertir(p1)
    print('Pila anterior con elemento de la posicion ' + str(i) + ' eliminado')
    barrido(p)
else:
    print("El numero ingresado excede el limite de la pila")
"""


# Ej8
"""palos = ['Oro', 'Basto', 'Copa', 'Espada']
for i in range(0, cant):
    num = random.randint(1, 13)
    palo = random.choice(palos)
    apilar(p, [num, palo])

while not pila_vacia(p):
    carta = desapilar(p)
    if carta[1] == 'Oro':
        apilar(p1, carta)
    elif carta[1] == 'Basto':
        apilar(p2, carta)
    elif carta[1] == 'Copa':
        apilar(p3, carta)
    elif carta[1] == 'Espada':
        apilar(p4, carta)

print('Oro:')
barrido(p1)
print('Basto:')
barrido(p2)
print('Copa:')
barrido(p3)
print('Espada:')
barrido(p4)

p1 = ordenPilaCrec(p1)
print('Oro ordenado crecientemente:')
barrido(p1)
"""


# Ej9  FACTORIAL

#print(str(factorialPila(5)))


# Ej10
"""cargaAutoInt(p, cant)
barrido(p)
while not pila_vacia(p):
    dato = desapilar(p)
    if dato % 2 == 0:
        apilar(p1, dato)
    else:
        apilar(p2, dato)
print('Pila par:')
barrido(p1)
print('Pila impar:')
barrido(p2)
"""


# Ej11
"""vocales = 'aeiouAEIOU'
palabra = 'Algoritmos'
cont = 0
p = stringToPila(palabra)

while not pila_vacia(p):
    dato = desapilar(p)
    if dato in vocales:
        cont += 1
    apilar(p1, dato)
print('Hay ' + str(cont) + ' vocales')

p = invertir(p1)
barrido(p)
"""


# Ej12
"""num = int(input('ingrese numero distinto de cero: '))
while (num != 0):
    if not pila_llena(p):
        while not pila_vacia(p) and (cima(p) >= num):
            apilar(p1, desapilar(p))
        apilar(p, num)
        while not pila_vacia(p1):
            apilar(p, desapilar(p1))
    else:
        print('Pila llena, no se puede agregar numero')
    barrido(p)
    num = int(input('Ingrese un numero distinto de cero: '))
"""


# Ej13  QUICKSORT
"""
# Probar ordenar z cantidad de listas distintas
z = 100
cant_orden = 0
no_orden = []

for k in range(0, z):
    lista = listaRandom(14)

    quicksortPila(lista, 0, len(lista) - 1)
    print(lista)
    ordenado = comprobarOrdenAsc(lista)
    if ordenado:
        cant_orden += 1

print("Se ordenaron correctamente: " + str(cant_orden) + " de " + str(z))

# Probar ordenar una única lista

lista = listaRandom(25)
quicksortPila(lista, 0, len(lista) - 1)
print(lista)
"""


# Ej14
"""numeros = '0123456789'
parrafo = 'Habia 3 casas, pero a una la destruyeron. Oh, rayos!'  # 52
vocales = 'aeiouAEIOU'
consonantes = 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'

for elemento in parrafo:
    if (elemento in vocales):  # 18
        apilar(p1, elemento)
    elif (elemento in consonantes):  # 20
        apilar(p2, elemento)
    else:  # 14
        apilar(p3, elemento)
"""
# Punto A
"""print('Cantidad de vocales: ' + str(tamanio(p1)))
print('Cantiad de consonantes: ' + str(tamanio(p2)))
print('Cantidad de otros caracteres: ' + str(tamanio(p3)))"""

# Punto B y D
"""cont_num = 0
cont_espacios = 0
while not pila_vacia(p3):
    dato = desapilar(p3)
    if (dato == ' '):
        cont_espacios += 1
    elif (dato in numeros):
        cont_num += 1
    apilar(p, dato)
p3 = invertir(p)

print('Cantidad de espacios en blanco: ' + str(cont_espacios))
print('Cantidad de numeros: ' + str(cont_num))"""

# Punto C
"""cont_total = tamanio(p1) + tamanio(p2) + tamanio(p3)
print("Porcentaje de vocales: " + str((tamanio(p1) * 100) / cont_total))
print("Porcentaje de consonantes: " + str((tamanio(p2) * 100) / cont_total))"""


# Punto E
"""if tamanio(p1) == tamanio(p3):
    print("Igual cantidad")
else:
    print("Cantidades distintas")"""

# Punto F
"""hayZ = False
while not pila_vacia(p2) and not hayZ:
    dato = desapilar(p2)
    if dato == 'z':
        hayZ = True
    apilar(p, dato)

while not pila_vacia(p):
    apilar(p2, desapilar(p))

if hayZ:
    print('Hay por lo menos una letra z')
else:
    print('No hay letra z')
"""

# Ejercicio 15
"""objetos = ['monitor', 'teclado', 'silla', 'lampara', 'pisapapeles', 'basurero',
           'cinta adhesiva', 'carpetas', 'grapadora']
for i in range(0, cant):
    peso = random.randint(1, 21)
    objeto = random.choice(objetos)
    apilar(p, [peso, objeto])

print('Pila desordenada:')
barrido(p)
p = ordenPilaCrec(p)
print('Pila ordenada:')
barrido(p)
"""

# Ej16
"""
def dirToNum(direccion):
    '''Convierte la dirección ingresada en un número del 1 al 9, según corresponda'''
    num = 0
    if (direccion == "norte"):
        num = 8
    elif (direccion == "sur"):
        num = 2
    elif (direccion == "oeste"):
        num = 4
    elif (direccion == "este"):
        num = 6
    elif (direccion == "noreste"):
        num = 9
    elif (direccion == "noroeste"):
        num = 7
    elif (direccion == "sureste"):
        num = 3
    elif (direccion == "suroeste"):
        num = 1
    return num


def NumToDir(numero):
    '''Convierte el número posicional en la dirección correspondiente'''
    dir = ""
    if (numero == 1):
        dir = "suroeste"
    elif (numero == 2):
        dir = "sur"
    elif (numero == 3):
        dir = "sureste"
    elif (numero == 4):
        dir = "oeste"
    elif (numero == 6):
        dir = "este"
    elif (numero == 7):
        dir = "noroeste"
    elif (numero == 8):
        dir = "norte"
    elif (numero == 9):
        dir = "noreste"
    return dir


movimientos = ['norte', 'sur', 'este', 'oeste', 'noreste', 'sureste',
               'noroeste', 'suroeste']
lista_movs = []
lista_movs_rev = []

for i in range(0, cant):
    mov = random.choice(movimientos)
    lista_movs.append(mov)
    apilar(p, dirToNum(mov))

while not pila_vacia(p):
    num = 10 - desapilar(p)
    lista_movs_rev.append(NumToDir(num))

print("Movimientos realizados por el robot: ")
print(lista_movs)

print("Movimientos inversos, para volver a punto de partida: ")
print(lista_movs_rev)
"""


# Ej17  FIBONACCI
"""
numero = 7
fibonacciPila(numero)
"""

# Ej18
"""tMedia = 0
cant_mayores = 0
cant_menores = 0

cargaAutoInt(p, cant)

tMayor = cima(p)
tMenor = cima(p)

while not pila_vacia(p):
    dato = desapilar(p)
    tMedia += dato
    if dato < tMenor:
        tMenor = dato
    if dato > tMayor:
        tMayor = dato
    apilar(p1, dato)

print('Temp Menor: ' + str(tMenor))
print('Temp Mayor: ' + str(tMayor))
tMedia = round(tMedia / tamanio(p1))
print('Temp Media: ' + str(tMedia))

while not pila_vacia(p1):
    dato = desapilar(p1)
    if dato >= tMedia:
        cant_mayores += 1
    else:
        cant_menores += 1
    apilar(p, dato)

print('Temperaturas:')
barrido(p)

print('Cant temperaturas mayores e iguales a la media: ' + str(cant_mayores))
print('Cant temperaturas menores a la media: ' + str(cant_menores))
"""


# Ej19
"""cargaAutoStr(p, cant)
print("Pila completa")
barrido(p)
print("Solo los elementos con un largo mayor a 7")

while not pila_vacia(p):
    dato = desapilar(p)
    if len(dato) > 7:
        print(dato)
    apilar(p1, dato)
p = invertir(p1)
"""


# Ej20
"""cargaAutoInt(p, cant)
barrido(p)
while not pila_vacia(p):
    dato = desapilar(p)
    if (dato % 2 == 0) or (dato % 3 == 0) or (dato % 5 == 0):
        apilar(p1, dato)

p1 = invertir(p1)
print('Pila filtrada:')
barrido(p1)
"""
