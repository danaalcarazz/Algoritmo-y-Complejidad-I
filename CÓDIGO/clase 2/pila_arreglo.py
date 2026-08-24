class PilaArreglo:
    def __init__(self, capacidad_inicial=10):
        self.__capacidad = capacidad_inicial
        self.__datos = [None] * self.__capacidad
        self.__tope = -1

    def __redimensionar(self, nueva_capacidad):
        nuevos_datos = [None] * nueva_capacidad
        for i in range(self.__tope + 1):
            nuevos_datos[i] = self.__datos[i]
        self.__datos = nuevos_datos
        self.__capacidad = nueva_capacidad

    def apilar(self, elemento):
        if self.__tope + 1 == self.__capacidad:
            self.__redimensionar(self.__capacidad * 2)
        
        self.__tope += 1
        self.__datos[self.__tope] = elemento

    def desapilar(self):
        if self.estaVacia():
            raise Exception("No se puede desapilar una pila vacía")

        elemento = self.__datos[self.__tope]
        self.__datos[self.__tope] = None  # Limpia la referencia
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