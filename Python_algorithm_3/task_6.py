# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a = [random.randint(0, 20) for _ in range(0, 10)]
print('Исходный массив', a)
amax = 0
amin = 0

for i in range(1, len(a)):
    if a[amax] < a[i]:
        amax = i
    elif a[amin] > a[i]:
        amin = i

print('Мининмум и максимум', a[amin], a[amax])

b = a[amax + 1: amin]
if len(b) == 0:
    b = a[amin + 1: amax]

print('Срез', b)

summa = 0
for i in b:
    summa += i

print('Сумма', summa)