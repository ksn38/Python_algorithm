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


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    d = {}
    for i in range(length):
        d.update({i: [start]})

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    for i in range(length):
                        if parent[i] != -1:
                            if parent[i] != d[i][-1]:
                                # print(parent[i])
                                d[i].append(parent[i])

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                # print(i)

    for i in d:
        if d[i][-1] != i:
            if cost[i] == float('inf'):
                d[i] = 'нет пути'
            else:
                d[i].append(i)

    return cost, d


s = 0
print('стоимость кратчайшего пути и последовательность вершин до каждой точки до точки:\n', dijkstra(g, s))

