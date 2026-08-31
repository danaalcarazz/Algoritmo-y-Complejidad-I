#división sucesiva
def divisiones_sucesivas(n):
    contador = 0
    while n > 1:
        n = n // 2
        contador += 1
    return contador

try:
    numero = int(input("Introduce un número entero positivo: "))
    if numero <= 0:
        raise ValueError("El número debe ser positivo.")
    resultado = divisiones_sucesivas(numero)
    print(f"Se realizaron {resultado} divisiones.")

except ValueError as error:
    print(f"Error: {error}")