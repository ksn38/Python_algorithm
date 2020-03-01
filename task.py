#Определить, какое число в массиве встречается чаще всего.

from collections import deque, Counter, defaultdict, OrderedDict
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

# словари из collections и обычный словарь
def dict_collections():
    random.seed(97)
    acount = Counter(random.randint(0, 9) for _ in range(0, 10))
    def_dict = defaultdict(int, acount)
    ord_dict = OrderedDict(acount)
    dict_simple = dict(acount)
    
    return acount, defaultdict, ord_dict, dict_simple

dict_collections()

def show_size(x):
    print(f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for i in x.items():
                show_size(i)
        elif not isinstance(x, str):
            for i in x:
                show_size(i)
                
def show_size_dict(x):
    for i in x:
        print(f'type= {i.__class__}, size= {sys.getsizeof(i)}')

print('счетчик с двумя листами')
show_size(counterlist())
print('\nсчетчик с двумя очередями из collections')
show_size(counterdeque())
print('\nсчетчик из collections')
show_size(counter())
print('\nсловари из collections и обычный словарь')
show_size_dict(dict_collections())

