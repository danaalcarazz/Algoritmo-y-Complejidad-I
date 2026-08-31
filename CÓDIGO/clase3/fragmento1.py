#acceso directo
def ultimo_elemento(lista):
    if len(lista) == 0:
        raise ValueError("El arreglo está vacío.")
    return lista[-1]

entrada = input("Introduce elementos separados por comas: ")

mi_lista = entrada.split(",")
mi_lista = [elemento.strip() for elemento in mi_lista if elemento.strip() != ""]

try:
    resultado = ultimo_elemento(mi_lista)
    print(f"El último elemento de la lista es: {resultado}")

except ValueError as error:
    print(f"{error}")