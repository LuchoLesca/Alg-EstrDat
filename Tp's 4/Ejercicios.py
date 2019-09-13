from TDA_Cola_Nodo import Cola, arribo, atencion, barridoC, cargaAutoIntC
from TDA_Cola_Nodo import cargaAutoStrC, cola_llena, cola_vacia, moverAFinal
from TDA_Cola_Nodo import tamanio, primo, fibonacci, en_frente

from TDA_Pila_Nodo import Pila, apilar, desapilar, pila_llena, pila_vacia
from TDA_Pila_Nodo import barrido, cargaAutoInt, cargaAutoStr

import random
import time


cant = 10
p = Pila()
c = Cola()
c1 = Cola()
c2 = Cola()
c3 = Cola()


# Ejercicio 1
"""
vocales = "aeiouAEIOU"

cargaAutoStrC(c, cant)
print("Con vocales: ")
barrido(c)

for i in range(0, tamanio(c)):
    dato = atencion(c)
    if dato not in vocales:
        arribo(c, dato)

print("Sin vocales: ")
barrido(c)
"""


# Ejercicio 2
"""
cargaAutoIntC(c, cant)
print("Cola normal: ")
barrido(c)

while not cola_vacia(c):
    apilar(p, atencion(c))

while not pila_vacia(p):
    arribo(c, desapilar(p))

print("Cola invertida: ")
barrido(c)
"""


# Ejercicio 3
"""
palabra = "Noi"
palabra = "NoN"

for letra in palabra:
    apilar(p, letra)
    arribo(c, letra)

palin = True
for i in range(0, c.tamanio):
    dato = atencion(c)
    if (dato != desapilar(p)):
        palin = False
    arribo(c, dato)

if palin:
    print("Palindromo")
else:
    print("No palindromo")
"""


# Ejercicio 4
"""
cargaAutoIntC(c, cant)

print("Cola original:")
barrido(c)

while not cola_vacia(c):
    num = atencion(c)
    if primo(num):
        arribo(c1, num)

print("Cola de primos:")
barrido(c1)
"""


# Ejercicio 5
"""
cargaAutoInt(p, cant)

print("Pila oiriginal:")
barrido(p)

while not pila_vacia(p):
    arribo(c, desapilar(p))

while not cola_vacia(c):
    apilar(p, atencion(c))

print("------")
print("Pila invertida:")
barrido(p)
"""


# Ejercicio 6
"""
cargaAutoIntC(c, cant)
num = 7
cont = 0

barridoC(c)

for i in range(0, tamanio(c)):
    aux = atencion(c)
    if (aux == num):
        cont += 1
    arribo(c, aux)

print("El numero " + str(num) + " se encuentra " + str(cont) + " veces ")
"""


# Ejercicio 7
"""
indice = 2

cargaAutoIntC(c, cant)
print("Cola original:")
barridoC(c)

if (tamanio(c) > indice):
    for i in range(0, tamanio(c)):
        aux = atencion(c)
        if (i != indice):
            arribo(c, aux)

print("Cola con elemento " + str(indice) + " eliminado")
barridoC(c)
"""


# Ejercicio 8
"""
nuevo = int(input("Ingrese numero a agregar distintos de cero: "))

while (nuevo != 0):
    while (not cola_vacia(c)) and (c.frente.info < nuevo):
        arribo(c1, atencion(c))

    arribo(c1, nuevo)

    while (not cola_vacia(c)):
        arribo(c1, atencion(c))

    c, c1 = c1, c

    barridoC(c)

    nuevo = int(input("Ingrese numero a agregar distintos de cero: "))
"""


# Ejercicio 9
"""
cargaAutoIntC(c, cant)
print("Cola:")
barridoC(c)


min = c.frente.info
max = c.frente.info
cont = 0

while not cola_vacia(c):
    dato = atencion(c)
    if dato > max:
        max = dato
    if dato < min:
        min = dato
    if dato < 0:
        cont += 1
    arribo(c1, dato)

c, c1 = c1, c

print("Cola terminado:")
barridoC(c)

print("Rango: " + str(max - min))
print("Cantidad de numeros negativos: " + str(cont))
"""


# Ejercicio 10 (Fibonacci)
"""
# Prueba uno
# fibonacci(5)

# Prueba varios ciclos
for i in range(0, 7):
    print("Indice: " + str(i))
    fibonacci(i)
"""


# Ejercicio 11
"""
for i in range(1, cant + 1):
    arribo(c1, (i*2))

for i in range(1, cant + 1):
    arribo(c2, (i*3))
'''
print("C1:")
barridoC(c1)
print("C2:")
barridoC(c2)
'''

while (not cola_vacia(c1)) and (not cola_vacia(c2)):
    if (c1.frente.info) < (c2.frente.info):
        arribo(c, atencion(c1))
    else:
        arribo(c, atencion(c2))

if tamanio(c1) > 0:
    while not cola_vacia(c1):
        arribo(c, atencion(c1))
elif tamanio(c2) > 0:
    while not cola_vacia(c2):
        arribo(c, atencion(c2))

barridoC(c)
"""


# Ejercicio 12
"""
digitos = "0123456789"
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, cant):
    for i in range(0, 20):
        opcion = (random.randint(0, 1))

    if (opcion == 0):
        arribo(c, random.choice(digitos))
    else:
        arribo(c, random.choice(caracteres))

print("Cola original:")
barridoC(c)

while not cola_vacia(c):
    dato = atencion(c)
    if dato in digitos:
        arribo(c1, dato)
    else:
        arribo(c2, dato)

print("Cola de dígitos:")
barridoC(c1)
print("Cola de caracteres:")
barridoC(c2)

print("Cantidad de caracteres en la cola: " + str(tamanio(c2)))
"""


# Ejercicio 13  <---


# Ejercicio 14
"""
cargaAutoIntC(c1, cant)
cargaAutoIntC(c2, cant)
"""

# Se creo una copia (c2) de c1
"""for i in range(0, tamanio(c1)):
    dato = atencion(c1)
    arribo(c1, dato)
    arribo(c2, dato)
"""

# A
"""if (tamanio(c1) == tamanio(c2)):
    print("Tienen la misma cantidad de elementos")
else:
    print("No tienen la misma cantidad de elementos")
"""

# B
"""
if tamanio(c1) == tamanio(c2):

    iguales = True
    i = 1

    while (iguales) and (i <= tamanio(c1)):
        dato1 = atencion(c1)
        dato2 = atencion(c2)

        if dato1 != dato2:
            iguales = False

        i += 1

    if iguales:
        print("Son iguales")
    else:
        print("No son iguales")

else:
    print("El tamaño es distinto, por lo tanto no son iguales")
"""

# C
"""
suma_c1 = 0
suma_c2 = 0

for i in range(0, tamanio(c1)):
    dato = atencion(c1)
    suma_c1 += dato
    arribo(c1, dato)

for i in range(0, tamanio(c2)):
    dato = atencion(c2)
    suma_c2 += dato
    arribo(c2, dato)

if suma_c1 == suma_c2:
    print("Son iguales")
else:
    if suma_c1 > suma_c2:
        print("C1 es mayor")
    else:
        print("C2 es mayor")
"""

# D
"""
cprimos_c1 = 0
cprimos_c2 = 0

for i in range(0, tamanio(c1)):
    dato = atencion(c1)
    if primo(dato):
        cprimos_c1 += 1
    arribo(c1, dato)

for i in range(0, tamanio(c2)):
    dato = atencion(c2)
    if primo(dato):
        cprimos_c2 += 1
    arribo(c2, dato)

if cprimos_c1 == cprimos_c2:
    print("Igual cantidad de numeros primos en elementos")
else:
    if cprimos_c1 > cprimos_c2:
        print("Mas numeros primos en c1")
    else:
        print("Mas numeros primos en c2")
"""

# E
"""
hay_mult_dos = False
hay_mult_tres = False
hay1 = False
hay2 = False

for i in range(0, tamanio(c1)):
    dato = atencion(c1)
    if (dato % 3 == 0):
        hay_mult_tres = True
    if (dato % 2 == 0):
        hay_mult_tres = True
    arribo(c1, dato)

if (hay_mult_dos) and (hay_mult_tres):
    hay1 = True

for i in range(0, tamanio(c2)):
    dato = atencion(c2)
    if (dato % 3 == 0):
        hay_mult_tres = True
    if (dato % 2 == 0):
        hay_mult_tres = True
    arribo(c2, dato)

if (hay_mult_dos) and (hay_mult_tres):
    hay2 = True

if hay1 and hay2:
    print("Ambas colas poseen al menos un número múltiplo de dos y un número múltiplo de tres")
else:
    print("Ambas colas no poseen al menos un número múltiplo de dos y un número múltiplo de tres")
"""

# Ejercicio 15  <---


# Ejercicio 16
"""
for i in range(1, 6):
    arribo(c, [i, random.uniform(1, 10)])

barridoC(c)
"""
# A
"""
for i in range(1, 6):
    proceso = atencion(c)
    print(proceso)
    time.sleep(proceso[1])
"""

# B
"""
i = 0
while not cola_vacia(c):

    i += 1
    print("Ciclo " + str(i))

    proceso = atencion(c)
    if proceso[1] <= 4.5:
        time.sleep(proceso[1])
    else:
        time.sleep(4.5)

    proceso[1] -= 4.5

    if (proceso[1] > 0):
        arribo(c, proceso)

    barridoC(c)
"""

# C
"""
i = 0
while not cola_vacia(c):

    i += 1
    print("Ciclo " + str(i))

    proceso = atencion(c)
    if proceso[1] <= 4.5:
        time.sleep(proceso[1])
    else:
        time.sleep(4.5)

    proceso[1] -= 4.5

    if (proceso[1] > 0):
        arribo(c, proceso)

    agregar = random.choice([True, False])  # Decide si se agrega nuevo proceso
    if agregar:                             # o no, y lo carga aleatorio
        arribo(c, [7, random.uniform(1, 10)])

    barridoC(c)
"""

# Ejercicio 17
"""
# A
letras = "ABCDEF"

for i in range(0, cant):
    turno = str(random.choice(letras))
    for j in range(0, 3):
        turno += str(random.randint(0, 9))
    arribo(c, turno)

print("Cola original:")
barridoC(c)


# B

while not cola_vacia(c):
    turno = atencion(c)
    if turno[0] in ["A", "C", "F"]:
        arribo(c1, turno)
    else:
        arribo(c2, turno)

print("C1 -------------")
barridoC(c1)
print("C2 -------------")
barridoC(c2)
print("")

# C

contA, contB, contC, contD, contE, contF = 0, 0, 0, 0, 0, 0

if tamanio(c1) == tamanio(c2):
    print("El tamaño de ambas colas es igual")
else:
    if tamanio(c1) > tamanio(c2):
        print("C1 tiene más cantidad de turnos")

        for i in range(0, tamanio(c1)):
            turno = atencion(c1)
            if turno[0] == "A":
                contA += 1
            elif turno[0] == "C":
                contC += 1
            else:
                contF += 1
            arribo(c1, turno)

        mayor = "A"
        cant_mayor = contA
        if cant_mayor < contC:
            mayor = "C"
            cant_mayor = contC
        if cant_mayor < contF:
            mayor = "F"
            cant_mayor = contF
        print("Aparece mas veces la letra: " + mayor + " con " +
              str(cant_mayor) + " ocurrencias")

    else:
        print("C2 tiene más cantidad de turnos")

        for i in range(0, tamanio(c2)):
            turno = atencion(c2)
            if turno[0] == "B":
                contB += 1
            elif turno[0] == "D":
                contD += 1
            else:
                contE += 1
            arribo(c2, turno)

        mayor = "B"
        cant_mayor = contB
        if cant_mayor < contD:
            mayor = "D"
            cant_mayor = contD
        if cant_mayor < contE:
            mayor = "E"
            cant_mayor = contE
        print("Aparece mas veces la letra: " + mayor + " con " +
              str(cant_mayor) + " ocurrencias")
"""

# Ejercicio 18  <---


# Ejercicio 19
"""
palabra_in = "Parasito"
# palabra_in = "Parasitos"

if len(palabra_in) % 2 == 0:
    for i in range(0, len(palabra_in), 2):
        byte = palabra_in[i] + palabra_in[i + 1]
        arribo(c, byte)
else:
    for i in range(0, len(palabra_in) - 1, 2):
        byte = palabra_in[i] + palabra_in[i + 1]
        arribo(c, byte)
    arribo(c, palabra_in[len(palabra_in) - 1])

barridoC(c)

# B

cola_buff_in = Cola()

while not cola_vacia(c):
    arribo(cola_buff_in, atencion(c))

# barridoC(cola_buff_in)

# C
palabra_out = ""

while not cola_vacia(cola_buff_in):
    palabra_out += atencion(cola_buff_in)

print(palabra_out)
"""

# Ejercicio 20
"""
cant_c1, cant_c2, cant_c3 = 0, 0, 0

for i in range(0, 8):
    cabina = random.randint(1, 3)
    if cabina == 1:
        arribo(c1, True)
    elif cabina == 2:
        arribo(c2, True)
    else:
        arribo(c3, True)
'''
print("Cabina 1:")
barridoC(c1)
print("Cabina 2:")
barridoC(c2)
print("Cabina 3:")
barridoC(c3)
'''
while (not cola_vacia(c1)) or (not cola_vacia(c2)) or (not cola_vacia(c3)):
    if not cola_vacia(c1):
        atencion(c1)
        cant_c1 += 1
    if not cola_vacia(c2):
        atencion(c2)
        cant_c2 += 1
    if not cola_vacia(c3):
        atencion(c3)
        cant_c3 += 1

cant_mayor = cant_c1
cab_mayor = 1

if cant_mayor < cant_c2:
    cant_mayor = cant_c2
    cab_mayor = 2
if cant_mayor < cant_c3:
    cant_mayor = cant_c3
    cab_mayor = 3

print("Cabina que más dinero recaudó: " + str(cab_mayor))
"""

# Ejercicio 21 
"""

def insertar_vuelo_despegues(nuevo, cola):
    '''Devuelve la cola con el elemento nuevo cargado'''
    hora = nuevo[1]

    aux = Cola()

    while (not cola_vacia(cola)) and (cola.frente.info[1] < hora):
        arribo(aux, atencion(cola))

    arribo(aux, nuevo)

    while not cola_vacia(cola):
        arribo(aux, atencion(cola))

    return aux


def insertar_vuelo_aterrizajes(nuevo, cola):
    '''Devuelve la cola con el elemento nuevo cargado'''
    hora = nuevo[2]

    aux = Cola()

    while (not cola_vacia(cola)) and (cola.frente.info[2] < hora):
        arribo(aux, atencion(cola))

    arribo(aux, nuevo)

    while not cola_vacia(cola):
        arribo(aux, atencion(cola))

    return aux


def obtener_hora():
    return time.strftime("%S")


def crear_vuelo():  # Para usos practicos, los horarios seran segundos
    empresa = random.choice(empresas)
    hora_salida = random.randint(0, 59)
    hora_llegada = random.randint(0, 59)
    origen = random.choice(aero_ori)
    destino = random.choice(aero_des)
    tipo = random.choice(tipos_aviones)

    return [empresa, hora_salida, hora_llegada, origen, destino, tipo]


# Tiempos
# Aviones       aterrizaje         despegue
# pasajeros     10                  5
# negocios      5                   3
# carga         7                   9


# INDICES: empresa = 0, hora_s = 1, hora_l = 2
#          origen = 3, destino = 4, tipo = 5


despegues = Cola()
aterrizajes = Cola()
aux = Cola()

empresas = ["Empr_a", "Empr_b", "Empr_c", "Empr_d", "Empr_e"]
aero_ori = ["Ori_a", "Ori_b", "Ori_c", "Ori_d", "Ori_e"]
aero_des = ["Des_a", "Des_b", "Des_c", "Des_d", "Des_e"]
tipos_aviones = ["pasajeros", "negocios", "carga"]


# Genera cola de despegues y aterrizajes iniciales
for i in range(0, 2):
    vuelo_nuevo = crear_vuelo()
    despegues = insertar_vuelo_despegues(vuelo_nuevo, despegues)
    vuelo_nuevo = crear_vuelo()
    aterrizajes = insertar_vuelo_aterrizajes(vuelo_nuevo, aterrizajes)


def reprogramarVuelo(vuelo, despegues):
    '''Reprograma el vuelo para último'''
    caux = Cola()
    ultimo_despegue = []

    if (tamanio(despegues) > 1):
        while (tamanio(despegues) > 1):
            arribo(caux, atencion(despegues))

        ultimo_despegue = atencion(despegues)  # Extrae hora de ultimo despegue
        ultima_hora = ultimo_despegue[1]

        arribo(caux, ultimo_despegue)  # Arriba ultimo despegue

        vuelo[1] = random.randint(ultima_hora, 59)  # Asigna al vuelo reprogramado un horario mayor al último

    else:
        vuelo[1] = random.randint(vuelo[1], 59)  # Cambia el horario del último vuelo para un horario mayor al que tenía

    arribo(caux, vuelo)

    despegues = caux

    return despegues


print("Despegues:")
barridoC(despegues)
print("Aterrizajes:")
barridoC(aterrizajes)

pista = False
hora_actual = int(obtener_hora())

while (not cola_vacia(despegues)) or (not cola_vacia(aterrizajes)):
    if not pista:

        if hora_actual < 59:
            hora_actual += 1
        else:
            hora_actual = 0

        if (not cola_vacia(despegues)):

            prox_despegue = en_frente(despegues)

            if (prox_despegue[1] <= hora_actual) or (cola_vacia(aterrizajes)):
                print("Hora actual: " + str(hora_actual))  # Acordarse sacar esto, es solo para prueba
                print("Que desea hacer con el despegue actual: ")
                opcion = int(input("1- despegar.  2- cancelar.  3- Reprogramar: "))

                prox_despegue = atencion(despegues)

                if (opcion == 1):
                    if prox_despegue[5] == "pasajeros":
                        duracion = 5
                    elif prox_despegue[5] == "carga":
                        duracion = 9
                    else:
                        duracion = 3

                    print("Despegando, durará " + str(duracion) + " seg")
                    time.sleep(duracion)

                elif (opcion == 3):
                    print("Vuelo reprogramado")
                    despegues = reprogramarVuelo(prox_despegue, despegues)

                else:
                    print("Vuelo cancelado")

                print("Despegues:")
                barridoC(despegues)
                print("Aterrizajes:")
                barridoC(aterrizajes)

            else:
                if (not cola_vacia(aterrizajes)):
                    print("Hora actual: " + str(hora_actual))  # Acordarse sacar esto, es solo para prueba
                    prox_aterrizaje = atencion(aterrizajes)
                    if prox_aterrizaje[5] == "pasajeros":
                        duracion = 10
                    elif prox_aterrizaje[5] == "carga":
                        duracion = 7
                    else:
                        duracion = 5

                    print("Aterrizando, durará " + str(duracion) + " seg")
                    time.sleep(duracion)

                    print("Despegues:")
                    barridoC(despegues)
                    print("Aterrizajes:")
                    barridoC(aterrizajes)

        else:
            print("Hora actual: " + str(hora_actual))  # Acordarse sacar esto, es solo para prueba
            prox_aterrizaje = atencion(aterrizajes)
            if prox_aterrizaje[5] == "pasajeros":
                duracion = 10
            elif prox_aterrizaje[5] == "carga":
                duracion = 7
            else:
                duracion = 5

            print("Aterrizando, durará " + str(duracion) + " seg")
            time.sleep(duracion)

            print("Despegues:")
            barridoC(despegues)
            print("Aterrizajes:")
            barridoC(aterrizajes)
"""

"""
    otro = input(print("Desea ingresa un nuevo vuelo para despegar? S/N"))
    if otro == "S":
        vuelo = crear_vuelo()
        despegues = insertar_vuelo_despegues(vuelo, despegues)

    otro = input(print("Desea ingresa un nuevo vuelo para aterrizar? S/N"))
    if otro == "S":
        vuelo = crear_vuelo()
        aterrizajes = insertar_vuelo_aterrizajes(vuelo, aterrizajes)
"""
