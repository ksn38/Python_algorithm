'''Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.'''

import random

random.seed(5)
a = [random.randint(-100, 99) for i in range(10)]
#print('исходный массив', a)

def sortbub(x):
    random.seed(5)
    a = [random.randint(-100, 99) for i in range(x)]
    for i in range(0, len(a)):
        #print('новый цикл')
        for j in range(i, len(a)):
            #print('a[i] {}[{}]'.format(a[i], i))
            #print('a[j] {}[{}]'.format(a[j], j))
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
            #print(a)
    return a

def sortbub2(x):
    random.seed(5)
    a = [random.randint(-100, 99) for i in range(x)]

    for i in range(0, len(a)):
        for j in range(0, len(a)):
            #print('a[i] {}[{}]'.format(a[i], i))
            #print('a[j] {}[{}]'.format(a[j], j))
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
        #print(a)
    return a

print('отсортированный массив', sortbub(10))
print('отсортированный массив', sortbub2(10))