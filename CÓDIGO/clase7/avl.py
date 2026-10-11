class NodoAVL:
    def __init__(self, key):
        self.key = key
        self.height = 1  #una hoja nueva tiene altura 1 por convención
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        #retorna la altura de un nodo (0 si es nulo)
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        #calcula el factor de equilibrio (FE = Altura Derecho - Altura Izquierdo)
        if not node:
            return 0
        return self.height(node.right) - self.height(node.left)

    def update_height(self, node):
        #actualiza la altura del nodo basándose en sus hijos
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotar_derecha(self, z):
        #rotación simple a la derecha (caso LL)
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        self.update_height(z)
        self.update_height(y)
        
        return y

    def rotar_izquierda(self, z):
        #rotación simple a la izquierda (caso RR)
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)
        
        return y

    def insertar(self, nodo, key):
        #1. inserción normal de un ABB (BST)
        if not nodo:
            return NodoAVL(key)
        
        if key < nodo.key:
            nodo.left = self.insertar(nodo.left, key)
        elif key > nodo.key:
            nodo.right = self.insertar(nodo.right, key)
        else:
            return nodo  #no se permiten duplicados

        #2. actualizar altura y calcular el factor de equilibrio
        self.update_height(nodo)
        fb = self.get_balance(nodo)

        #3. rebalancear si el nodo se desbalancea (FE = +2 o -2)
        
        #si FE < -1 (pesado a la izquierda)
        if fb < -1:
            if self.get_balance(nodo.left) <= 0:
                return self.rotar_derecha(nodo)  #caso LL
            else:
                nodo.left = self.rotar_izquierda(nodo.left)
                return self.rotar_derecha(nodo)  #caso LR

        #si FE > 1 (pesado a la derecha)
        if fb > 1:
            if self.get_balance(nodo.right) >= 0:
                return self.rotar_izquierda(nodo)  #caso RR
            else:
                nodo.right = self.rotar_derecha(nodo.right)
                return self.rotar_izquierda(nodo)  #caso RL

        return nodo

    def add(self, key):
        #método público para insertar una clave en el árbol
        self.root = self.insertar(self.root, key)

    def recorrido_preorden(self, nodo, resultado):
        #recorrido preorden para visualizar claves y sus FE
        if nodo:
            resultado.append(f"Clave: {nodo.key} (FE: {self.get_balance(nodo)})")
            self.recorrido_preorden(nodo.left, resultado)
            self.recorrido_preorden(nodo.right, resultado)


if __name__ == "__main__":
    avl = AVLTree()
    secuencia = [10, 20, 30, 40, 50, 25]
    
    print("Insertando elementos en el Árbol AVL...")
    for val in secuencia:
        avl.add(val)
        
    print("\nEstado final del árbol (Recorrido Preorden con Factores de Equilibrio):")
    res = []
    avl.recorrido_preorden(avl.root, res)
    for item in res:
        print(f" - {item}")