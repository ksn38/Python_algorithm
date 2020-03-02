#Определить, какое число в массиве встречается чаще всего.

import random

a = [random.randint(0, 9) for _ in range(0, 10)]
acount = []
amax = 0

for i in range(0, len(a)):
    count = 0
    for j in range(0, len(a)):
        if a[j] == a[i]:
            count += 1
    acount.append(count)
    
print(a, 'массив')
print(acount, 'частоты элементов')

often = 0
aoften = []

for i in range(0, len(acount)):
    if acount[i] > acount[often]:
        often = i

aoften.append(a[often])

for i in range(0, len(acount)):
    if acount[i] == acount[often]:
        aoften.append(a[i])
                
print('Чаще всего встречается: ', set(aoften))
