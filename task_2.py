'''Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.'''

import random

a = [random.randint(0, 49) for _ in range(10)]
print(a, 'исходный массив')

def mergesort0(x):
    asorted = []
    while len(x) != 0:
        if x[0] < x[-1]:
            asorted.append(x.pop(0))
        else:
            asorted.append(x.pop(-1))
    return asorted

def mergesort(x):
    if len(x) < 2:
        return x
    result = []  # moved!
    mid = int(len(x) / 2)
    y = mergesort(x[:mid])
    z = mergesort(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result
        


#print(mergesort(a), 'отсортированный массив')
print(mergesort(a), 'отсортированный массив')
print(a)

