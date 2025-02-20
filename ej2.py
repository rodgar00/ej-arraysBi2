fila = 3
columna = 4

matriz = []

for nFilas in range(fila):
    matriz.append([])
    for nColumnas in range(columna):
        valor = int(input(f"Introduce los valores para{nFilas+1},{nColumnas+1} "))
        matriz[nFilas].append(valor)

