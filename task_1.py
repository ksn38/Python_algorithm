# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков. 


# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

#Вариант с одним циклом
def amax1(n):
    random.seed(44)
    a = [random.randint(-100, 100) for _ in range(0, n)]
    #print('Исходный массив', a)
    
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
    #print('Исходный массив', a)

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
    #print('Исходный массив', a)
    
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

#В результате проверки быстродействия на массивах от 50 до 500 с шагом в 50
# оказалось что вариант с двумя циклами оказался быстрее, так как первый цикл
#ороткий, а во втором проверяется одно условие в отличие от варианта с одним циклом, 
#но с двумя условиями в нем. Вариант с двумя циклами и промежуточным массивом
#оказался самым медленным. Судя по графику сложность алгоритма относится к постоянной.

import matplotlib.pyplot as plt

a = [132, 253, 374, 496, 617, 740, 870, 994, 1120, 1250]

plt.plot(a)
plt.show()

#"task_1.amax1(50)"
#1000 loops, best of 5: 143 usec per loop

#"task_1.amax1(150)"
#1000 loops, best of 5: 406 usec per loop

#"task_1.amax1(100)"
#1000 loops, best of 5: 273 usec per loop

#"task_1.amax1(150)"
#1000 loops, best of 5: 407 usec per loop

#"task_1.amax1(250)"
#1000 loops, best of 5: 675 usec per loop

#"task_1.amax1(300)"
#1000 loops, best of 5: 810 usec per loop

#"task_1.amax1(350)"
#1000 loops, best of 5: 943 usec per loop

#"task_1.amax1(400)"
#1000 loops, best of 5: 1.08 msec per loop

#"task_1.amax1(450)"
#1000 loops, best of 5: 1.21 msec per loop

#"task_1.amax1(500)"
#1000 loops, best of 5: 1.35 msec per loop




#"task_1.amax2(50)"
#1000 loops, best of 5: 132 usec per loop

#"task_1.amax2(100)"
#1000 loops, best of 5: 253 usec per loop

#"task_1.amax2(150)"
#1000 loops, best of 5: 374 usec per loop

#"task_1.amax2(200)"
#1000 loops, best of 5: 496 usec per loop

#"task_1.amax2(250)"
#1000 loops, best of 5: 617 usec per loop

#"task_1.amax2(300)"
#1000 loops, best of 5: 740 usec per loop

#"task_1.amax2(350)"
#1000 loops, best of 5: 870 usec per loop

#"task_1.amax2(400)"
#1000 loops, best of 5: 994 usec per loop

#"task_1.amax2(450)"
#1000 loops, best of 5: 1.12 msec per loop

#"task_1.amax2(500)"
#1000 loops, best of 5: 1.25 msec per loop




#"task_1.amax3(50)"
#1000 loops, best of 5: 145 usec per loop

#"task_1.amax3(100)"
#1000 loops, best of 5: 278 usec per loop

#"task_1.amax3(150)"
#1000 loops, best of 5: 411 usec per loop

#"task_1.amax3(200)"
#1000 loops, best of 5: 550 usec per loop

#"task_1.amax3(250)"
#1000 loops, best of 5: 676 usec per loop

#"task_1.amax3(300)"
#1000 loops, best of 5: 818 usec per loop

#"task_1.amax3(350)"
#1000 loops, best of 5: 957 usec per loop

#"task_1.amax3(400)"
#1000 loops, best of 5: 1.1 msec per loop

#"task_1.amax3(450)"
#1000 loops, best of 5: 1.23 msec per loop

#"task_1.amax3(500)"
#1000 loops, best of 5: 1.37 msec per loop


