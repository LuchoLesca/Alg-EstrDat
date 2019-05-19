from Polinomios import crear, cargar, grado, producto, suma
from random import randint


p1 = crear(randint(0, 5))
p2 = crear(randint(0, 5))

for i in range(0, grado(p1) + 1):
    cargar(p1, i, randint(0, 3))

for i in range(0, grado(p2) + 1):
    cargar(p2, i, randint(0, 3))

print(p1)
print(p2)

print(suma(p1, p2))
print(producto(p1, p2))
