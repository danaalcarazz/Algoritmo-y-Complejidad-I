#procesamiento de múltiples conjuntos
def procesar_listas(lista_n, lista_m):
    suma = 0    
    for elemento in lista_n:
        suma += elemento
    
    multiplicacion = 1 if lista_m else 0
    for elemento in lista_m:
        multiplicacion *= elemento
        
    return suma, multiplicacion

entrada_n = input("Introduce los elementos de la lista N separados por comas: ")

lista_n = entrada_n.split(",")
lista_n = [int(elemento.strip()) for elemento in lista_n if elemento.strip() != ""]

entrada_m = input("Introduce los elementos de la lista M separados por comas: ")

lista_m = entrada_m.split(",")
lista_m = [int(elemento.strip()) for elemento in lista_m if elemento.strip() != ""]

suma, multiplicacion = procesar_listas(lista_n, lista_m)

print(f"La suma de los elementos de N es: {suma}")
print(f"La multiplicación de los elementos de M es: {multiplicacion}")