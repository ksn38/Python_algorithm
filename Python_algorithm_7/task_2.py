'''Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.'''

import random

a = [random.randint(0, 49) for _ in range(10)]
print(a, 'исходный массив')

def mergesort(x):
    if len(x) < 2:
        return x
    asorted = []
    mid = len(x) // 2
    y = mergesort(x[:mid])
    z = mergesort(x[mid:])
    while len(y) > 0 and len(z) > 0:
        if y[0] > z[0]:
            asorted.append(z[0])
            z.pop(0)
        else:
            asorted.append(y[0])
            y.pop(0)
    asorted += y
    asorted += z
    return asorted
        
print(mergesort(a), 'отсортированный массив')


