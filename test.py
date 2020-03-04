def sortbub2(x):
    random.seed(5)
    a = [i for i in range(x, 10)]

    minimum = 0
    for i in range(0, len(a)):
        if a[i] < a[minimum]:
            a[minimum] = a[i]
            print('a[i] {}[{}]'.format(a[i], i))
            print('a[minimum] {}[{}]'.format(a[minimum], minimum))
        for j in range(0, len(a)):
            print('a[i] {}[{}]'.format(a[i], i))
            print('a[j] {}[{}]'.format(a[j], j))
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
        print(a)
    return a