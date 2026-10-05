**Clase 6 - Árboles Binarios de Búsqueda**



Parte A - Implementación de un ABB

Se implementó un Árbol Binario de Búsqueda utilizando Programación Orientada a Objetos en Python.

La implementación contiene una clase NodoArbol, encargada de almacenar el dato y las referencias al hijo izquierdo y al hijo derecho.



También se implementaron las siguientes operaciones:

\- insertar

\- buscar

\- eliminar



La eliminación tiene los tres casos:

1\. Nodo sin hijos.

2\. Nodo con un solo hijo.

3\. Nodo con dos hijos.



Para probar el funcionamiento se utilizaron 15 valores.



Parte B - Recorridos

Se implementaron los cuatro recorridos de un árbol binario:

\- preorden

\- inorden

\- postorden

\- por niveles



El recorrido inorden permite comprobar que los valores de un ABB se obtienen en orden ascendente.



Pruebas realizadas

Se probaron búsquedas de valores presentes y ausentes.



También se realizaron eliminaciones correspondientes a los tres casos:



\- 10: nodo sin hijos.

\- 20: nodo con un solo hijo.

\- 30: nodo con dos hijos.



Parte C - LeetCode

Search in a Binary Search Tree



Link:

https://leetcode.com/problems/search-in-a-binary-search-tree/



Se implementó una solución recursiva para buscar un valor dentro de un Árbol Binario de Búsqueda.



La solución utiliza la propiedad del ABB para decidir si la búsqueda debe continuar por el subárbol izquierdo o por el subárbol derecho.



Complejidad

\- Mejor caso: O(1)

\- Caso promedio: O(log n)

\- Peor caso: O(n)



Conclusión

La implementación permitió aplicar los conceptos de árboles binarios de búsqueda, inserción, búsqueda, eliminación y recorridos. También se comprobó que la eficiencia de las operaciones depende de la altura del árbol y de su nivel de equilibrio.

