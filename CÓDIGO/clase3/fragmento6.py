#fibonacci ineficiente
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

try:
    numero = int(input("Introduce la posición de fibonacci que deseas calcular: "))
    if numero < 0:
        raise ValueError("El número debe ser mayor o igual a 0.")
    resultado = fibonacci(numero)
    print(f"El número de fibonacci en la posición {numero} es: {resultado}.")

except ValueError as error:
    print(f"Error: {error}")