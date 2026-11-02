def insertion_sort(arreglo):
    numeros = arreglo.copy()

    for i in range(1, len(numeros)):
        actual = numeros[i]
        j = i - 1
        while j >= 0 and numeros[j] > actual:
            numeros[j + 1] = numeros[j]
            j -= 1
        numeros[j + 1] = actual
    return numeros

numeros = [35, 12, 44, 1, 15, 6, 3, 4]
resultado = insertion_sort(numeros)

print("Arreglo original:", numeros)
print("Arreglo ordenado:", resultado)