import heapq

class Solution:
    def lastStoneWeight(self, stones):
        cola = [-peso for peso in stones]
        heapq.heapify(cola)

        while len(cola) > 1:
            piedra1 = -heapq.heappop(cola)
            piedra2 = -heapq.heappop(cola)

            if piedra1 != piedra2:
                diferencia = piedra1 - piedra2
                heapq.heappush(cola, -diferencia)

        return -cola[0] if cola else 0