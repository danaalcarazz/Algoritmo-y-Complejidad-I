#búsqueda binariad
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

entrada = input("Introduce números ordenados separados por comas: ")

mi_lista = entrada.split(",")
mi_lista = [int(elemento.strip()) for elemento in mi_lista if elemento.strip() != ""]

objetivo = int(input("Introduce el número que deseas buscar: "))

resultado = busqueda_binaria(mi_lista, objetivo)

if resultado != -1:
    print(f"El número se encuentra en la posición {resultado}.")
else:
    print("El número no se encuentra en la lista.")