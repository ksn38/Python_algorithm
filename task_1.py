#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны 
#каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

a = [i for i in range(2, 100)]

for i in range(2, 10):
    spam = 0
    for j, val in enumerate(a):
        if j % i == 0:
            spam += 1
    print(spam)
