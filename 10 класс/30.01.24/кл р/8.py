for i in range(10000):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s > i:
        a = 0
        for k in range(1, s):
            if s % k == 0:
                a += k
        if a == i:
            print(i, s)
