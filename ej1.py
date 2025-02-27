from ayuda import printMatriz

filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

if filas % 2 == 0 or columnas % 2 == 0:
    print("Las filas y columnas deben ser impares.")
else:
    matriz = []
    for nFilas in range(filas):
        matriz.append([])
        for nColumnas in range(columnas):
            valor = int(input(f"Introduce los valores para [{nFilas + 1}],[{nColumnas + 1}] sin repeticiones: "))
            matriz[nFilas].append(valor)

    resultadoF = []
    for i in range(filas):
        suma = 0
        for j in range(columnas):
            suma += matriz[i][j]
        resultadoF.append(suma)

    resultadoC = []
    for i in range(filas):
        suma = 0
        for j in range(columnas):
            suma += matriz[j][i]
        resultadoC.append(suma)

    resultadoDiagonalpp = 0
    for i in range(filas):
        for j in range(columnas):
            if i == j:
                resultadoDiagonalpp += matriz[i][j]

    resultadoDiagonalsecun = 0
    for i in range(filas):
        resultadoDiagonalsecun += matriz[i][columnas - i - 1]

    def esMagico():
        if resultadoDiagonalpp != resultadoDiagonalsecun:
            return False
        for i in range(len(resultadoF)):
            if resultadoC[i] != resultadoDiagonalpp or resultadoF[i] != resultadoDiagonalpp:
                return False
        return True

    if esMagico():
        print(printMatriz(matriz))
        print("Es un cuadrado mágico")
    else:
        print("No son los resultados iguales")
