#Определить, какое число в массиве встречается чаще всего.

from collections import deque, Counter
import random
import sys

# счетчик с двумя листами
def counterlist():
    random.seed(97)
    a = [random.randint(0, 9) for _ in range(0, 10)]
    acount = []

    for i in range(0, len(a)):
        count = 0
        for j in range(0, len(a)):
            if a[j] == a[i]:
                count += 1
        acount.append(count)
        
    #return print('{} - массив\n{} - частоты элементов'.format(a, acount))
    return a, acount

counterlist()

# счетчик с двумя очередями из collections
def counterdeque():
    random.seed(97)
    a = deque(random.randint(0, 9) for _ in range(0, 10))
    acount = deque()

    for i in range(0, len(a)):
        count = 0
        for j in range(0, len(a)):
            if a[j] == a[i]:
                count += 1
        acount.append(count)
        
    #return print('{} - массив\n{} - частоты элементов'.format(a, acount))
    return a, acount

counterdeque()

# счетчик из collections
def counter():
    random.seed(97)
    acount = Counter(random.randint(0, 9) for _ in range(0, 10))
        
    #return print('{} - уникальные элементы массива и их частоты'.format(acount))
    return acount

counter()


def show_size(x):
    print(f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for i in x.items():
                show_size(i)
        elif not isinstance(x, str):
            for i in x:
                show_size(i)

print('счетчик с двумя листами')
show_size(counterlist())
print('\nсчетчик с двумя очередями из collections')
show_size(counterdeque())
print('\nсчетчик из collections')
show_size(counter())

