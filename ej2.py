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
    valor = 0
    for j in range(columna):
        valor += matriz[i][j]
    sumaFilas.append(valor)

valorMaximo = []
máximo = max(sumaFilas)
valorMaximo.append(máximo)

print(printMatriz(matriz))
print(sumaFilas)
print(f"El resultado mayor es {valorMaximo}")
