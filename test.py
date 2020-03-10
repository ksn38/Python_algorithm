g2 = [[0, 0, 3],
    [0, 0, 9],
    [3, 9, 0]]

g = [[0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    d = {}
    
    cost[start] = 0
    min_cost = 0
    
    while min_cost < float('inf'):
        
        is_visited[start] = True
        
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    print(parent)
                    for i in range(length):
                        if parent[i] != 'inf':
                            #print(i)
                            d.update({i: [0, parent[i], i]})
                     
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                
    return cost, d
    
s = 0
print(dijkstra(g, s))

#d = {'a': [1, 2], 'b': [3, 4]}
#d.update({'a': [5, 6]})
