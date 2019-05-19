import random


def fibonacci(x):
    if x == 0 or x == 1:
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)


def suma(num):
    if num == 1:
        return num
    else:
        return (num + suma(num - 1))


def producto(n1, n2):
    if (n1 == 0 or n2 == 0):
        return 0
    elif (n2 == 1):
        return n1
    else:
        return n1 + producto(n1, n2 - 1)


def potencia(b, e):
    if e == 0:
        return 1
    else:
        return b * (potencia(b, e - 1))


def invertir_str(palabra):
    if len(palabra) == 1:
        return(palabra)
    else:
        return(palabra[len(palabra) - 1]) + invertir_str(palabra[0:len(palabra) - 1])


def serie(num):
    if num == 1:
        return 1
    else:
        return (1/num) + (serie(num - 1))


def ent_bin(num):
    if num <= 1:
        return str(num)
    else:
        return ent_bin(num // 2) + str((num % 2))


def logaritmo(n, b):
    if n <= b:
        return 1
    else:
        return (1 + logaritmo(n/b, b))


def cant_dig(num):
    if num == 0:
        return 0
    else:
        return 1 + cant_dig(num // 10)


def invertir_num(num):
    if (num // 10) == 0:
        return num
    else:
        return str(invertir_num(num % 10)) + str(invertir_num(num // 10))


def euclidesmcd(a, b):
    if a < b:
        return euclidesmcd(b, a)
    elif b == 0:
        return a
    else:
        return euclidesmcd(b, (a % b))


def euclidesmcm(a, b):
    if a < b:
        return euclidesmcm(b, a)
    else:
        return (a * b) / (euclidesmcd(a, b))


def suma_dig(num):
    if num < 10:
        return num
    else:
        return (num % 10) + suma_dig(num // 10)


def raiz(r, num):
    if (r+1) * (r+1) > num:
        return r
    else:
        return raiz(r + 1, num)


def recorrermat(m, i, j):
    if i >= 0 and j >= 0:
        print(m[i][j])
        if j == 0:
            i -= 1
            j = len(m[i])
        recorrermat(m, i, j - 1)


def intercambio(a, b):
    c = a
    a = b
    b = c


def quicksort(vect, pri, ult):
    i = pri
    j = ult - 1
    pivot = ult
    while (i < j):
        while (vect[i] <= vect[pivot]) and (i < j):
            i += 1
        while (vect[j] > vect[pivot]) and (i < j):
            j -= 1
        vect[i], vect[j] = vect[j], vect[i]
    if vect[i] > vect[pivot]:
        vect[pivot], vect[i] = vect[i], vect[pivot]
    if pri < j:
        quicksort(vect, pri, j)
    if ult > i:
        quicksort(vect, i+1, ult)
    return vect


def bbin_R(lista, primero, ultimo, buscado):

    if (primero <= ultimo):
        med = (primero + ultimo) // 2
        if lista[med] == buscado:
            return med
        else:
            if lista[med] > buscado:
                return bbin_R(lista, primero, med - 1, buscado)
            else:
                return bbin_R(lista, med + 1, ultimo, buscado)
    else:
        return -1


def laber(lab, x, y, camino):
    f, c = len(lab), len(lab)
    if ((x >= 0 and x <= f) and (y >= 0 and y <= c)):
        if (lab[x][y] == 2):
            camino.append([x, y])
            print('Saliste del laberinto')
            print(camino)
        elif(lab[x][y] == 1):
            lab[x][y] = 3
            camino.append([x, y])
            laber(lab, x, y + 1, camino)
            laber(lab, x, y - 1, camino)
            laber(lab, x + 1, y, camino)
            laber(lab, x - 1, y, camino)
            camino.pop()
            lab[x][y] = 1


def moverTorre(altura, origen, destino, intermedio):
    if altura >= 1:
        moverTorre(altura-1, origen, intermedio, destino)
        moverDisco(origen, destino)
        moverTorre(altura-1, intermedio, destino, origen)


def moverDisco(desde, hacia):
    print("mover disco de", desde, "a", hacia)


def sucesion(n):
    if n == 1:
        return 3
    else:
        return ((n - 1) + 1)


def merge(izq, der):
    mez = []
    i = 0
    j = 0
    while(i < len(izq) and j < len(der)):
        if(izq[i] <= der[j]):
            mez.append(izq[i])
            i = i + 1
        else:
            mez.append(der[j])
            j = j + 1
    while(i < len(izq)):
        mez.append(izq[i])
        i = i + 1
    while(j < len(der)):
        mez.append(der[j])
        j = j + 1

    return mez


def mergesort(vect):
    if(len(vect) <= 1):
        return vect
    else:
        izq = []
        der = []
        medio = len(vect) // 2
        for i in range(0, medio):
            izq.append(vect[i])
        for i in range(medio, len(vect)):
            der.append(vect[i])

        izq = mergesort(izq)
        der = mergesort(der)
        return merge(izq, der)
