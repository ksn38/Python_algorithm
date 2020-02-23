def sieve0(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        print('i', i) 
        if sieve[i] != 0:
            j = i * 2
            print('j ', j)

            while j < n:
                sieve[j] = 0
                j += i
                print('jj  ', j)

    result = [i for i in sieve if i != 0]
    return result
    
#print(sieve0(15))


def sieve(n):
    sieve = [0, 1]
    m = 3
    while len(sieve) < n:
        result = [i for i in range(1, m)]
        print('result', result)
        for i in range(2, len(result)):
            print('i', i) 
            if result[i] != 0:
                j = i * 2
                print('j ', j)

                while j < len(result):
                    result[j] = 0
                    j += i
                    print('jj  ', j)
                print('jresult', result)

        sieve = ([i for i in result if i != 0])
        print('sieve', sieve)
        m += 1
    return result
    
print(sieve(5))
print('sieve0', sieve0(15))
