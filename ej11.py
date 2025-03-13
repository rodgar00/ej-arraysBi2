divisas = [
    ["Dólar", 0.82],
    ["Libra esterlina", 1.072],
    ["Yen", 0.0075],
    ["Dirham", 0.084]
]

moneda_origen = input("¿Qué moneda tienes? (Dólar, Libra esterlina, Yen, Dirham): ")
cantidad_origen = float(input(f"¿Cuántos {moneda_origen} tienes?: "))
moneda_destino = input("¿Qué moneda quieres? (Dólar, Libra esterlina, Yen, Dirham): ")

indice_origen = -1
indice_destino = -1
for i in range(len(divisas)):
    if divisas[i][0] == moneda_origen:
        indice_origen = i
    if divisas[i][0] == moneda_destino:
        indice_destino = i

if indice_origen != -1 and indice_destino != -1:
    euros = cantidad_origen * divisas[indice_origen][1]
    cantidad_destino = euros / divisas[indice_destino][1]
    print(f"{cantidad_origen} {moneda_origen} equivalen a {cantidad_destino: 2f} {moneda_destino}.")
else:
    print("Moneda no válida.")
