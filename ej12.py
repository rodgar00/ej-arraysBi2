empleados = 5
ventas = []

for i in range(empleados):
    nombre = input(f"Ingrese el nombre del vendedor {i + 1}: ")
    ventas.append([nombre, 0, 0])

    venta = -1
    while venta != 0:
        venta = float(input(f"Ingrese el importe de la venta de {nombre} (0 para terminar): "))
        if venta != 0:
            ventas[i][1] += venta
            ventas[i][2] += 1

venta_total_empresa = 0
venta_media_empresa = 0

for i in range(empleados):
    total_ventas = ventas[i][1]
    ventas_vendedor = ventas[i][2]
    venta_media_vendedor = total_ventas / ventas_vendedor if ventas_vendedor != 0 else 0
    venta_total_empresa += total_ventas

    print(f"Vendedor: {ventas[i][0]}")
    print(f"Venta total: {total_ventas:.2f}")
    print(f"Venta media: {venta_media_vendedor:.2f}")
    print("-" * 20)

venta_media_empresa = venta_total_empresa / sum(
    ventas[i][2] for i in range(empleados)) if venta_total_empresa != 0 else 0

print(f"Venta total de la empresa: {venta_total_empresa:.2f}")
print(f"Venta media de la empresa: {venta_media_empresa:.2f}")
