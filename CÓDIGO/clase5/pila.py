class Solution:
    def isValid(self, s):
        stack = []
        # diccionario para saber cuál es la pareja de cada símbolo
        mapping = {")": "(", "}": "{", "]": "["}
    
        for char in s:
            if char in mapping:
            # se saca el elemento superior de la pila o un marcador si está vacía
                top_element = stack.pop() if stack else '#'
                
                # si la pareja de apertura esperada no coincide con lo que sacamoos da falso
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
            
        return not stack