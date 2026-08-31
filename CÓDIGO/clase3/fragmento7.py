#iteración anidada con saltos
def iteracion_anidada(n):
    for i in range(n):
        j = 1
        while j < n:
            print(f"i = {i}, j = {j}")
            j *= 2

try:
    numero = int(input("Introduce un número entero positivo: "))
    if numero <= 0:
        raise ValueError("El número debe ser positivo.")
    iteracion_anidada(numero)

except ValueError as error:
    print(f"Error: {error}")