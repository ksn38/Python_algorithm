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

def mergesort1(x):
    asorted = []
    i = len(x)//2
    j = (len(x)//2) + 1
    while len(x[i:j]) != len(x):
        if x[i] < x[j]:
            asorted.append(x[i])
            print('i', x[i], i)
            i -= 1
        else:
            asorted.append(x[j])
            print('j', x[j], j)
            j -= -1
    asorted.append(x[i])
    return asorted

def mergesort(x):
    asorted = []
    i = 0
    j = -1
    while len(x[i:j]) != 0:
        if x[i] < x[j]:
            asorted.append(x[i])
            print(x[i], i)
            i += 1
        else:
            asorted.append(x[j])
            print(x[j], j)
            j += -1
    asorted.append(x[i])
    return asorted
        


#print(mergesort(a), 'отсортированный массив')
print(mergesort1(a), 'отсортированный массив')
print(a)
