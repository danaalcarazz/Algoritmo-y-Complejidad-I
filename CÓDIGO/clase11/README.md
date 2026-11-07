**Clase 11 - Benchmark de Algoritmos de Ordenamiento**



En esta actividad se implementa un benchmark para comparar el rendimiento de cinco algoritmos de ordenamiento: Selección, Inserción, Burbuja, Quicksort y Heapsort.



El objetivo es medir sus tiempos de ejecución utilizando los mismos conjuntos de datos, analizar sus comparaciones y movimientos, y relacionar los resultados experimentales con la complejidad teórica de cada algoritmo.



**1.Algoritmos implementados.**

1.1 Selection Sort (Selección)



Este algoritmo busca el elemento menor dentro de la parte no ordenada del arreglo y lo intercambia con el elemento de la posición correspondiente.



Complejidad:

\- Mejor caso: O(n²).

\- Caso promedio: O(n²).

\- Peor caso: O(n²).

\- Espacio auxiliar: O(1).



Propiedades:

\- No es estable en su implementación tradicional.

\- No es adaptable, porque realiza prácticamente las mismas comparaciones independientemente del orden inicial.

\- Es in-place.



1.2. Insertion Sort (Inserción)



Ordena los elementos progresivamente, insertando cada valor en su posición correcta dentro de la parte previamente ordenada.



Complejidad:

\- Mejor caso: O(n).

\- Caso promedio: O(n²).

\- Peor caso: O(n²).

\- Espacio auxiliar: O(1).



Propiedades:

\- Es estable.

\- Es adaptable, porque mejora su rendimiento cuando los datos están casi ordenados.

\- Es in-place.



1.3. Bubble Sort (Burbuja)

Compara elementos consecutivos y los intercambia cuando están en el orden incorrecto. La implementación utiliza una bandera para detenerse cuando no se producen intercambios.



Complejidad:

\- Mejor caso: O(n).

\- Caso promedio: O(n²).

\- Peor caso: O(n²).

\- Espacio auxiliar: O(1).



Propiedades:

\- Es estable.

\- Es adaptable en la implementación con bandera.

\- Es in-place.



1.4. Quicksort

Utiliza la estrategia Divide y Vencerás, seleccionando un pivote para separar los elementos en particiones.



La implementación utiliza mediana de tres para seleccionar el pivote y una partición de tres vías.



Complejidad:

\- Mejor caso: O(n log n).

\- Caso promedio: O(n log n).

\- Peor caso: O(n²).

\- Espacio auxiliar: depende de la profundidad de las llamadas recursivas.



Propiedades:

\- No es estable.

\- Trabaja principalmente sobre el mismo arreglo.

\- Su rendimiento depende de la distribución de los datos y de la selección del pivote.



1.5. Heapsort



Utiliza una estructura de árbol denominada heap o montículo. Primero construye un Max-Heap y posteriormente extrae los elementos mayores para colocarlos en su posición definitiva.



Complejidad:

\- Mejor caso: O(n log n).

\- Caso promedio: O(n log n).

\- Peor caso: O(n log n).

\- Espacio auxiliar: O(1).



Propiedades:

\- No es estable.

\- No es adaptable.

\- Es in-place.

\- Garantiza un rendimiento O(n log n) incluso en el peor caso.



**2. Metodología del benchmark**



Para comparar los algoritmos se utilizaron tres tamaños de entrada:



\- n = 1.000 elementos.

\- n = 2.000 elementos.

\- n = 4.000 elementos.



Se evaluaron tres órdenes iniciales:



\- Aleatorio: elementos distribuidos sin un orden específico.

\- Ordenado: elementos organizados de menor a mayor.

\- Inverso: elementos organizados de mayor a menor.



Todos los algoritmos recibieron copias de los mismos datos para garantizar una comparación bajo condiciones equivalentes.



Cada algoritmo se ejecutó siete veces por combinación, además de una ejecución inicial de calentamiento.



Los tiempos fueron medidos mediante "time.perf\_counter\_ns()", utilizando la mediana para reducir la influencia de valores extremos.



También se registraron las comparaciones entre elementos y los movimientos realizados durante el ordenamiento.



Los resultados se almacenaron en el archivo "resultados.csv" y se representaron mediante gráficos con escala logarítmica.



**3. Ejecución manual de Heapsort**



Se utiliza el siguiente arreglo:

\[9, 4, 7, 1, 8, 3]



3.1. Construcción del Max-Heap



El último nodo padre se calcula mediante:



n // 2 - 1 = 6 // 2 - 1 = 2



Se comienza desde el índice 2 y se reorganizan los elementos para que cada padre sea mayor o igual que sus hijos.



Arreglo después de construir el Max-Heap:



\[9, 8, 7, 1, 4, 3]



Durante esta fase se realizan:

\- 5 comparaciones.

\- 1 intercambio.



3.2. Extracción de elementos



Se intercambia repetidamente el elemento mayor con el último elemento del heap y se reorganiza la parte restante.



Paso 1:

\[8, 4, 7, 1, 3 | 9]



Paso 2:

\[7, 4, 3, 1 | 8, 9]



Paso 3:

\[4, 1, 3 | 7, 8, 9]



Paso 4:

\[3, 1 | 4, 7, 8, 9]



Paso 5:

\[1 | 3, 4, 7, 8, 9]



Resultado final:



\[1, 3, 4, 7, 8, 9]



3.3. Conteo de operaciones



\- Construcción del heap: 5 comparaciones y 1 intercambio.

\- Extracción de elementos: 9 comparaciones y 9 intercambios.

\- Total: 14 comparaciones y 10 intercambios.



Estos resultados coinciden con los contadores obtenidos mediante la implementación en Python.



**4. Análisis de los resultados**



4.1. ¿Qué algoritmo fue el más rápido y cuál el más lento para cada orden inicial?



Datos aleatorios.



Con 1.000 elementos:

\- Más rápido: Heapsort (3,294 ms).

\- Más lento: Burbuja (112,892 ms).



Con 2.000 elementos:

\- Más rápido: Heapsort (10,709 ms).

\- Más lento: Burbuja (553,899 ms).



Con 4.000 elementos:

\- Más rápido: Heapsort (22,295 ms).

\- Más lento: Burbuja (2.567,684 ms).



Heapsort fue el más rápido en las tres pruebas porque mantiene una complejidad O(n log n), lo que permite ordenar grandes cantidades de elementos con un crecimiento moderado de operaciones.



Burbuja fue el más lento porque necesita realizar numerosas comparaciones e intercambios. Su complejidad promedio O(n²) provoca que el tiempo aumente considerablemente cuando crece el arreglo.



Datos ordenados.



Con 1.000 elementos:

\- Más rápido: Burbuja (0,175 ms).

\- Más lento: Selección (84,987 ms).



Con 2.000 elementos:

\- Más rápido: Burbuja (0,381 ms).

\- Más lento: Selección (331,077 ms).



Con 4.000 elementos:

\- Más rápido: Burbuja (0,213 ms).

\- Más lento: Selección (588,495 ms).



Burbuja fue el más rápido porque su implementación utiliza una bandera que permite finalizar cuando no se realizan intercambios.



Como los elementos ya estaban ordenados, solamente necesitó una pasada, obteniendo un comportamiento O(n).



Selección fue el más lento porque continúa buscando el elemento mínimo en cada iteración, incluso cuando el arreglo ya está ordenado. Por ello, mantiene su complejidad O(n²).



Datos inversos.



Con 1.000 elementos:

\- Más rápido: Heapsort (1,987 ms).

\- Más lento: Inserción (77,181 ms).



Con 2.000 elementos:

\- Más rápido: Heapsort (15,995 ms).

\- Más lento: Burbuja (1.184,066 ms).



Con 4.000 elementos:

\- Más rápido: Heapsort (35,606 ms).

\- Más lento: Burbuja (4.001,914 ms).



Heapsort fue el más rápido porque conserva su complejidad O(n log n) independientemente del orden inicial de los elementos.



Inserción y Burbuja presentan un comportamiento desfavorable cuando los datos están en orden inverso, ya que necesitan realizar numerosos desplazamientos e intercambios.



En este caso, ambos se aproximan a su peor comportamiento O(n²), mientras que Heapsort mantiene un crecimiento más eficiente.



4.2. ¿Al duplicar n los tiempos aumentan según la complejidad teórica?



Para comprobarlo se utiliza la relación:



Factor de crecimiento = T(2n) / T(n)



En los algoritmos cuadráticos, la relación esperada es aproximadamente:



(2n)² / n² = 4



Para los algoritmos O(n log n), la relación es:



2 × log(2n) / log(n)



Por lo tanto, al duplicar n se espera un crecimiento algo superior a dos veces, aproximadamente 2,20 para los tamaños evaluados.



Resultados con datos aleatorios.



De 1.000 a 2.000 elementos:

\- Selección: 4,21 veces.

\- Inserción: 7,70 veces.

\- Burbuja: 4,91 veces.

\- Quicksort: 3,17 veces.

\- Heapsort: 3,25 veces.



De 2.000 a 4.000 elementos:

\- Selección: 2,61 veces.

\- Inserción: 3,21 veces.

\- Burbuja: 4,64 veces.

\- Quicksort: 2,08 veces.

\- Heapsort: 2,08 veces.



Interpretación:



Burbuja presentó factores cercanos a cuatro, especialmente al pasar de 2.000 a 4.000 elementos.



Selección e Inserción mostraron variaciones, aunque sus tiempos aumentaron considerablemente al duplicar el tamaño.



Quicksort y Heapsort presentaron un crecimiento cercano al esperado para O(n log n) en la segunda duplicación.



Resultados con datos ordenados.



De 1.000 a 2.000 elementos:

\- Selección: 3,90 veces.

\- Inserción: 1,13 veces.

\- Burbuja: 2,18 veces.

\- Quicksort: 2,88 veces.

\- Heapsort: 2,05 veces.



De 2.000 a 4.000 elementos:

\- Selección: 1,78 veces.

\- Inserción: 1,33 veces.

\- Burbuja: 0,56 veces.

\- Quicksort: 0,80 veces.

\- Heapsort: 0,85 veces.



Interpretación:



Inserción y Burbuja con bandera aprovechan que los datos ya están ordenados, por lo que presentan un comportamiento O(n) y no se espera que sus tiempos se multipliquen por cuatro.



Selección continúa realizando O(n²) comparaciones, aunque los factores experimentales no siempre coinciden con el valor teórico.



Algunos tiempos disminuyeron al aumentar n, lo que indica variaciones experimentales que pueden relacionarse con la carga del sistema, la resolución de las mediciones y otros factores de ejecución.



Resultados con datos inversos.



De 1.000 a 2.000 elementos:

\- Selección: 4,20 veces.

\- Inserción: 3,79 veces.

\- Burbuja: 17,50 veces.

\- Quicksort: 6,78 veces.

\- Heapsort: 8,05 veces.



De 2.000 a 4.000 elementos:

\- Selección: 12,77 veces.

\- Inserción: 10,38 veces.

\- Burbuja: 3,38 veces.

\- Quicksort: 3,02 veces.

\- Heapsort: 2,23 veces.



Interpretación:

Selección e Inserción se aproximaron al factor cuatro durante la primera duplicación.



Burbuja presentó un crecimiento elevado porque los datos inversos requieren una gran cantidad de intercambios.



Heapsort se aproximó al crecimiento esperado de O(n log n) al pasar de 2.000 a 4.000 elementos.



Las diferencias observadas muestran que los tiempos reales no dependen únicamente de la complejidad teórica, sino también de factores relacionados con el entorno de ejecución.



**Conclusión de la comprobación.**



Los resultados respaldan parcialmente las tendencias teóricas.



Los algoritmos cuadráticos presentan un crecimiento generalmente mayor cuando aumenta el tamaño de los datos desordenados.



Quicksort y Heapsort muestran un crecimiento más moderado, especialmente con datos aleatorios.



Sin embargo, las proporciones no siempre coinciden con los valores esperados. Esto demuestra la importancia de repetir las mediciones y considerar que la notación Big-O describe el crecimiento asintótico, no un tiempo exacto de ejecución.



4.3. ¿Por qué Quicksort suele superar a Heapsort si ambos son O(n log n)?



Quicksort suele ser más rápido en muchas implementaciones porque realiza particiones que favorecen el acceso a posiciones cercanas dentro del arreglo.



Esta característica permite aprovechar mejor la memoria caché del procesador y reducir ciertos costos de acceso a memoria.



Heapsort, en cambio, reorganiza constantemente el heap mediante operaciones entre padres e hijos, accediendo a posiciones que pueden encontrarse más separadas dentro del arreglo.



Además, Heapsort puede necesitar más comparaciones para mantener la propiedad del montículo.



Aunque ambos presentan complejidad O(n log n) en el caso promedio, sus operaciones internas y constantes de ejecución son diferentes.



Relación con los resultados obtenidos:



En este benchmark, Heapsort fue más rápido que Quicksort en las pruebas realizadas.



Esto no contradice la teoría, porque Quicksort no necesariamente supera a Heapsort en todas las implementaciones.



El rendimiento práctico también depende del lenguaje de programación, la estrategia de partición, la cantidad de operaciones y el entorno de ejecución.



La principal ventaja de Heapsort es que garantiza O(n log n) incluso en el peor caso, mientras que Quicksort puede alcanzar O(n²).



**5. Resultados y gráficos**



Los resultados experimentales se encuentran almacenados en el archivo "resultados.csv".



Este archivo incluye:

\- Orden inicial de los datos.

\- Tamaño del arreglo.

\- Algoritmo utilizado.

\- Tiempo mediano de ejecución.

\- Tiempo mínimo y máximo.

\- Cantidad de comparaciones.

\- Cantidad de movimientos.



Se generaron tres gráficos:



Gráfico 1: Datos aleatorios



grafico\_aleatorio.png



Gráfico 2: Datos ordenados



grafico\_ordenado.png



Gráfico 3: Datos inversos



grafico\_inverso.png



Los gráficos utilizan una escala logarítmica para facilitar la comparación de algoritmos con tiempos de ejecución muy diferentes.



**6. Conclusión**



La implementación del benchmark permitió comparar experimentalmente cinco algoritmos de ordenamiento y relacionar sus tiempos de ejecución con la complejidad teórica.



En las pruebas realizadas, Heapsort obtuvo los menores tiempos con datos aleatorios e inversos, mientras que Burbuja fue el más rápido cuando los datos estaban previamente ordenados.



Los algoritmos cuadráticos mostraron mayores tiempos al aumentar la cantidad de elementos desordenados, especialmente Inserción y Burbuja.



Quicksort y Heapsort presentaron un crecimiento generalmente más favorable, relacionado con su complejidad O(n log n) en los casos evaluados.



Los factores de crecimiento experimentales no siempre coincidieron exactamente con las proporciones teóricas, debido a las características de la implementación y a posibles variaciones del entorno de ejecución.



En conclusión, el rendimiento de un algoritmo depende no solamente de su complejidad, sino también del tamaño de entrada, el orden inicial de los datos y las condiciones en las que se ejecuta.



