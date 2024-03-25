# Grafy

#zlekcji

import sys

class Graph:
    def __init__(self, w):
        self.wierzcholki = w
        self.graph = [[0] * w for _ in range(w)]
        
    def add(self, start, end, waga):
        self.graph[start][end] = waga
        self.graph[end][start] = waga
        
    def path(self, start, end, b):
        
        def _path(s, budget):
            memo = [sys.maxsize] * self.wierzcholki
            memo[s] = 0
            
            for _ in range(self.wierzcholki - 1):
                for u in range(self.wierzcholki):
                    for v in range(self.wierzcholki):
                        if memo[u] + self.graph[u][v] <= budget:
                            memo[v] = min(memo[v], memo[u] + self.graph[u][v])
                        
            return memo[end]
        
        return _path(start, b)
    
#v2
    
class Graph:
    def __init__(self, size):
        self.size = size
        self.g = [[0] * size for _ in range(size)]
        
    def add(self, start, end, w):
        self.g[start][end] = w
        self.g[end][start] = w

        
    def bfs(self, start):
        visited = [False] * self.size
        visit = []

        return visit

g = Graph(4)
g.add(0,1,10)
g.add(0,2,2)
g.add(2,3,1)
g.add(1,3,11)


print(g.bfs(0))