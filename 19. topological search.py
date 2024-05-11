#topological search

class Graph:
    def __init__(self,ver):
        self.ver=ver
        self.graph=[[0]* ver for _ in range(ver)]

    def add_edge(self,start,end,waga):
        self.graph[start][end]=waga
        self.graph[end][start]=waga
    
    def __iter__(self):
        return iter(self.graph)

g=Graph(6)

g.add_edge(0, 1,5)
g.add_edge(0, 5,15)
g.add_edge(1, 2,20)
g.add_edge(2, 3,10)
g.add_edge(3, 4,30)
g.add_edge(3, 5,20)
g.add_edge(4, 0,15)
g.add_edge(5, 4,5)
g.add_edge(5, 2,10)

for row in g:
    print(row)
        
        
