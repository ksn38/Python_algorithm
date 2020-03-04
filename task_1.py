'''Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.'''

import random

a = [random.randint(-100, 99) for i in range(10)]
print(a, 'исходный массив')

def sortbub0(x):
    random.seed(5)
    a = [random.randint(-100, 99) for i in range(x)]
    buble = []
    for i in range(0, len(a)):
        #print('новый цикл')
        for j in range(i, len(a)):
            #print('a[i] {}[{}]'.format(a[i], i))
            #print('a[j] {}[{}]'.format(a[j], j))
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
            #print(a)
    return a

# гибрид сортировки пузрьком и сортировки выбором
def sortbub(a):
    for i in range(0, len(a)):
        amin = i
        for j in range(i, len(a)):
            if a[j] < a[amin]:
                a[amin], a[j] = a[amin], a[j]
            elif a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a

print(sortbub(a), 'отсортированный массив')
