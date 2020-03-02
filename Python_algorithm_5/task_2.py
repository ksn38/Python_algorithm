# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.

from collections import deque

a = ['A', '2']
b = ['C', '4', 'F']

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

# функция сложение 16-ричных чисел
def summator(lst1, lst2):
    summa = []
    lst1, lst2 = apend0(lst1, lst2)
    lst1.reverse()
    lst2.reverse()
    mem = 0
    for i in range(0, len(lst1)):
        if mem == 0:
            if lst1[i] + lst2[i] < 16:
                summa.append(lst1[i] + lst2[i])
            else:
                summa.append(lst1[i] + lst2[i] - 16)
                mem = 1
        else:
            mem = 0
            if lst1[i] + lst2[i] < 16:
                summa.append(lst1[i] + lst2[i] + 1)
            else:
                summa.append(lst1[i] + lst2[i] - 15)
                mem = 1
    if mem == 1:
        summa.append(1)
    lst1.reverse()
    lst2.reverse()

    return summa[::-1]

# функция умножения 16-ричных чисел
def multiplicator(lst1, lst2):
    mul = [0 for _ in range(0, len(lst2))]
    for i in lst1:
        counter = 0
        while counter != i:
            mul, lst2 = apend0(mul, lst2)
            mul = summator(mul, lst2)
            counter += 1
        mul.append(0)
    return mul[:-1]

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

print('сумма', from10to16(summator(a, b)))
print('произведение', from10to16(multiplicator(a, b)))