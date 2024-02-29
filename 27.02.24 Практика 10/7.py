def f(n, d=2):
    if n == 1:
        return []
    if n % d == 0:
        return [d] + f(n // d, d)
    else:
        return f(n, d + 1)
n = int(input("Введите натуральное число:\n"))
c = "*".join(map(str, f(n)))
print(f"{n} =", c)
