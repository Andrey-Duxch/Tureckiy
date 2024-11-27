def f(n):
    if n == 0:
        return 1
    elif n > 0 and n % 2 != 0:
        return f(n//100) * (n % 10)
    elif n > 0 and n % 2 == 0:
        return f(n//100)
k = 0
for i in range(10**9, 6 * 10**9):
    if f(i) == 21:
        k += 1
        print(f"при{i} = {k}")
print()
