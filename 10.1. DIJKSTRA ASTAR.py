#DIJKSTRA ASTAR

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
            if distance < dist[neighbour]: #inf
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

import heapq


def heuristic(node, goal):
    return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5


def astar(graph, start, goal):
    visited = set()
    
    pq = [(0, start)]
    g_score = {start: 0}
    
    while pq:
        f, current = heapq.heappop(pq)
        
        if current == goal:
            return g_score[current]
            
        visited.add(current)
        
        for neighbour, cost in graph[current].items(): 
            if neighbour in visited:
                continue
            
            distance = g_score[current] + cost
            
            if neighbour not in g_score or distance < g_score[neighbour]:
                g_score[neighbour] = distance
                heuristic_score = distance + heuristic(neighbour, goal)
                heapq.heappush(pq, (heuristic_score , neighbour))
                
                
    return None  