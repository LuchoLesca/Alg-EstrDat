from TDA_Arbol import *
from random import randint


r = None
"""
r = insertar(r, 4)
r = insertar(r, 20)
r = insertar(r, 21)
r = insertar(r, 0)
r = insertar(r, 2)
r = insertar(r, 15)
r = insertar(r, 12)
"""

for i in range(1, 17):
    r = insertar(r, i)

preorden(r)
print()
