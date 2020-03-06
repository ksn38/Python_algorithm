'''Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.'''

import random
arr = [random.randint(-100, 99) for i in range(10)]
print(arr, 'исходный массив')

# Перед самим методом пузырька прогнал массив через цикл, который перемещает положительные числа в одну сторону.
# При прогоне через timeit 100 циклов с массивом размером в 1000 элементов лучший цикл стал быстрее на 10-15 %
def sortbub(a):
    m = 0
    for i in range(0, len(a)):
        if a[i] > 0:
            a[i], a[m] = a[m], a[i]
            m += 1
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a

print(sortbub(arr), 'отсортированный массив')


# функции для timeit
def sortbub0(x):
    a = [random.randint(-100, 99) for i in range(x)]
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def sortbub1(x):
    a = [random.randint(-100, 99) for i in range(x)]
    m = 0
    for i in range(0, len(a)):
        if a[i] > 0:
            a[i], a[m] = a[m], a[i]
            m += 1
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a

# (base) E:\Python_algorithm>python -m timeit -n 100 "import task_1" "task_1.sortbub0(1000)"
# 100 loops, best of 5: 62.3 msec per loop

# (base) E:\Python_algorithm>python -m timeit -n 100 "import task_1" "task_1.sortbub1(1000)"
# 100 loops, best of 5: 54.5 msec per loop
