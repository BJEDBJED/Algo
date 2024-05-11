#Bellman-Ford

class Graph:
    def __init__(self,w):
        self.wierzcholki=w
        self.graph=[[0] * w for _ in range(w)]

    def add(self,u,v,waga):
        self.graph[u][v]=waga

    def bellman_ford(self,src):
        distances=[float('inf')]*self.wierzcholki
        distances[src]=0

        for _ in range(self.wierzcholki-1):
            for u in range(self.wierzcholki):
                for v in range(self.wierzcholki):
                    if self.graph[u][v]!=0 and distances[u] != float('inf') and distances[u]+self.graph[u][v]<distances[v]:
                        distances[v]=distances[u]+self.graph[u][v]

        for u in range(self.wierzcholki):
            for v in range(self.wierzcholki):
                if self.graph[u][v] !=0 and distances[u] !=float('inf') and distances[u]+self.graph[u][v]<distances[v]:
                    print("Mamy cykl o ujemnej wadze")
                    return None 
        
        return distances

g=Graph(6)
g.add(0,1,5)
g.add(1,2,-5)
g.add(1,3,15)
g.add(2,4,25)
g.add(2,5,5)
g.add(3,4,-15)

print(g.bellman_ford(0))
