def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f(n//8) + n % 8
    elif n > 0 and n % 2 != 0:
        return f(n//8)
k = 0
for i in range(8**8, 8**9+1):
    if f(i) == 2:
        k += 1
print(k)
