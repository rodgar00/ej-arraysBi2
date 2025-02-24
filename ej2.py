from ayuda import printMatriz

fila = 3
columna = 4

matriz = []

for nFilas in range(fila):
    matriz.append([])
    for nColumnas in range(columna):
        valor = int(input(f"Introduce los valores para{nFilas+1},{nColumnas+1} "))
        matriz[nFilas].append(valor)

sumaFilas = []
for i in range (fila):
    suma = 0
    for j in range(columna):
        suma += matriz[i][j]
    sumaFilas.append(suma)

valorMaximo = []
maximo = max(sumaFilas)
valorMaximo.append(maximo)

printMatriz(matriz)
print(sumaFilas)
print(f"El resultado mayor es {valorMaximo}")
