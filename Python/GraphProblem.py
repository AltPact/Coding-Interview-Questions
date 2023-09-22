# Using code taken from: https://medium.com/nerd-for-tech/graph-traversal-in-python-bfs-dfs-dijkstra-a-star-parallel-comparision-dd4132ec323a

#BFS
def bfs(graph,node):
    visited=[]
    queue=[]    
    visited.append(node)
    queue.append(node)
    
    while queue:
        s=queue.pop(0)
        
        for x in graph[s]:
            if x not in visited:
                visited.append(x)
                queue.append(x)
    return visited

#DFS
def dfs(graph,node):
    visited=[]
    queue=[]
    
    queue.append(node)
    visited.append(node)
    
    while queue:
        s=queue.pop()
        print(s)
        for x in graph[s][::-1]:
            if x not in visited:
                visited.append(x)
                queue.append(x)


#Dijkstra
import heapq
def dijkstra(graph,node):    
    distances={node:float('inf') for node in graph}
    distances[node]=0
    came_from={node:None for node in graph}    
    queue=[(0,node)]
    
    while queue:
        current_distance,current_node=heapq.heappop(queue)
        # relaxation
        for next_node,weight in graph[current_node].items():
            distance_temp=current_distance+weight
            if distance_temp<distances[next_node]:
                distances[next_node]=distance_temp
                came_from[next_node]=current_node
                heapq.heappush(queue,(distance_temp,next_node))
    return distances,came_from

import heapq

# A* Algorithm
def astar(graph, start_node, end_node):
    f_distance = {node: float('inf') for node in graph}
    f_distance[start_node] = 0

    g_distance = {node: float('inf') for node in graph}
    g_distance[start_node] = 0

    came_from = {node: None for node in graph}
    came_from[start_node] = start_node

    queue = [(0, start_node)]

    while queue:
        current_f_distance, current_node = heapq.heappop(queue)
        if current_node == end_node:
            return f_distance, came_from
        for next_node, edge_cost in graph[current_node].items():
            temp_g_distance = g_distance[current_node] + edge_cost
            if temp_g_distance < g_distance[next_node]:
                g_distance[next_node] = temp_g_distance
                heuristic = 0  # You can customize the heuristic function here
                f_distance[next_node] = temp_g_distance + heuristic
                came_from[next_node] = current_node
                heapq.heappush(queue, (f_distance[next_node], next_node))

    return f_distance, came_from

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS
print("BFS:")
bfs_result = bfs(graph, 'A')
print(bfs_result)

# DFS
print("\nDFS:")
dfs_result = dfs(graph, 'A')
print(dfs_result)

graphDijkstra = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 7},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 3},
    'F': {'C': 7, 'E': 3}
}

# Dijkstra's Algorithm
print("\nDijkstra's Algorithm:")
dijkstra_result, came_from = dijkstra(graphDijkstra, 'A')
print("Shortest Distances:", dijkstra_result)
print("Shortest Paths:", came_from)

# Sample graph representation as a dictionary
graphAStar = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 7},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 3},
    'F': {'C': 7, 'E': 3}
}

# A* Algorithm
print("\nA* Algorithm:")
a_star_result, came_from = astar(graphAStar, 'A', 'F')
print("Estimated Distances (f-distance):", a_star_result)
print("Shortest Paths:", came_from)
