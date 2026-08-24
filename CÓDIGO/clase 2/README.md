**TAD Pila**

En este trabajo se implementa el Tipo Abstracto de Dato (TAD) Pila en Python utilizando dos representaciones diferentes:



1\. Arreglo dinámico.

2\. Lista enlazada.



La Pila trabaja bajo el principio LIFO (Last In, First Out), donde el último elemento que ingresa es el primero en salir.



* Operaciones implementadas

Las dos implementaciones cuentan con las siguientes operaciones:



\- apilar(elemento): agrega un elemento en el tope de la pila.

\- desapilar(): elimina y devuelve el elemento que se encuentra en el tope.

\- cima(): devuelve el elemento del tope sin eliminarlo.

\- estaVacia(): indica si la pila no contiene elementos.

\- tamaño(): devuelve la cantidad de elementos de la pila.



La creación de cada pila se realiza mediante el constructor de la clase.



* Implementación mediante arreglo dinámico

La clase PilaArreglo representa la pila utilizando un arreglo dinámico.



La estructura posee dos atributos internos:

\- \_\_datos: almacena los elementos de la pila.

\- \_\_tope: indica la posición del último elemento almacenado.



Cuando la pila está vacía, el valor de \_\_tope es -1.

Al realizar apilar(), el elemento se agrega al arreglo y se actualiza el índice del tope.

Al realizar desapilar(), se obtiene el elemento ubicado en el tope, se elimina del arreglo y se actualiza el índice.



* Implementación mediante lista enlazada

La clase PilaLista representa la pila mediante nodos enlazados.



Cada nodo contiene:

\- dato: elemento almacenado.

\- siguiente: referencia al siguiente nodo.



La pila mantiene una referencia llamada \_\_tope, que apunta al primer nodo de la estructura.

Al realizar apilar(), se crea un nuevo nodo y se coloca como nuevo tope.

Al realizar desapilar(), se elimina el nodo que se encuentra en el tope y se actualiza la referencia.



* Manejo de errores



Las operaciones desapilar() y cima() requieren que la pila no esté vacía.

Si se intenta ejecutar alguna de estas operaciones sobre una pila vacía, se lanza una excepción con un mensaje descriptivo:

"No se puede desapilar una pila vacía" o "No se puede consultar la cima de una pila vacía"

De esta manera, las violaciones de precondiciones son manejadas explícitamente.



* Programa de pruebas



El archivo main.py contiene las pruebas de ambas implementaciones.

Se utilizan los valores: 1, 2, 3

Los elementos se apilan en ese orden y luego se desapilan.

El resultado esperado al desapilar es: 3, 2, 1

Esto permite comprobar el comportamiento LIFO de la Pila.



También se comparan los resultados obtenidos por ambas implementaciones para verificar que proporcionan el mismo comportamiento.

