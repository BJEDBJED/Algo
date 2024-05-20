# Algo Dijkstra

class Graph():

    def __init__(self,vertex):
        self.V=vertex
        self.graph=[[0 for _ in range(vertex)] for _ in range(vertex)]

    def printway(self,dist):
        for node in range(self.V):
            print(f"{node},{dist[node]}")

    def minway(self,dist,shortset):
        min=float('inf')
        min_index=0

        for v in range(self.V):
            if dist[v]<min and shortset[v]==False:
                min=dist[v]
                min_index=v
        return min_index
    
    def dijkstra(self,src):
        dist=[float('inf')]*self.V
        dist[src]=0
        shortset=[False]*self.V

        for cout in range(self.V):
            u=self.minway(dist,shortset)
            shortset[u]=True

            for v in range(self.V):
                if self.graph[u][v]>0 and shortset[v] == False and dist[v]>dist[u] + self.graph[u][v]:
                    dist[v]=dist[u]+self.graph[u][v]
        self.printway(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
g.dijkstra(0)

#2

import heapq

def dijkstra(graph, start):
    dist = { vertex: float('inf') for vertex in graph}
    dist[start] = 0
    
    pq = [(0,start)]
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        if current_dist > dist[current_vertex]:
            continue
        
        for neighbour, weight in graph[current_vertex].items():            distance = current_dist + weight
            if distance < dist[neighbour]: 
                dist[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))
    


    return dist

graph = {
    'A':{'B':1, 'C': 4},
    'B':{'A':1, 'C': 2, 'D': 5},
    'C':{'A':4, 'B': 2, 'D': 1},
    'D':{'B':5, 'C': 1}
    }
    
    
start = 'A'
shortest = dijkstra(graph, start)
print(shortest)
