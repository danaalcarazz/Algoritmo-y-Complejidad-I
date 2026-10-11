**Clase 7 - Árboles Balanceados**



1\. Inserción y Rebalanceo en Árboles AVL

2\. Implementación Programada de un Árbol AVL



**Actividad 1:** Simulaciones de Inserción y Rebalanceo.

Convención aplicada: FE = Altura Derecho - Altura Izquierdo.



**Secuencia 1:** \[10, 20, 30, 40, 50, 25]



1\. Insertar 10

&#x20;  - Paso A: Árbol: 10 (FE: 0)

&#x20;  - Paso B: Balanceado (No requiere rotación).

&#x20;  - Paso C: Árbol final: 10 (FE: 0)



2\. Insertar 20

&#x20;  - Paso A: 

&#x20;    10 (FE: +1)

&#x20;      \\

&#x20;       20 (FE: 0)

&#x20;  - Paso B: Balanceado (No requiere rotación).

&#x20;  - Paso C: Árbol final: 10 (FE: +1), 20 (FE: 0)



3\. Insertar 30

&#x20;  - Paso A: 

&#x20;    10 (FE: +2)

&#x20;      \\

&#x20;       20 (FE: +1)

&#x20;         \\

&#x20;          30 (FE: 0)

&#x20;  - Paso B: Rotación Simple a la Izquierda (RR) en el nodo 10.

&#x20;  - Paso C: Árbol final:

&#x20;         20 (FE: 0)

&#x20;        /   \\

&#x20;    10 (0)   30 (0)



4\. Insertar 40

&#x20;  - Paso A: 

&#x20;         20 (FE: +1)

&#x20;        /   \\

&#x20;    10 (0)   30 (FE: +1)

&#x20;               \\

&#x20;                40 (FE: 0)

&#x20;  - Paso B: Balanceado (No requiere rotación).

&#x20;  - Paso C: Árbol final: 20 (FE: +1), 10 (FE: 0), 30 (FE: +1), 40 (FE: 0)



5\. Insertar 50

&#x20;  - Paso A: 

&#x20;        20 (FE: +2)

&#x20;       /   \\

&#x20;   10 (0)   30 (FE: +2)

&#x20;              \\

&#x20;               40 (FE: +1)

&#x20;                 \\

&#x20;                  50 (FE: 0)

&#x20;  - Paso B: Rotación Simple a la Izquierda (RR) en el nodo 30.

&#x20;  - Paso C: Árbol final:

&#x20;        20 (FE: +1)

&#x20;       /   \\

&#x20;   10 (0)   40 (FE: 0)

&#x20;            /   \\

&#x20;        30 (0)   50 (0)



6\. Insertar 25

&#x20;  - Paso A:

&#x20;        20 (FE: +2)

&#x20;       /   \\

&#x20;   10 (0)   40 (FE: -1)

&#x20;            /   \\

&#x20;        30 (-1)  50 (0)

&#x20;        /

&#x20;       25 (0)

&#x20;  - Paso B: Rotación Doble RL (Derecha-Izquierda) en el nodo 20.

&#x20;  - Paso C: Árbol final:

&#x20;          30 (FE: 0)

&#x20;         /          \\

&#x20;    20 (FE: 0)     40 (FE: +1)

&#x20;    /     \\              \\

10 (FE: 0) 25 (FE: 0)   50 (FE: 0)





**Secuencia 2:** \[30, 10, 40, 20, 15, 35]



1\. Insertar 30

&#x20;  - Paso A: 30 (FE: 0)

&#x20;  - Paso B: Balanceado.

&#x20;  - Paso C: 30 (FE: 0)



2\. Insertar 10

&#x20;  - Paso A: 30 (FE: -1) con hijo izquierdo 10 (FE: 0).

&#x20;  - Paso B: Balanceado.

&#x20;  - Paso C: 30 (FE: -1), 10 (FE: 0)



3\. Insertar 40

&#x20;  - Paso A: 

&#x20;        30 (FE: 0)

&#x20;       /   \\

&#x20;   10 (0)   40 (0)

&#x20;  - Paso B: Balanceado.

&#x20;  - Paso C: Raíz 30 (FE: 0) con hijos 10 (0) y 40 (0).



4\. Insertar 20

&#x20;  - Paso A: 

&#x20;        30 (FE: -1)

&#x20;       /       \\

&#x20;   10 (FE: +1)  40 (0)

&#x20;       \\

&#x20;        20 (0)

&#x20;  - Paso B: Balanceado (no requiere rotación).

&#x20;  - Paso C: 

&#x20;        30 (FE: -1)

&#x20;       /           \\

&#x20; 10 (FE: +1)     40 (FE: 0)

&#x20;       \\

&#x20;       20 (FE: 0)



5\. Insertar 15

&#x20;  - Paso A:

&#x20;        30 (FE: -2)

&#x20;       /           \\

&#x20;   10 (FE: +2)     40 (FE: 0)

&#x20;       \\

&#x20;        20 (FE: -1)

&#x20;        /

&#x20;     15 (FE: 0)

&#x20;  - Paso B: Rotación Doble LR en el nodo 10.

&#x20;  - Paso C: Árbol final:

&#x20;        30 (FE: -1)

&#x20;       /           \\

&#x20;   15 (FE: 0)     40 (FE: 0)

&#x20;   /     \\

&#x20;  10 (0)  20 (0)



6\. Insertar 35

&#x20;  - Paso A: Inserción como hijo izquierdo de 40.

&#x20;  - Paso B: Balanceado (no requiere rotación).

&#x20;  - Paso C: Árbol final:

&#x20;        30 (FE: 0)

&#x20;       /          \\

&#x20;   15 (FE: 0)     40 (FE: -1)

&#x20;   /     \\         /

&#x20;  10 (0) 20 (0)  35 (0)



**Secuencia 3:** \[50, 40, 30, 20, 10, 25]



1\. Insertar 50

&#x20;  - Paso A: 50 (FE: 0)

&#x20;  - Paso B: Balanceado.

&#x20;  - Paso C: 50 (FE: 0)



2\. Insertar 40

&#x20;  - Paso A: 50 (FE: -1) con hijo izquierdo 40 (0).

&#x20;  - Paso B: Balanceado.

&#x20;  - Paso C: 50, 40.



3\. Insertar 30

&#x20;  - Paso A: Desbalance en 50 (FE: -2).

&#x20;  - Paso B: Rotación Simple a la Derecha (LL) en el nodo 50.

&#x20;  - Paso C:

&#x20;       40 (FE: 0)

&#x20;      /   \\

&#x20;    30(0)  50(0)



4\. Insertar 20

&#x20;  - Paso A: Inserción a la izquierda de 30.

&#x20;  - Paso B: Balanceado.

&#x20;  - Paso C: Raíz 40 (FE: -1), hijo izquierdo 30 (FE: -1) (con 20), hijo derecho 50 (FE: 0).



5\. Insertar 10

&#x20;  - Paso A: Desbalance (FE: -2 en nodo 30).

&#x20;  - Paso B: Rotación Simple a la Derecha (LL) en el nodo 30.

&#x20;  - Paso C: 

&#x20;        40 (FE: -1)

&#x20;       /           \\

&#x20;   20 (FE: 0)      50 (FE: 0)

&#x20;   /       \\

10 (FE: 0)  30 (FE: 0)



6\. Insertar 25

&#x20;  - Paso A: Inserción que genera desbalance.

&#x20;  - Paso B: Rotación Doble LR en el nodo 40.

&#x20;  - Paso C: 

&#x20;        30 (FE: 0)

&#x20;       /          \\

&#x20;   20 (FE: 0)     40 (FE: +1)

&#x20;   /     \\               \\

&#x20;  10 (0)  25 (0)         50 (0)





**Actividad 2:** Implementación en Python



El archivo "avl.py" incluido en esta carpeta contiene la estructura completa del Árbol AVL que cumple con todos los requerimientos técnicos. 

