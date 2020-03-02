#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(0, 100) for _ in range(0, 6)]
print(a)

amax = 0
amin = 0

for i in range(1, len(a)):
    if a[i] < a[amax]:
        amax = i

for i in range(1, len(a)):
    if a[i] > a[amin]:
        amin = i
        
a[amax], a[amin] = a[amin], a[amax]

print(a)
