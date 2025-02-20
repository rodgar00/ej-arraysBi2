from ayuda import printMatriz
filas = 4
columnas = 4

matriz = []

for nFilas in range(filas):
    matriz.append([])
    for nColumnas in range(columnas):
        valor = int(input(f"Introduce los valores para [{nFilas + 1}],[{nColumnas + 1}] sin repeticiones: "))
        matriz[nFilas].append(valor)

resultadoC = []
for i in range(filas):
    suma = 0
    for j in range(columnas):
        suma += matriz[i][j]
    resultadoC.append(suma)

resultadoF = []
for i in range(filas):
    suma = 0
    for j in range(columnas):
        suma += matriz[j][i]
    resultadoF.append(suma)

resultadoDiagonalpp = 0
for i in range(filas):
    resultadoDiagonalpp += matriz[i][i]

resultadoDiagonalsecun = 0
for i in range(filas):
    resultadoDiagonalsecun += matriz[i][columnas - i - 1]

print(resultadoF)
print(resultadoC)
print(resultadoDiagonalsecun)
print(resultadoDiagonalpp)

def esMagico():
    if resultadoDiagonalpp!=resultadoDiagonalsecun:
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

