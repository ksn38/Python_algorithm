g2 = [[0, 0, 3],
    [0, 0, 9],
    [3, 9, 0]]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    
    cost[start] = 0
    min_cost = 0
    
    while min_cost < float('inf'):
        
        is_visited[start] = True
        
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                     
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                
    return cost
    
s = 1
print(dijkstra(g2, s))
