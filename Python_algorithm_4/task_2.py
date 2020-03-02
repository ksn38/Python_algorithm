#Написать два алгоритма нахождения i-го по счёту простого числа. 
#Функция нахождения простого числа должна принимать на вход натуральное и 
#возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов. 


# Решето Эратосфена
def sieve(n):
    m = n + 1
    while True:
        sieve = [i for i in range(m)]
        sieve[1] = 0

        for i in range(2, m):
            if sieve[i] != 0:
                j = i * 2

                while j < m:
                    sieve[j] = 0
                    j += i

        result = [i for i in sieve if i != 0]
        if len(result) < n:
            m += 1
        else:
            return result[-1]


# Метод перебора
def prime(n):
    prime = [0, 1]
    maxp = 3
    
    while len(prime) < n + 2:
        for i in range(maxp - 1, maxp):
            countp = 0
            for j in range(2, maxp):
                if i % j == 0:
                    countp += 1
            if countp == 1:
                prime.append(i)
            maxp += 1
            
    return prime[-1]


# print('prime', prime(2))
# print('sieve', sieve(2))

# В результате проверки быстродействия на массивах размером от 10 до 70 с шагом в 10
# оказалось что вариант с перебором оказался быстрее, так как при следующей итерации новые значения простых
# чисел добавляются к старым, а перебираются с начала только делители. В решете Эратосфена
# на каждом цикле приходится искать простые числа с самого начала.
# Судя по графику сложность алгоритма относится к квадратичной.

import matplotlib.pyplot as plt

s = [0.0983, 0.527, 1.3, 3.07, 5.42, 8.33, 13.5]
p = [0.0466, 0.198, 0.452, 0.986, 1.65, 2.45, 3.73]

plt.plot(s, label='sieve')
plt.plot(p, label='prime')
plt.legend()
plt.show()

# Решето Эратосфена
# "import task_2" "task_2.sieve(10)"
# 1000 loops, best of 5: 98.3 usec per loop

# "import task_2" "task_2.sieve(20)"
# 1000 loops, best of 5: 527 usec per loop

# "import task_2" "task_2.sieve(30)"
# 1000 loops, best of 5: 1.3 msec per loop

# "import task_2" "task_2.sieve(40)"
# 1000 loops, best of 5: 3.07 msec per loop

# "import task_2" "task_2.sieve(50)"
# 1000 loops, best of 5: 5.42 msec per loop

# "import task_2" "task_2.sieve(60)"
# 1000 loops, best of 5: 8.33 msec per loop

# "import task_2" "task_2.sieve(70)"
# 1000 loops, best of 5: 13.5 msec per loop


# Метод перебора
# "import task_2" "task_2.prime(10)"
# 1000 loops, best of 5: 46.6 usec per loop

# "import task_2" "task_2.prime(20)"
# 1000 loops, best of 5: 198 usec per loop

# "import task_2" "task_2.prime(30)"
# 1000 loops, best of 5: 452 usec per loop

# "import task_2" "task_2.prime(40)"
# 1000 loops, best of 5: 986 usec per loop

# "import task_2" "task_2.prime(50)"
# 1000 loops, best of 5: 1.65 msec per loop

# "import task_2" "task_2.prime(60)"
# 1000 loops, best of 5: 2.45 msec per loop

# "import task_2" "task_2.prime(70)"
# 1000 loops, best of 5: 3.73 msec per loop

