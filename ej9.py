import random

from ayuda import printMatriz

matriz = []
for nFilas in range(3):
    fila = [random.randint(1, 10) for nColumnas in range(3)]
    matriz.append(fila)

a, b, c = matriz[0]
d, e, f = matriz[1]
g, h, i = matriz[2]

determinante = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

printMatriz(matriz)
print(f"El determinante de la matriz es: {determinante}")
