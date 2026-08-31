**Clase 3 - Análisis de Algoritmos y Notación Asintótica**



Fragmento 1 - Acceso directo

* Descripción: Función que recibe una lista y devuelve su último elemento.
* Complejidad Big-O: O(1)
* Caso analizado: Peor caso/Caso promedio.
* Justificación: El último elemento se obtiene mediante un acceso directo por índice (lista\[-1]. No es necesario recorrer la lista, por lo que el tiempo de ejecución es constante.





Fragmento 2 - Búsqueda lineal

* Descripción: Función que recorre una lista desordenada elemento por elemento hasta encontrar el objetivo.
* Complejidad Big-O: O(n)
* Caso analizado: Peor caso.
* Justificación: El ciclo for recorre los elementos uno por uno hasta encontrar el objetivo. En el peor caso debe recorrer los n elementos por lo que la complejidad es O(n).





Fragmento 3 - Detección de duplicados

* Descripción: Función que compara los elementos de una lista mediante dos ciclos anidados para detectar duplicados.
* Complejidad Big-O: O(n²)
* Caso analizado: Peor caso.
* Justificación: Los dos ciclos for que se utilizó están anidados y realizan comparaciones entre los elementos de la lista. Por lo tanto, la cantidad de operaciones crece aproximadamente como n².





Fragmento 4 - División sucesiva

* Descripción: Función que divide sucesivamente un número entre 2 hasta que sea menor o igual a 1.
* Complejidad Big-O: O(log n)
* Caso analizado: Peor caso/Caso promedio.
* Justificación: El ciclo while utilizado divide el valor de n entre 2 en cada iteración. Al reducirse a la mitad sucesivamente, el número de iteraciones es logarítmico.





Fragmento 5 - Búsqueda binaria

* Descripción: Algoritmo que busca un elemento en una lista previamente ordenada dividiendo el espacio de búsqueda a la mitad.
* Complejidad Big-O: O(log n)
* Caso analizado: Peor caso.
* Justificación: Con el ciclo while se reduce aprox. a la mitad el espacio de búsqueda en cada iteración. Por ello, la cantidad de iteraciones crece logarítmicamente.





Fragmento 6 - Fibonacci ineficiente

* Descripción: Función recursiva que calcula Fibonacci realizando llamadas para n-1 y n-2.
* Complejidad Big-O: O(2ⁿ)
* Caso analizado: Peor caso/Caso promedio.
* Justificación: Cada llamada genera dos nuevas llamadas recursivas, produciendo un crecimiento exponencial y la cantidad de llamadas aumenta aprox. como 2ⁿ.





Fragmento 7 - Iteración anidada con saltos

* Descripción: Función con un ciclo externo de n iteraciones y un ciclo interno que duplica su variable de control.
* Complejidad Big-O: O(n log n)
* Caso analizado: Peor caso/Caso promedio.
* Justificación: El ciclo externo se ejecuta n veces y el interno duplica j, realizando O(log n) iteraciones, al estar anidados, se multiplican siendo O(n log n)





Fragmento 8 - Procesamiento de múltiples conjuntos

* Descripción: Función que recorre primero una lista de tamaño N y luego otra de tamaño M.
* Complejidad Big-O: O(N + M)
* Caso analizado: Peor caso/Caso promedio.
* Justificación: Los dos ciclos se ejecutan de manera secuencial, uno recorre n elementos y otro m elementos, al no estar anidados sus costos se suman siendo O(N + M).

