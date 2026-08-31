#detección de duplicados
def tiene_duplicados(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j]:
                return True
    return False
entrada = input("Introduce los elementos separados por comas: ")

mi_lista = entrada.split(",")
mi_lista = [elemento.strip() for elemento in mi_lista if elemento.strip() != ""]

if tiene_duplicados(mi_lista):
    print("La lista contiene elementos duplicados.")
else:
    print("La lista no contiene elementos duplicados.")