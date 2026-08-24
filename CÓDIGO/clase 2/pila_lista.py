class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaLista:
    def __init__(self):
        self.__tope = None
        self.__tamaño = 0

    def apilar(self, elemento):
        nuevo_nodo = Nodo(elemento)

        nuevo_nodo.siguiente = self.__tope
        self.__tope = nuevo_nodo

        self.__tamaño += 1

    def desapilar(self):
        if self.estaVacia():
            raise Exception("No se puede desapilar una pila vacía")

        elemento = self.__tope.dato

        self.__tope = self.__tope.siguiente
        self.__tamaño -= 1

        return elemento

    def cima(self):
        if self.estaVacia():
            raise Exception("No se puede consultar la cima de una pila vacía")

        return self.__tope.dato

    def estaVacia(self):
        return self.__tope is None

    def tamaño(self):
        return self.__tamaño