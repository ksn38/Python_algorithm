def sieve0(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        #print('i', i)
        if sieve[i] != 0:
            j = i * 2
            #print('j ', j)

            while j < n:
                sieve[j] = 0
                j += i
                #print('jj  ', j)

    result = [i for i in sieve if i != 0]
    return result
    


def sieve(n):
    while True:
        sieve = [i for i in range(n)]
        sieve[1] = 0

        for i in range(2, n):
            if sieve[i] != 0:
                j = i * 2

                while j < n:
                    sieve[j] = 0
                    j += i

        result = [i for i in sieve if i != 0]
        if len(result) == n:
            break
        else:
            n += 1
        return result[-1]

print(sieve(300))
print(sieve0(300))