def f(n):
    k = 0
    while n > 0:
        b = n % 10
        n = n // 10
        k += b
    return k
print(f(123))
