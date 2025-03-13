simbolos_base13 = [
    ["+", 0],
    ["-", 1],
    ["*", 2],
    ["/", 3],
    ["=", 4],
    ["?", 5],
    ["\\", 6],
    ["!", 7],
    ["¿", 8],
    ["$", 9],
    ["(", 10],
    ["@", 11],
    ["#", 12]
]

def decimal_a_base13(num):
    if num == 0:
        return simbolos_base13[0][0]
    resultado = ""
    while num > 0:
        resultado = simbolos_base13[num % 13][0] + resultado
        num = num // 13
    return resultado

numero_decimal = int(input("Introduce un número decimal: "))
numero_base13 = decimal_a_base13(numero_decimal)
print(f"{numero_decimal} en base 13 es: {numero_base13}")

def base13_a_decimal(num_base13):
    decimal = 0
    for i, simbolo in enumerate(num_base13[::-1]):
        for j in range(len(simbolos_base13)):
            if simbolos_base13[j][0] == simbolo:
                valor = simbolos_base13[j][1]
                decimal += valor * (13 ** i)
    return decimal

numero_base13 = input("Introduce un número en base 13: ")
numero_decimal = base13_a_decimal(numero_base13)
print(f"{numero_base13} en decimal es: {numero_decimal}")
