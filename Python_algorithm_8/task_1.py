'''На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.'''

N = 4

# создание матрицы смежности для неориентрованного граафа
n = []
for i in range(N):
    Ni = []
    for j in range(N):
        if i != j:
            Ni.append(1)
        else:
            Ni.append(0)
    n.append(Ni)

print('матрицa смежности', n)
print('число рукопожатий', (sum(sum(i) for i in (n)))//2)
