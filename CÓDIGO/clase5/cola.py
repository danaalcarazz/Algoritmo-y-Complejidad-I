from collections import deque

class RecentCounter:
    def __init__(self):
        # se usa un deque q sería cola doble para operaciones eficientes
        self.queue = deque()

    def ping(self, t):
        # se agrega la nueva solicitud al final de la cola
        self.queue.append(t)
        
        # se elimina de la cola todas las solicitudes que sean menores a t - 3000
        while self.queue[0] < t - 3000:
            self.queue.popleft()
            
        # el tamaño actual de la cola es el número de solicitudes en los últimos 3000ms
        return len(self.queue)