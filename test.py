import random

random.seed(1)
a = [random.randint(0, 49) for _ in range(10)]
print(a, 'исходный массив')

def mergesort(x):
    if len(x) < 2:
        return x
    result = []  # moved!
    mid = int(len(x) / 2)
    #print('mid', mid)
    y = mergesort(x[:mid])
    print('y', y)
    z = mergesort(x[mid:])
   # print('z', z)
    return y



# print(mergesort(a), 'отсортированный массив')
print(mergesort(a), 'отсортированный массив')