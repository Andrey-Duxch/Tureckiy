def f(n):
    if n < 2:
        return n
    elif n >= 2:
        return f(n//2) + f(n % 2)
k = 0
for i in range(2**0, 2**10):
    if f(i) == 27:
        k += 1
        print(f"при{i} = {f(i)}")
print(k)
