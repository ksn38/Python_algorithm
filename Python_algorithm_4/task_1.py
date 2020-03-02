# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков. 


# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

# Вариант с одним циклом
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

# Вариант с двумя циклами, промежуточным списком и функцией max
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

#В результате проверки быстродействия на массивах размером от 50 до 500 с шагом в 50
#оказалось что вариант с двумя циклами оказался быстрее, так как первый цикл
#ороткий, а во втором проверяется одно условие в отличие от варианта с одним циклом, 
#но с двумя условиями в нем. Вариант с двумя циклами и промежуточным массивом  и функцией max
#оказался самым медленным, но незначительно. Судя по графику сложность алгоритма относится к постоянной.

import matplotlib.pyplot as plt

a = [89, 169, 243, 329, 410, 498, 558, 647, 742, 799]
b = [87, 157, 234, 313, 384, 459, 549, 602, 677, 779]
c = [90, 166, 253, 331, 416, 492, 567, 679, 740, 808]

plt.plot(a, label='с одним циклом')
plt.plot(b, label='с 2мя циклами')
plt.plot(c, label='с двумя циклами и ф-ей max')
plt.legend()
plt.show()

# Вариант с одним циклом
# "import task_1" "task_1.amax1(50)"
# 1000 loops, best of 5: 88.9 usec per loop

# "import task_1" "task_1.amax1(100)"
# 1000 loops, best of 5: 169 usec per loop

# "import task_1" "task_1.amax1(150)"
# 1000 loops, best of 5: 243 usec per loop

# "import task_1" "task_1.amax1(200)"
# 1000 loops, best of 5: 329 usec per loop

# "import task_1" "task_1.amax1(250)"
# 1000 loops, best of 5: 410 usec per loop

# "import task_1" "task_1.amax1(300)"
# 1000 loops, best of 5: 498 usec per loop

# "import task_1" "task_1.amax1(350)"
# 1000 loops, best of 5: 558 usec per loop

# "import task_1" "task_1.amax1(400)"
# 1000 loops, best of 5: 647 usec per loop

# "import task_1" "task_1.amax1(450)"
# 1000 loops, best of 5: 742 usec per loop

# "import task_1" "task_1.amax1(500)"
# 1000 loops, best of 5: 799 usec per loop


# Вариант с 2мя циклами
# "import task_1" "task_1.amax2(50)"
# 1000 loops, best of 5: 86.6 usec per loop

# "import task_1" "task_1.amax2(100)"
# 1000 loops, best of 5: 157 usec per loop

# "import task_1" "task_1.amax2(150)"
# 1000 loops, best of 5: 234 usec per loop

# "import task_1" "task_1.amax2(200)"
# 1000 loops, best of 5: 313 usec per loop

# "import task_1" "task_1.amax2(250)"
# 1000 loops, best of 5: 384 usec per loop

# "import task_1" "task_1.amax2(300)"
# 1000 loops, best of 5: 459 usec per loop

# "import task_1" "task_1.amax2(350)"
# 1000 loops, best of 5: 549 usec per loop

# "import task_1" "task_1.amax2(400)"
# 1000 loops, best of 5: 602 usec per loop

# "import task_1" "task_1.amax2(450)"
# 1000 loops, best of 5: 677 usec per loop

# "import task_1" "task_1.amax2(500)"
# 1000 loops, best of 5: 779 usec per loop


# Вариант с двумя циклами, промежуточным списком и функцией max
# "import task_1" "task_1.amax3(50)"
# 1000 loops, best of 5: 90 usec per loop

# "import task_1" "task_1.amax3(100)"
# 1000 loops, best of 5: 166 usec per loop

# "import task_1" "task_1.amax3(150)"
# 1000 loops, best of 5: 253 usec per loop

# "import task_1" "task_1.amax3(200)"
# 1000 loops, best of 5: 331 usec per loop

# "import task_1" "task_1.amax3(250)"
# 1000 loops, best of 5: 416 usec per loop

# "import task_1" "task_1.amax3(300)"
# 1000 loops, best of 5: 492 usec per loop

# "import task_1" "task_1.amax3(350)"
# 1000 loops, best of 5: 567 usec per loop

# "import task_1" "task_1.amax3(400)"
# 1000 loops, best of 5: 679 usec per loop

# "import task_1" "task_1.amax3(450)"
# 1000 loops, best of 5: 740 usec per loop

# "import task_1" "task_1.amax3(500)"
# 1000 loops, best of 5: 808 usec per loop


