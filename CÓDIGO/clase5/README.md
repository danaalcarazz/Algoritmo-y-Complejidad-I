**Clase 5 - Estructura de Pila y Cola**

Resolver un problema de pilas (stack) y uno de colas (queue) de la página LeetCode.





Ejercicios resueltos:



1\. Valid Parentheses (Pila / Stack)

Enlace del problema: https://leetcode.com/problems/valid-parentheses/ 

Descripción: Determina si una cadena de texto que contiene paréntesis ("()", "{}", "\[]") es válida, verificando que los pares se abran y cierren en el orden correcto utilizando el principio LIFO.



Complejidad:

* Tiempo: O(N) Se recorre la cadena una sola vez de izquierda a derecha.
* Espacio: O(N) En el peor de los casos, todos los caracteres son de apertura y se almacenan en la pila.
* Archivo de solución: pila.py





2\. Number of Recent Calls (Cola / Queue)

Enlace del problema: https://leetcode.com/problems/number-of-recent-calls/

Descripción: Implementa un contador de solicitudes recientes usando una ventana de tiempo de 3000 milisegundos. Se utiliza el principio FIFO (primero en entrar, primero en salir) para descartar eficientemente las peticiones antiguas que ya quedaron fuera del rango de tiempo.



Complejidad:

* Tiempo: O(1) en promedio por operación (cada elemento entra y sale de la cola una sola vez).
* Espacio: O(N) - Almacena únicamente las solicitudes activas dentro de la ventana de los últimos 3000ms.
* Archivo de solución: cola.py

