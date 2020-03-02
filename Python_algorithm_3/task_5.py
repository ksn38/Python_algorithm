#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

a = [random.randint(-20, 20) for _ in range(0, 10)]
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

print('Значение', a[amax])
print('Индекс', amax)