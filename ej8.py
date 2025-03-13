matriz1 = [
    [2, 0, 1],
    [3, 0, 0],
    [5, 1, 1]
]
matriz2 = [
    [1, 0, 1],
    [1, 2, 1],
    [1, 1, 0]
]

matrizResuelta = [[0 for nFilas in range(3)] for nColumnas in range(3)]

for i in range(3):
    for j in range(3):
        matrizResuelta[i][j] = (
            matriz1[i][0] * matriz2[0][j] +
            matriz1[i][1] * matriz2[1][j] +
            matriz1[i][2] * matriz2[2][j]
        )

print(matrizResuelta)
