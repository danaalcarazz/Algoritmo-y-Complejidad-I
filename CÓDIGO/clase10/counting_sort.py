def counting_sort(arreglo):
    if not arreglo:
        return []

    minimo = min(arreglo)
    maximo = max(arreglo)
    conteo = [0] * (maximo - minimo + 1)

    for numero in arreglo:
        conteo[numero - minimo] += 1
    resultado = []
    for i in range(len(conteo)):
        resultado.extend([i + minimo] * conteo[i])
    return resultado

numeros = [35, 12, 44, 1, 15, 6, 3, 4]
resultado = counting_sort(numeros)

print("Arreglo original:", numeros)
print("Arreglo ya ordenado:", resultado)