import random

def counterlist(x):
    random.seed(x)
    a = [random.randint(0, 9) for _ in range(0, 10)]
    acount = []

    for i in range(0, len(a)):
        count = 0
        for j in range(0, len(a)):
            if a[j] == a[i]:
                count += 1
        acount.append(count)
        
    return print('{} - массив\n{} - частоты элементов'.format(a, acount))

for i in range(0, 100):
    print(i)
    counterlist(i)
