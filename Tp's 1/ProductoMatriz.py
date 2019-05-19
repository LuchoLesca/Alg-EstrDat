"""
# m1 = [[2, 1, 1], [0, 2, 3]]
# m2 = [[1, 3], [0, 0], [1, 2]]

m1 = [[3, 6], [5, 4], [1, -1], [3, 2], [2, 1]]
m2 = [[0, 1, 9, 8], [1, 10, 3, 4]]
m3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# f1 = 2
# c1 = 3
# f2 = 3
# c2 = 2
f1 = 5
c1 = 2
f2 = 2
c2 = 4

if (c1 != f2):
    print('No se puede realizar la op. El numero de f y c no coincide')
else:
    for i in range(0, f1):  # Cuenta las filas de la matriz resultante
        for j in range(0, c2):  # Cuenta las columnas de matriz resultante
            m3[i][j] = 0  # iniciar elemento de esa posición
            for h in range(0, c1):
                m3[i][j] = (m1[i][h] * m2[h][j]) + m3[i][j]


for i in range(0, f1):
    print('Fila ' + str(i + 1))
    for j in range(0, c2):
        print(m3[i][j])
"""

# Busquena binaria recursaiva







pos = -1
