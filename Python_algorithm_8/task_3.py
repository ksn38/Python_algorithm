'''Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания: a. граф должен храниться в виде списка смежности; b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.'''

n = int(input('введите число вершин '))
node = int(input('введите точку входа '))

# генератор графа с ориентацией ребер в обе стороны
def graph(n):
    a = dict([(i, 0) for i in range(n)])

    for i in a:
        b = [i for i in range(n)]
        b.pop(i)
        a[i] = b
    return a

print('сгенерированный граф', graph(n))

# поиск вглубину
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for i in graph[node]:
            dfs(graph, i, visited)
    return visited

print('путь обхода графа', dfs(graph(n), node, []))

