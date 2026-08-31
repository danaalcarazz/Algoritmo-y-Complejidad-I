#búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

entrada = input("Introduce los elementos separados por comas: ")

mi_lista = entrada.split(",")
mi_lista = [elemento.strip() for elemento in mi_lista if elemento.strip() != ""]

objetivo = input("Introduce el elemento que deseas buscar: ").strip()

resultado = busqueda_lineal(mi_lista, objetivo)

if resultado != -1:
    print(f"El elemento se encuentra en la posición {resultado}.")
else:

    print("El elemento no se encuentra en la lista.")