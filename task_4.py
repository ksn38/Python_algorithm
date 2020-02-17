#Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 
#Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите n '))
ncir = 0
summa = 0
num1 = 1
num2 = -0.5
summa += num1

while n-1 != ncir:
    def fsumma(num1, num2):
        num1 += (num1 + num2)/2
        return fsumma(num1, fsumma(num1, num2))
    ncir += 1
    print(summa)

print(summa)
