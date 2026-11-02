def busqueda_secuencial(arreglo, objetivo):
    for i in range(len(arreglo)):
        if arreglo[i] == objetivo:
            return i
    return -1

numeros = [1, 3, 4, 6, 12, 15, 35, 44]
objetivo = 12
resultado = busqueda_secuencial(numeros, objetivo)

if resultado != -1:
    print(f"El número {objetivo} se encontró en el índice {resultado}")
else:
    print("El número no se encontró")