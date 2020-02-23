# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков. 


# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

#Вариант с одним циклом
def amax1(n):
    random.seed(44)
    a = [random.randint(-100, 100) for _ in range(0, n)]
    print('Исходный массив', a)
    
    i = 0
    amax = -1

    while i < n:
        if a[i] < 0 and amax == -1:
            amax = i
        elif a[i] < 0 and a[i] > a[amax]:
            amax = i
            
        i += 1
            
    return a[amax], amax
    
# Вариант с 2мя циклами
def amax2(n):
    random.seed(44)
    a = [random.randint(-100, 100) for _ in range(0, n)]
    print('Исходный массив', a)

    amax = 0

    while True:
        if a[amax] > 0:
            amax += 1
        else:
            break

    for i in range(1, len(a)):
        if a[amax] < a[i] and a[i] < 0:
            amax = i
            
    return a[amax], amax

#Вариант с двумя циклами и промежуточным списком
def amax3(n):
    random.seed(44)
    a = [random.randint(-100, 100) for _ in range(0, n)]
    print('Исходный массив', a)
    
    i = 0
    b = []
    amax = 0

    while i < n:
        if a[i] < 0:
            b.append(a[i])
            
        i += 1
    
    bmax = max(b)
    
    for i in range(0, len(a)):
        if a[i] == bmax:
            amax = i
            
    return bmax, amax

print(amax1(20))

