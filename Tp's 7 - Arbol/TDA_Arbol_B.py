# Grado de nodo = LA cantidad de nodos que hereda(hijo) un nodos
# Grqdo del arbol(aridad) = es el mayor grado de nodo que posea
# Rama(arista) = camino entre un nodo y el siguiente. Hay un solo camino de
# ramas para llegar de un nodo a otro
# Nivel de un nodo = Se termina entre la cantidad de ramas que hay entre un
# nodo y la raíz. Esto más 1
# Altura de un nodo = es la mayor cantidad de ramas entre ese nodo y la hoja
# más lejana

"""
# BARRIDOS
- Inorden: muestra todos los elementos de manera ordenada
- Preorden: muestra elementos de manera que fueron cargados
- Postorden: muestra elementos en sentido inverso
"""

# Arbol binario (caso particular) como maximo, cada nodo puede tener 2 nodos

"""
Barrido preorden:
Tratar nodo (mostrar, sumar, etc.)
Llama a preorden(nodo.izq)
Llama a preorden(nodo.der)

"""
"""
def preorden(raiz):  # Va a servir para hacer una búsqueda más facilmente
    print(raiz.info)
    preorden(raiz.izq)
    preorden(raiz.der)
"""
"""
Barrido inorden:
inorden(raiz.izq)
tratar nodo
inorden(raiz.der)
"""
"""
def inorden(raiz):
    inorden(raiz.izq)
    print(raiz.info)
    inorden(raiz.der)
"""
"""
Barrido postorden:
postorden(raiz.der)
tratar nodo
postorden(raiz.izq)
"""
"""
def postorden(raiz):
    inorden(raiz.der)
    print(raiz.info)
    inorden(raiz.izq)


def busqueda(raiz, buscado):
    pos = None
    if raiz is not None:
        if raiz.info == buscado:
            pos = raiz
        else:
            if raiz.info > buscado:
                pos = busqueda(raiz.izq, buscado)
            else:
                pos = busqueda(raiz.der, buscado)

    return pos
"""
