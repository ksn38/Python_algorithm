'''Доработать алгоритм Дейкстры (рассматривался на уроке), 
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.'''

g = [[0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]]
    
g2 = [[0, 0, 3],
    [0, 0, 9],
    [3, 9, 0]]


def dijkstra(graph, start):
    length = len(graph)
    print('length', length)
    is_visited = [False] * length
    print('is_visited', is_visited)
    cost = [float('inf')] * length
    print('cost', cost)
    parent = [-1] * length
    print('parent', parent)
    
    cost[start] = 0
    min_cost = 0
    print('--начало циклов--\n')
    
    while min_cost < float('inf'):
        
        is_visited[start] = True
        print('  is_visited[{}]'.format(start), is_visited[start])
        
        for i, vertex in enumerate(graph[start]):
            print('    graph[{}]'.format(start), graph[start])
            print('    i, vertex', i, vertex)
            if vertex != 0 and not is_visited[i]:
                print('    vertex', vertex)
                print('    cost[i = {}]'.format(i), cost[i])
                
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    print('    cost[{}] = {} + {}'.format(i, vertex, cost[start]))
                    #print('    cost[i]'.format(i), cost[i])
                    parent[i] = start
                    print('    parent[{}]'.format(i), parent[i])
                    print('    parent', parent)
        
        print('  ++конец 1ого цикла++\n')                
        min_cost = float('inf')
        for i in range(length):
            print('    min_cost ', min_cost)
            print('    cost[{}]'.format(i), cost[i])
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                print('    min_cost = cost[i]', min_cost)
                start = i
                print('    start = i', start)
        print('  **конец 2ого цикла**\n')
                
    return cost
    
s = 1
print(dijkstra(g2, s))
