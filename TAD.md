	1. TAD Fracción
Dominio: pares ordenados (numerador, denominador) de números enteros, con denominador ≠ 0.

Operaciones:

crear(n: Entero, d: Entero) -> Fracción
  Precondición: d ≠ 0
  Postcondición: el resultado representa la fracción n/d.

numerador(f: Fracción) -> Entero
  Precondición: f es una Fracción válida.
  Postcondición: devuelve el numerador de f, sin modificar f.

denominador(f: Fracción) -> Entero
  Precondición: f es una Fracción válida.
  Postcondición: devuelve el denominador de f, sin modificar f.

sumar(f1: Fracción, f2: Fracción) -> Fracción
  Precondición: f1 y f2 son Fracciones válidas.
  Postcondición: el resultado representa la suma matemática de f1 y f2, expresada como una nueva Fracción.

simplificar(f1: Fracción) -> Fracción
  Precondición: f es una Fracción válida.
  Postcondición: el resultado es equivalente a f, con numerador y denominador coprimos.

restar(f1: Fracción, f2: Fracción) -> Fracción
  Precondición: f1 y f2 son Fracciones válidas.
  Postcondición: el resultado representa la resta matemática de f1 y f2, expresada como una nueva Fracción.

multiplicar(f1: Fracción, f2: Fracción) -> Fracción
  Precondición: f1 y f2 son Fracciones válidas.
  Postcondición: el resultado representa la multiplicación matemática de f1 y f2, expresada como una nueva Fracción.

sonIguales(f1: Fracción, f2: Fracción) -> Booleano
  Precondición: f1 y f2 son Fracciones válidas.
  Postcondición: devuelve Verdadero si f1 y f2 representan el mismo valor racional, aunque sus numeradores y denominadores sean diferentes o no estén simplificados, de no ser así, devuelve Falso.

	2. TAD Punto2D
Dominio: pares ordenados (x, y) de números reales que representan las coordenadas de un punto en el plano cartesiano.

Operaciones:

crear(x: Real, y: Real) -> Punto2D
  Precondición: x e y son números reales.
  Postcondición: el resultado es un Punto2D cuyas coordenadas son x e y.

coordenadaX(p: Punto2D) -> Real
  Precondición: p es un Punto2D válido.
  Postcondición: devuelve la coordenada x de p sin modificar p.


coordenadaY(p: Punto2D) -> Real
  Precondición: p es un Punto2D válido.
  Postcondición: devuelve la coordenada y de p sin modificar p.

distancia(p1: Punto2D, p2: Punto2D) -> Real
  Precondición: p1 y p2 son Puntos2D válidos.
  Postcondición: devuelve la distancia euclidiana entre p1 y p2.

trasladar(p: Punto2D, dx: Real, dy: Real) -> Punto2D
  Precondición: p es un Punto2D válido.
  Postcondición: el resultado es un nuevo Punto2D cuyas coordenadas son (x+dx, y+dy), donde (x, y) son las coordenadas de p, el punto original p no se modifica.
