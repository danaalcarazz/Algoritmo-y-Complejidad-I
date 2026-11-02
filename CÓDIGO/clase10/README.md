**Clase 10 - Algoritmos de Ordenamiento**



Descripción:

Implementación y comparación de dos algoritmos de ordenamiento: Insertion Sort (Inserción) y Counting Sort (Conteo).

Se utiliza el arreglo "\[35, 12, 44, 1, 15, 6, 3, 4]" para analizar su funcionamiento, complejidad, propiedades y casos de uso recomendados.



**1. Insertion Sort (Ordenamiento por Inserción)**

Insertion Sort es un algoritmo que ordena los elementos progresivamente, insertando cada valor en su posición correcta dentro de una sección previamente ordenada.



Funcionamiento:

1\. Se comienza desde el segundo elemento.

2\. Se compara con los elementos anteriores.

3\. Los elementos mayores se desplazan hacia la derecha.

4\. Se inserta el elemento en su posición correspondiente.

5\. Se repite hasta ordenar todo el arreglo.



Complejidad:

\- Mejor caso: O(n).

\- Caso promedio: O(n²).

\- Peor caso: O(n²).

\- Espacio auxiliar del algoritmo: O(1).



Propiedades:

\- Estabilidad: Estable, conserva el orden relativo de elementos iguales.

\- Adaptabilidad: Sí, es eficiente con datos casi ordenados.

\- In-place: Sí, el algoritmo base trabaja sin un arreglo auxiliar. La implementación utiliza una copia para conservar el original.



Casos de uso: Es recomendado para arreglos pequeños o que están parcialmente ordenados.



**2. Counting Sort (Ordenamiento por Conteo)**

Counting Sort es un algoritmo de ordenamiento que cuenta la frecuencia de aparición de cada valor y utiliza esos conteos para construir un arreglo ordenado.

A diferencia de los algoritmos basados en comparaciones, Counting Sort utiliza las frecuencias de los elementos para determinar su posición.



Funcionamiento:

1\. Se identifica el valor mínimo y máximo del arreglo.

2\. Se crea un arreglo auxiliar para almacenar las frecuencias.

3\. Se cuenta cuántas veces aparece cada número.

4\. Se recorren las frecuencias en orden ascendente.

5\. Se construye el arreglo ordenado según la cantidad de apariciones de cada valor.



Complejidad:

\- Mejor caso: O(n + k).

\- Caso promedio: O(n + k).

\- Peor caso: O(n + k).

\- Espacio auxiliar: O(n + k).



Donde "n" representa la cantidad de elementos y "k" el tamaño del rango de valores.



Propiedades:

\- Estabilidad: La implementación presentada no garantiza estabilidad para registros con claves repetidas; una variante con posiciones acumuladas puede ser estable.

\- Adaptabilidad: No, su funcionamiento no mejora por recibir datos previamente ordenados.

\- In-place: No, necesita arreglos auxiliares.

\- Tipo: Algoritmo no basado en comparaciones.



Casos de uso: Recomendado para ordenar números enteros cuando el rango de valores es relativamente pequeño.



**3. Comparación de algoritmos**

Insertion Sort:

\- Estrategia: Ordenamiento mediante comparaciones e inserciones.

\- Mejor caso: O(n).

\- Caso promedio: O(n²).

\- Peor caso: O(n²).

\- Estabilidad: Estable, conserva el orden relativo de elementos iguales.

\- Adaptabilidad: Sí, mejora su rendimiento cuando los datos están casi ordenados.

\- In-place: Sí, en su versión tradicional.

\- Espacio auxiliar: O(1) en el algoritmo base.

\- Uso recomendado: Arreglos pequeños o parcialmente ordenados.



Counting Sort:

\- Estrategia: Ordenamiento mediante conteo de frecuencias, sin comparaciones entre elementos.

\- Mejor caso: O(n + k).

\- Caso promedio: O(n + k).

\- Peor caso: O(n + k).

\- Estabilidad: No garantizada en la implementación utilizada; existen variantes estables.

\- Adaptabilidad: No, su rendimiento no mejora significativamente cuando los datos ya están ordenados.

\- In-place: No, utiliza memoria adicional.

\- Espacio auxiliar: O(k) en la implementación utilizada, donde k representa el tamaño del rango de valores.

\- Uso recomendado: Arreglos de números enteros con un rango de valores reducido.



Diferencia principal:

Insertion Sort ordena los elementos mediante comparaciones y desplazamientos, siendo adecuado para conjuntos pequeños o casi ordenados. En cambio, Counting Sort utiliza las frecuencias de los valores para construir el arreglo ordenado, ofreciendo una complejidad O(n + k), que puede resultar más eficiente cuando el rango de valores es pequeño. Sin embargo, Counting Sort requiere memoria adicional y está limitado a datos enteros o claves que puedan representarse mediante un rango discreto.



**4. Resultados**

Arreglo original:

"\[35, 12, 44, 1, 15, 6, 3, 4]"



Arreglo ordenado:

"\[1, 3, 4, 6, 12, 15, 35, 44]"



Ambos algoritmos producen el mismo resultado, aunque utilizan estrategias diferentes.



**5. Conclusión**



Insertion Sort es un algoritmo sencillo y adecuado para arreglos pequeños o parcialmente ordenados, pero su eficiencia disminuye cuando aumenta la cantidad de elementos desordenados.

Counting Sort puede resultar más eficiente cuando se trabaja con números enteros dentro de un rango reducido, ya que no necesita comparar los elementos entre sí. Sin embargo, requiere memoria adicional y no resulta conveniente cuando el rango de valores es demasiado grande.

Por lo tanto, la elección del algoritmo depende del tamaño del arreglo, las características de los datos y los recursos disponibles.

