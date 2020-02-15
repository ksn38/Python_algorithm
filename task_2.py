#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, 
#в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введите число ')
chet = 0
nechet = 0
lenum = len(num)

while chet + nechet != lenum:
    ost = int(num) % 10
    num = int(num) // 10
    if ost % 2 == 0:
        chet += 1
    else:
        nechet += 1

print('нечетных цифр: {}, четных: {}'.format(nechet, chet))
