#Написать два алгоритма нахождения i-го по счёту простого числа. 
#Функция нахождения простого числа должна принимать на вход натуральное и 
#возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов. 

def sieve0(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result

def prime0(n):
    prime = []
    
    for i in range(2, n):
        countp = 0
        for j in range(2, n):
            if i % j == 0:
                countp += 1
        if countp == 1:
            prime.append(i)
            
    return prime

print(prime0(100))
#print(sieve0(40))


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

print(prime(4))

def sieve(n):
    sieve = [0, 1]
    sieve[1] = 0
    
    while len(sieve) < n + 2:
        for i in range(2, len(sieve) + 1):
            print(i)
            if sieve[i - 1] != 0:
                j = i * 2
                sieve.append(j)
                print(sieve)

                while j < len(sieve) + 1:
                    sieve[j] = 0
                    j += i

    result = sieve[-1]
    return result
    
print(sieve(4))


