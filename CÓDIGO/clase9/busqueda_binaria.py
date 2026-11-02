def busqueda_binaria(arreglo, objetivo):
    izquierda = 0
    derecha = len(arreglo) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arreglo[medio] == objetivo:
            return medio
        elif arreglo[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


numeros = [1, 3, 4, 6, 12, 15, 35, 44]
objetivo = 12
resultado = busqueda_binaria(numeros, objetivo)

if resultado != -1:
    print(f"El número {objetivo} se encontró en el índice {resultado}")
else:
    print("El número no se encontró")