**Clase 8 - Priority Queues y Hash Tables**



Actividad:

Elegir un ejercicio de Leetcode relacionado a priority queues y uno de hash tables y resolverlos, subiendo la solución a GitHub, con un enlace al desafio de Leetcode.





**Ejercicio 1** Last Stone Weight



**- Estructura:** Priority Queue

**- Dificultad:** Fácil

**- Enlace:** https://leetcode.com/problems/last-stone-weight/

**- Archivo:** "priority\_queue.py"



Descripción: El ejercicio consiste en procesar una lista de piedras con diferentes pesos, seleccionando las dos más pesadas en cada operación hasta obtener el peso de la última piedra restante.

Solución: Se implementó una cola de prioridad utilizando la biblioteca "heapq" de Python, permitiendo extraer las piedras de mayor peso y calcular sus diferencias.



Complejidad temporal: O(n log n).



Complejidad espacial: O(n).



**Ejercicio 2** Two Sum



**- Estructura:** Hash Table

**- Dificultad:** Fácil

**- Enlace:** https://leetcode.com/problems/two-sum/

**- Archivo:** "hash\_table.py"



Descripción: El ejercicio consiste en encontrar los índices de dos números de una lista cuya suma sea igual a un valor objetivo.

Solución: Se utilizó un diccionario de Python para almacenar los números recorridos y sus posiciones, permitiendo buscar el complemento de cada número de manera eficiente.



