**Clase 4 — Análisis de Algoritmos Recursivos**



1. Resolución de ecuaciones de recurrencia



* Ecuación 1

Recurrencia: T(n) = 2T(n/2) + O(1)

Método: método maestro.



Valores

\* a = 2

\* b = 2

\* d = 0



Calculamos:

log₂(2) = 1



como 0 < 1 corresponde al caso 1.



Resultado:

T(n) = Θ(n)



Justificación:

La recurrencia genera dos subproblemas de tamaño n/2 y realiza un trabajo constante adicional. Como el trabajo adicional crece más lentamente que las llamadas recursivas, estas últimas dominan el costo.



Complejidad: Θ(n)





* Ecuación 2

Recurrencia: T(n) = 4T(n/2) + O(1)

Método: método maestro.



Valores:

\* a = 4

\* b = 2

\* d = 0



Calculamos:

log₂(4) = 2



como 0 < 2 corresponde al caso 1.



Resultado:

T(n) = Θ(n²)



Justificación:

En cada llamada se generan cuatro subproblemas de tamaño n/2. El costo de las llamadas recursivas crece más rápidamente que el trabajo constante realizado en cada llamada.



Complejidad: Θ(n²)





* Ecuación 3

Recurrencia: T(n) = 2T(n/2) + O(n²)

Método: método maestro.



Valores:

\* a = 2

\* b = 2

\* d = 2



Calculamos:

log₂(2) = 1



como: 2 > 1 corresponde al caso 3.



Resultado:

T(n) = Θ(n²)



Justificación:

El trabajo adicional O(n²) crece más rápidamente que el costo de las llamadas recursivas, por lo que el término dominante es n².



Complejidad: Θ(n²)





* Ecuación 4

Recurrencia: T(n) = T(n-1) + O(1)

Método: árbol de recursión.



No se utiliza el método maestro porque la recurrencia reduce el problema mediante n-1 y no mediante n/b por lo tanto, no tiene la forma requerida por el método maestro.



Desarrollo:

T(n) = T(n-1) + O(1)



T(n-1) = T(n-2) + O(1)



T(n) = T(n-2) + 2O(1)



T(n) = T(n-k) + kO(1)

y así sucesivamente...



La recursión termina cuando n-k = 1, por lo que existen aproximadamente n niveles.



Resultado:

T(n) = Θ(n)



Justificación:

El problema disminuye de uno en uno y cada llamada realiza un trabajo constante. Como se realizan aproximadamente n llamadas, el costo total es lineal.



Complejidad: Θ(n)





* Ecuación 5

Recurrencia: T(n) = T(n/3) + T(2n/3) + O(1)

Método: árbol de recursión.



Los subproblemas tienen tamaños diferentes: uno es n/3 y el otro 2n/3. Por esta razón, no se puede aplicar directamente el método maestro en su forma estándar.



Desarrollo:

Cada llamada realiza un trabajo constante O(1).

En el nivel 0 hay 1 nodo con trabajo O(1).

En el nivel 1 hay 2 nodos con trabajo 2·O(1).

En el nivel k hay 2^k nodos.



La rama más corta termina a una profundidad log₃(n) y la más larga a log₃/₂(n).



Dado que el trabajo por nodo es constante, el costo total está dominado por el nivel de las hojas. La cantidad total de hojas en este árbol de división es proporcional a n.



Multiplicando el número total de hojas por el costo constante de cada una, el trabajo total es lineal.



Resultado:

T(n) = Θ(n)



Justificación:

Cada división genera dos llamadas recursivas y realiza un trabajo constante O(1). Como el número total de nodos que llegan al caso base es lineal, el costo total de la recurrencia resulta Θ(n).



Complejidad: Θ(n)





* Ecuación 6

Recurrencia: T(n) = 3T(n/4) + O(n²)

Método: método maestro.



Valores

\* a = 3

\* b = 4

\* d = 2



Calculamos:

log₄(3) ≈ 0,792



como 2 > 0,792 corresponde al caso 3.



Resultado:

T(n) = Θ(n²)



Justificación:

El trabajo adicional O(n²) crece más rápidamente que el costo generado por las llamadas recursivas. Por lo tanto, el término dominante es n².



Complejidad: Θ(n²)







2\. Investigación — Divide y Vencerás



Algoritmo: Mergesort.

Mergesort es un algoritmo de ordenamiento que utiliza el paradigma Divide y Vencerás. El algoritmo divide el arreglo en dos mitades, ordena cada mitad de forma recursiva y finalmente combina ambas partes ordenadas.



Su funcionamiento puede resumirse en tres etapas:

1. Divide: toma el arreglo de tamaño n y lo corta por la mitad en dos subarreglos de tamaño n/2.
2. Vence: ordena recursivamente cada uno de los dos subarreglos aplicando el mismo procedimiento. El caso base ocurre cuando el subarreglo tiene 1 solo elemento, es decir q ya está ordenado por definición.
3. Combina: une los resultados para obtener la solución final.





\- Ejemplo

Tenemos el siguiente arreglo:



\[8, 3, 5, 4, 7, 6, 1, 2]



Primero se divide en dos partes:



\[8, 3, 5, 4] y \[7, 6, 1, 2]



Luego cada parte continúa dividiéndose hasta obtener elementos individuales.

\[8, 3], \[5, 4], \[7, 6], \[1,2]



\[8], \[3], \[5], \[4], \[7], \[6], \[1], \[2]



Finalmente, los elementos se combinan de manera ordenada hasta obtener:



\[1, 2, 3, 4, 5, 6, 7, 8]





\- Recurrencia de Mergesort

Mergesort realiza:

\* 2 llamadas recursivas.

\* Cada llamada trabaja con aproximadamente n/2 elementos.

\* La combinación de las dos partes cuesta O(n).



Por lo tanto, su ecuación de recurrencia es:

T(n) = 2T(n/2) + O(n)



Valores:

\* a = 2

\* b = 2

\* d = 1



Calculamos:

log₂(2) = 1



como d = log₂(2) corresponde al caso 2 del método maestro.



por lo tanto: T(n) = O(n log n)



La complejidad de Mergesort es:

Θ(n log n)





\- Implementación en Python

El código del algoritmo se encuentra en:

mergesort.py



El programa implementa mergesort de manera recursiva y muestra el arreglo original y el arreglo ordenado.





\- Análisis del código

La función merge\_sort() contiene el caso base:

if len(arr) <= 1:

&#x20;   return arr



Cuando el arreglo tiene uno o ningún elemento, ya se encuentra ordenado.



Sino, se calcula el punto medio y se divide el arreglo en dos partes. Cada mitad se ordena mediante una nueva llamada recursiva. Finalmente, la función merge() combina ambas mitades ordenadas.



La división genera dos llamadas "2T(n/2)" y la combinación necesita recorrer los elementos "O(n)"



Por eso:

T(n) = 2T(n/2) + O(n)



y:



T(n) = Θ(n log n)





\- Complejidad

Complejidad temporal: Θ(n log n)



Mergesort mantiene este orden de crecimiento porque el arreglo se divide aproximadamente en dos en cada nivel y la combinación de cada nivel requiere recorrer los elementos.



Complejidad espacial: O(n)



Se necesita espacio adicional para realizar la combinación de los subarreglos.

