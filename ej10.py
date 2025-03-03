almacenes = 2
pieza = 3
costes = []
tablaM3N2 = [
    [31, 42, 64],
    [50, 101, 194],
    [50, 101, 194],
    [19.61, 23, 86.4]
]
sumaTotal = sum(tablaM3N2[0] + tablaM3N2[1])
print(f"Este es el valor general: {sumaTotal}")
valorTotalPieza1 = sum(tablaM3N2[fila][0] for fila in range(almacenes))
print(f"El valor valor de la pieza 1: {valorTotalPieza1}")
valorTotalPieza2 = sum(tablaM3N2[fila][1] for fila in range(almacenes))
print(f"El valor valor de la pieza 2: {valorTotalPieza2}")
valorTotalPieza3 = sum(tablaM3N2[fila][2] for fila in range(almacenes))
print(f"El valor de la pieza 3: {valorTotalPieza3}")

valorTotalPiezas1 = sum(tablaM3N2[0])
print(f"El valor de las piezas en el almacén 1 es: {valorTotalPiezas1}")
valorTotalPiezas2 = sum(tablaM3N2[1])
print(f"El valor de las piezas en el almacén 2 es: {valorTotalPiezas2}")
