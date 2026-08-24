from pila_arreglo import PilaArreglo
from pila_lista import PilaLista

def probar_pila(pila, nombre):
    print(nombre)

    print("1. La pila está vacía:", pila.estaVacia())
    print("2. Tamaño inicial:", pila.tamaño())

    print("\nApilando 1, 2, 3")
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)

    print("3. La pila está vacía:", pila.estaVacia())
    print("4. Tamaño:", pila.tamaño())
    print("5. Cima:", pila.cima())

    print("\nDesapilando...")
    primero = pila.desapilar()
    segundo = pila.desapilar()
    tercero = pila.desapilar()

    print("6. Elementos desapilados:", primero, segundo, tercero)
    print("7. La pila está vacía:", pila.estaVacia())
    print("8. Tamaño final:", pila.tamaño())

    return [primero, segundo, tercero]

def main():
    pila_arreglo = PilaArreglo()
    pila_lista = PilaLista()

    resultado_arreglo = probar_pila(
        pila_arreglo,
        "Arreglo dinámico"
    )

    resultado_lista = probar_pila(
        pila_lista,
        "\nLista enlazada"
    )

    print("\nComparación de resultados")

    if resultado_arreglo == resultado_lista:
        print("Las dos implementaciones producen el mismo resultado.")
    else:
        print("Las implementaciones producen resultados diferentes.")

if __name__ == "__main__":
    main()