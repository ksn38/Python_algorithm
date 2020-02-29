# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.

from collections import deque

a = [2, 4, 14, 13]
b = [0, 12, 4, 15]

# перевод букв в 10-ричную систему
def from16to10(lst):
    for i in range(0, len(lst)):
        if lst[i] == 'A':
            lst[i] = 10
        elif lst[i] == 'B':
            lst[i] = 11
        elif lst[i] == 'C':
            lst[i] = 12
        elif lst[i] == 'D':
            lst[i] = 13
        elif lst[i] == 'E':
            lst[i] = 14
        elif lst[i] == 'F':
            lst[i] = 15
        else:
            lst[i] = int(lst[i])
    return lst

# добавление нулей вперед очереди меньшей длины
def apend0(lst1, lst2):
    lst1 = deque(from16to10(lst1))
    lst2 = deque(from16to10(lst2))
    while len(lst1) != len(lst2):
        if len(lst1) < len(lst2):
            lst1.appendleft(0)
        elif len(lst1) > len(lst2):
            lst2.appendleft(0)
        else:
            break
    return lst1, lst2

a2, b2 = apend0(a, b)

# функция сложение 16-ричных чисел
def summator(lst1, lst2):
    summa = []
    lst1.reverse()
    lst2.reverse()
    mem = 0
    for i in range(0, len(lst1)):
        if mem == 0:
            if lst1[i] + lst2[i] < 16:
                summa.append(lst1[i] + lst2[i])
                print(summa)
            else:
                summa.append(lst1[i] + lst2[i] - 16)
                print(summa)
                mem = 1
        else:
            mem = 0
            if lst1[i] + lst2[i] < 16:
                summa.append(lst1[i] + lst2[i] + 1)
                print(summa)
            else:
                summa.append(lst1[i] + lst2[i] - 15)
                print(summa)
                mem = 1
        print(mem)
    if mem == 1:
        summa.append(1)
    lst1.reverse()
    lst2.reverse()

    return summa[::-1]

summa = summator(a2, b2)
print(summa)

# перевод цифр в 16-ричную систему
def from10to16(lst):
    for i in range(0, len(lst)):
        if lst[i] == 10:
            lst[i] = 'A'
        elif lst[i] == 11:
            lst[i] = 'B'
        elif lst[i] == 12:
            lst[i] = 'C'
        elif lst[i] == 13:
            lst[i] = 'D'
        elif lst[i] == 14:
            lst[i] = 'E'
        elif lst[i] == 15:
            lst[i] = 'F'
        else:
            lst[i] = str(lst[i])
    return lst

print('сумма', from10to16(summa))