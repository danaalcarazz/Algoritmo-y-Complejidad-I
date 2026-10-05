class NodoArbol:
    def __init__(self, dato):
        #cada nodo guarda un dato y dos posibles hijos
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        #al comenzar, el árbol está vacío
        self.raiz = None

    def insertar(self, dato):
        #inserta un dato manteniendo el orden del ABB
        self.raiz = self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        #si no existe nodo, se crea uno nuevo
        if nodo is None:
            return NodoArbol(dato)

        #los valores menores van a la izquierda
        if dato < nodo.dato:
            nodo.izquierdo = self._insertar(nodo.izquierdo, dato)

        #los valores mayores van a la derecha
        elif dato > nodo.dato:
            nodo.derecho = self._insertar(nodo.derecho, dato)

        #se ignoran los valores repetidos
        return nodo

    def buscar(self, dato):
        #inicia la búsqueda desde la raíz
        return self._buscar(self.raiz, dato)

    def _buscar(self, nodo, dato):
        #si llegamos a un espacio vacío, el dato no existe
        if nodo is None:
            return None

        #si encontramos el dato, devolvemos el nodo
        if dato == nodo.dato:
            return nodo

        #si el dato es menor, buscamos en el lado izquierdo
        if dato < nodo.dato:
            return self._buscar(nodo.izquierdo, dato)

        #si es mayor, buscamos en el lado derecho
        return self._buscar(nodo.derecho, dato)

    def eliminar(self, dato):
        #inicia la eliminación desde la raíz
        self.raiz = self._eliminar(self.raiz, dato)

    def _eliminar(self, nodo, dato):
        #si el dato no existe, no se realiza ningún cambio
        if nodo is None:
            return None

        #buscamos el dato en el subárbol izquierdo
        if dato < nodo.dato:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, dato)

        #buscamos el dato en el subárbol derecho
        elif dato > nodo.dato:
            nodo.derecho = self._eliminar(nodo.derecho, dato)

        else:
            #caso 1 el nodo no tiene hijos
            if nodo.izquierdo is None and nodo.derecho is None:
                return None

            #caso 2 el nodo tiene solamente hijo derecho
            if nodo.izquierdo is None:
                return nodo.derecho

            #caso 2 el nodo tiene solamente hijo izquierdo
            if nodo.derecho is None:
                return nodo.izquierdo

            #caso 3 el nodo tiene dos hijos
            #se busca el menor valor del subárbol derecho
            sucesor = self._encontrar_minimo(nodo.derecho)

            #reemplazamos el dato por el sucesor
            nodo.dato = sucesor.dato

            #eliminamos el nodo que usamos como sucesor
            nodo.derecho = self._eliminar(nodo.derecho, sucesor.dato)

        return nodo

    def _encontrar_minimo(self, nodo):
        #comenzar desde el nodo recibido
        actual = nodo

        #el menor valor siempre está lo más a la izquierda posible
        while actual.izquierdo is not None:
            actual = actual.izquierdo

        return actual

    def preorden(self):
        #preorden raíz, izquierdo, derecho
        elementos = []
        self._preorden(self.raiz, elementos)
        return elementos

    def _preorden(self, nodo, elementos):
        if nodo is not None:
            #primero se visita la raíz
            elementos.append(nodo.dato)

            #después el subárbol izquierdo
            self._preorden(nodo.izquierdo, elementos)

            #finalmente el subárbol derecho
            self._preorden(nodo.derecho, elementos)

    def inorden(self):
        #inorden izquierdo, raíz, derecho
        elementos = []
        self._inorden(self.raiz, elementos)
        return elementos

    def _inorden(self, nodo, elementos):
        if nodo is not None:
            #primero se visita el subárbol izquierdo
            self._inorden(nodo.izquierdo, elementos)

            #después se visita la raíz
            elementos.append(nodo.dato)

            #finalmente el subárbol derecho
            self._inorden(nodo.derecho, elementos)

    def postorden(self):
        #postorden izquierdo, derecho, raíz
        elementos = []
        self._postorden(self.raiz, elementos)
        return elementos

    def _postorden(self, nodo, elementos):
        if nodo is not None:
            #primero se visita el subárbol izquierdo
            self._postorden(nodo.izquierdo, elementos)

            #después el subárbol derecho
            self._postorden(nodo.derecho, elementos)

            #al final se visita la raíz
            elementos.append(nodo.dato)

    def por_niveles(self):
        #si el árbol está vacío, devuelve una lista vacía
        if self.raiz is None:
            return []

        elementos = []

        #la cola comienza con la raíz
        cola = [self.raiz]

        while cola:
            #se toma el primer nodo de la cola
            actual = cola.pop(0)
            elementos.append(actual.dato)

            #se agregan los hijos a la cola
            if actual.izquierdo is not None:
                cola.append(actual.izquierdo)

            if actual.derecho is not None:
                cola.append(actual.derecho)

        return elementos


if __name__ == "__main__":
    #crear un árbol vacío
    arbol = ArbolBinarioBusqueda()

    valores = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90]

    #insertar los 15 valores
    for valor in valores:
        arbol.insertar(valor)

    #mostrar los cuatro recorridos del árbol
    print("Recorridos.")
    print("Preorden:", arbol.preorden())
    print("Inorden:", arbol.inorden())
    print("Postorden:", arbol.postorden())
    print("Por niveles:", arbol.por_niveles())

    print("\nBúsqueda:")

    #comprobar una búsqueda que sí existe
    if arbol.buscar(65) is not None:
        print("65 se encuentra en el árbol.")
    else:
        print("65 no se encuentra en el árbol.")

    #comprobar una búsqueda que no existe
    if arbol.buscar(100) is not None:
        print("100 se encuentra en el árbol.")
    else:
        print("100 no se encuentra en el árbol.")

    print("\nEliminación:")

    #probar eliminar un nodo sin hijos
    print("Eliminando 10: nodo sin hijos.")
    arbol.eliminar(10)

    #probar eliminar un nodo con un hijo
    print("Eliminando 20: nodo con un hijo.")
    arbol.eliminar(20)

    #probar eliminar un nodo con dos hijos
    print("Eliminando 30: nodo con dos hijos.")
    arbol.eliminar(30)

    #comprobar el árbol después de las eliminaciones
    print("\nInorden después de las eliminaciones")
    print(arbol.inorden())