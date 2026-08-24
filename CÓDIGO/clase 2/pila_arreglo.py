from array import array

class PilaArreglo:
    def __init__(self):
        self.__datos = array('i')
        self.__tope = -1

    def apilar(self, elemento):
        self.__datos.append(elemento)
        self.__tope += 1

    def desapilar(self):
        if self.estaVacia():
            raise Exception("No se puede desapilar una pila vacía")

        elemento = self.__datos[self.__tope]
        self.__datos.pop()
        self.__tope -= 1

        return elemento

    def cima(self):
        if self.estaVacia():
            raise Exception("No se puede consultar la cima de una pila vacía")

        return self.__datos[self.__tope]

    def estaVacia(self):
        return self.__tope == -1

    def tamaño(self):
        return self.__tope + 1