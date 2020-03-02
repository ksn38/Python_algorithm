#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
#Например, если введено число 3486, надо вывести 6843.

num = input('Введите число ')
lenum = len(num)
revnum = ''

while lenum != len(revnum):
    numost = int(num) % 10
    numost = str(numost)
    revnum = revnum + numost
    num = int(num) // 10
    num = str(num)
print(revnum)
