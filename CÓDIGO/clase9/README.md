**Clase 9 - Búsqueda Secuencial y Binaria**



Descripción:

Implementación de los algoritmos de búsqueda secuencial y binaria en Python, utilizando el arreglo `\[1, 3, 4, 6, 12, 15, 35, 44]` para localizar el número 12.



**1. Búsqueda Secuencial**

La búsqueda secuencial recorre los elementos de un arreglo uno por uno hasta encontrar el valor buscado o llegar al final.



Funcionamiento paso a paso:

1\. Índice 0: 1 ≠ 12.

2\. Índice 1: 3 ≠ 12.

3\. Índice 2: 4 ≠ 12.

4\. Índice 3: 6 ≠ 12.

5\. Índice 4: 12 = 12. Elemento encontrado.



Resultado: El número 12 se encuentra en el índice 4, después de 5 comparaciones.



Complejidad:

\- Mejor caso: O(1).

\- Caso promedio: O(n).

\- Peor caso: O(n).



**2. Búsqueda Binaria**

La búsqueda binaria divide repetidamente el intervalo de búsqueda en dos mitades. Requiere que el arreglo esté ordenado.



Funcionamiento paso a paso:

1\. Izquierda = 0, derecha = 7. Medio = 3, valor = 6. Como 12 > 6, se busca en la mitad derecha.

2\. Izquierda = 4, derecha = 7. Medio = 5, valor = 15. Como 12 < 15, se busca en la mitad izquierda del intervalo.

3\. Izquierda = 4, derecha = 4. Medio = 4, valor = 12. Elemento encontrado.



Resultado: El número 12 se encuentra en el índice 4, después de 3 comparaciones.



Complejidad:

\- Mejor caso: O(1).

\- Caso promedio: O(log n).

\- Peor caso: O(log n).



Ambos algoritmos encontraron correctamente el número 12 en el índice 4. La búsqueda secuencial realizó 5 comparaciones, mientras que la binaria necesitó solamente 3. Por lo tanto, la búsqueda binaria resulta más eficiente para arreglos ordenados, mientras que la secuencial es útil cuando los datos no están ordenados.

