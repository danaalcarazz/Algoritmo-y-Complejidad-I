import random
import time
import csv
from statistics import median


# 1. selección
def seleccion(a):
    comparaciones = 0
    movimientos = 0

    for i in range(len(a) - 1):
        menor = i

        for j in range(i + 1, len(a)):
            comparaciones += 1

            if a[j] < a[menor]:
                menor = j

        if menor != i:
            a[i], a[menor] = a[menor], a[i]
            movimientos += 1

    return comparaciones, movimientos


# 2. inserción
def insercion(a):
    comparaciones = 0
    movimientos = 0

    for i in range(1, len(a)):
        actual = a[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if a[j] <= actual:
                break

            a[j + 1] = a[j]
            movimientos += 1
            j -= 1

        a[j + 1] = actual
        movimientos += 1

    return comparaciones, movimientos


# 3. burbuja con bandera
def burbuja(a):
    comparaciones = 0
    movimientos = 0

    for fin in range(len(a) - 1, 0, -1):
        intercambio = False

        for j in range(fin):
            comparaciones += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                movimientos += 1
                intercambio = True

        if not intercambio:
            break

    return comparaciones, movimientos


# 4. quicksort con mediana de tres
def quicksort(a):
    comparaciones = 0
    movimientos = 0

    def ordenar(inicio, fin):
        nonlocal comparaciones, movimientos

        while inicio < fin:
            medio = (inicio + fin) // 2

            #selecciona el pivote con mediana de tres
            candidatos = [
                (a[inicio], inicio),
                (a[medio], medio),
                (a[fin], fin)
            ]

            #ordena tres candidatos contando comparaciones
            for i in range(1, 3):
                j = i

                while j > 0:
                    comparaciones += 1

                    if candidatos[j - 1][0] <= candidatos[j][0]:
                        break

                    candidatos[j - 1], candidatos[j] = (
                        candidatos[j], candidatos[j - 1]
                    )
                    j -= 1

            pivote = candidatos[1][0]

            #partición de tres vías
            menor = inicio
            actual = inicio
            mayor = fin

            while actual <= mayor:
                comparaciones += 1

                if a[actual] < pivote:
                    if actual != menor:
                        a[actual], a[menor] = a[menor], a[actual]
                        movimientos += 1

                    menor += 1
                    actual += 1
                else:
                    comparaciones += 1

                    if a[actual] > pivote:
                        if actual != mayor:
                            a[actual], a[mayor] = a[mayor], a[actual]
                            movimientos += 1

                        mayor -= 1
                    else:
                        actual += 1

            #procesa primero la partición más pequeña
            if menor - inicio < fin - mayor:
                ordenar(inicio, menor - 1)
                inicio = mayor + 1
            else:
                ordenar(mayor + 1, fin)
                fin = menor - 1

    ordenar(0, len(a) - 1)

    return comparaciones, movimientos


# 5. heapsort
def hundir(a, i, tam):
    comparaciones = 0
    movimientos = 0

    while True:
        mayor = i
        izquierdo = 2 * i + 1
        derecho = 2 * i + 2

        if izquierdo < tam:
            comparaciones += 1

            if a[izquierdo] > a[mayor]:
                mayor = izquierdo

        if derecho < tam:
            comparaciones += 1

            if a[derecho] > a[mayor]:
                mayor = derecho

        if mayor == i:
            break

        a[i], a[mayor] = a[mayor], a[i]
        movimientos += 1
        i = mayor

    return comparaciones, movimientos


def heapsort(a):
    comparaciones = 0
    movimientos = 0
    n = len(a)

    #construcción del max-heap
    for i in range(n // 2 - 1, -1, -1):
        c, m = hundir(a, i, n)
        comparaciones += c
        movimientos += m

    #extracción de los máximos
    for fin in range(n - 1, 0, -1):
        a[0], a[fin] = a[fin], a[0]
        movimientos += 1

        c, m = hundir(a, 0, fin)
        comparaciones += c
        movimientos += m

    return comparaciones, movimientos


ALGORITMOS = {
    "Seleccion": seleccion,
    "Insercion": insercion,
    "Burbuja": burbuja,
    "Quicksort": quicksort,
    "Heapsort": heapsort
}

TAMANOS = [1000, 2000, 4000]
REPETICIONES = 7
SEMILLA = 2026


def generar_datos(n, orden):
    generador = random.Random(SEMILLA + n)
    datos = [generador.randint(0, n * 10) for _ in range(n)]

    if orden == "Ordenado":
        datos.sort()
    elif orden == "Inverso":
        datos.sort(reverse=True)

    return datos


def verificar_algoritmos():
    pruebas = [
        [],
        [5],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [3, 1, 3, 2, 1],
        [9, 4, 7, 1, 8, 3]
    ]

    for nombre, algoritmo in ALGORITMOS.items():
        for datos in pruebas:
            copia = datos.copy()
            algoritmo(copia)

            assert copia == sorted(datos), (
                f"Error en {nombre} con {datos}"
            )

    ejemplo = [9, 4, 7, 1, 8, 3]
    comparaciones, movimientos = heapsort(ejemplo)

    assert ejemplo == [1, 3, 4, 7, 8, 9]
    assert (comparaciones, movimientos) == (14, 10)

    print("Todas las pruebas fueron correctas.")


def medir(algoritmo, datos):
    tiempos = []
    esperado = sorted(datos)

    # Ejecución de calentamiento
    calentamiento = datos.copy()
    algoritmo(calentamiento)

    for _ in range(REPETICIONES):
        copia = datos.copy()

        inicio = time.perf_counter_ns()
        comparaciones, movimientos = algoritmo(copia)
        fin = time.perf_counter_ns()

        assert copia == esperado, "Error de ordenamiento."

        tiempos.append((fin - inicio) / 1_000_000)

    return (
        median(tiempos),
        min(tiempos),
        max(tiempos),
        comparaciones,
        movimientos
    )


def ejecutar_benchmark():
    verificar_algoritmos()

    resultados = []
    ordenes = ["Aleatorio", "Ordenado", "Inverso"]

    for orden in ordenes:
        for n in TAMANOS:
            datos = generar_datos(n, orden)

            print(f"\nOrden: {orden} | Tamaño: {n}")

            for nombre, algoritmo in ALGORITMOS.items():
                mediana, minimo, maximo, c, m = medir(
                    algoritmo, datos
                )

                resultados.append({
                    "orden": orden,
                    "n": n,
                    "algoritmo": nombre,
                    "mediana_ms": mediana,
                    "minimo_ms": minimo,
                    "maximo_ms": maximo,
                    "comparaciones": c,
                    "movimientos": m
                })

                print(
                    f"{nombre}: {mediana:.3f} ms | "
                    f"Comparaciones: {c} | Movimientos: {m}"
                )

    with open(
        "resultados.csv", "w",
        newline="", encoding="utf-8-sig"
    ) as archivo:
        escritor = csv.DictWriter(
            archivo,
            fieldnames=resultados[0].keys()
        )

        escritor.writeheader()
        escritor.writerows(resultados)

    print("\nRESULTADOS DEL BENCHMARK")

    for orden in ordenes:
        print(f"\n{orden}")

        for n in TAMANOS:
            grupo = [
                r for r in resultados
                if r["orden"] == orden and r["n"] == n
            ]

            rapido = min(grupo, key=lambda r: r["mediana_ms"])
            lento = max(grupo, key=lambda r: r["mediana_ms"])

            print(
                f"n={n}: más rápido {rapido['algoritmo']}, "
                f"más lento {lento['algoritmo']}"
            )

        print("Factores de crecimiento al duplicar n:")

        for nombre in ALGORITMOS:
            tiempos = {
                r["n"]: r["mediana_ms"]
                for r in resultados
                if r["orden"] == orden
                and r["algoritmo"] == nombre
            }

            for n in TAMANOS[:-1]:
                if 2 * n in tiempos and tiempos[n] > 0:
                    factor = tiempos[2 * n] / tiempos[n]

                    print(
                        f"{nombre}: {n} a {2*n} = "
                        f"{factor:.2f} veces"
                    )

    return resultados


def generar_graficos(resultados):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Instalá matplotlib para generar los gráficos.")
        return

    for orden in ["Aleatorio", "Ordenado", "Inverso"]:
        plt.figure(figsize=(9, 5))

        for nombre in ALGORITMOS:
            datos = [
                r for r in resultados
                if r["orden"] == orden
                and r["algoritmo"] == nombre
            ]

            datos.sort(key=lambda r: r["n"])

            plt.plot(
                [r["n"] for r in datos],
                [r["mediana_ms"] for r in datos],
                marker="o",
                label=nombre
            )

        plt.yscale("log")
        plt.title(f"Benchmark - Datos {orden}")
        plt.xlabel("Tamaño del arreglo (n)")
        plt.ylabel("Tiempo mediano (ms) - escala logarítmica")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig(f"grafico_{orden.lower()}.png")
        plt.close()


if __name__ == "__main__":
    resultados = ejecutar_benchmark()
    generar_graficos(resultados)

    print("\nBenchmark finalizado.")