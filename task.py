#Определить, какое число в массиве встречается чаще всего.

from collections import deque, Counter, defaultdict, OrderedDict
import random
import sys

# 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] win32

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
    
    return acount, def_dict, ord_dict, dict_simple

dict_collections()

def show_size(x):
    for i in x:
        print(f'type= {i.__class__}, size= {sys.getsizeof(i)}, object= {i}')

def show_size2(x):
    print(f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

print('счетчик с двумя листами')
show_size(counterlist())
print('\nсчетчик с двумя очередями из collections')
show_size(counterdeque())
print('\nсчетчик из collections')
show_size2(counter())
print('\nсловари из collections и обычный словарь')
show_size(dict_collections())



# счетчик с двумя листами
# type= <class 'list'>, size= 192, object= [3, 6, 5, 0, 9, 0, 8, 0, 0, 4]
# type= <class 'list'>, size= 192, object= [1, 1, 1, 4, 1, 4, 1, 4, 4, 1]

# счетчик с двумя очередями из collections
# type= <class 'collections.deque'>, size= 632, object= deque([3, 6, 5, 0, 9, 0, 8, 0, 0, 4])
# type= <class 'collections.deque'>, size= 632, object= deque([1, 1, 1, 4, 1, 4, 1, 4, 4, 1])

# счетчик из collections
# type= <class 'collections.Counter'>, size= 384, object= Counter({0: 4, 3: 1, 6: 1, 5: 1, 9: 1, 8: 1, 4: 1})

# словари из collections и обычный словарь
# type= <class 'collections.Counter'>, size= 384, object= Counter({0: 4, 3: 1, 6: 1, 5: 1, 9: 1, 8: 1, 4: 1})
# type= <class 'collections.defaultdict'>, size= 376, object= defaultdict(<class 'int'>, {3: 1, 6: 1, 5: 1, 0: 4, 9: 1, 8: 1, 4: 1})
# type= <class 'collections.OrderedDict'>, size= 784, object= OrderedDict([(3, 1), (6, 1), (5, 1), (0, 4), (9, 1), (8, 1), (4, 1)])
# type= <class 'dict'>, size= 368, object= {3: 1, 6: 1, 5: 1, 0: 4, 9: 1, 8: 1, 4: 1}

Process finished with exit code 0
