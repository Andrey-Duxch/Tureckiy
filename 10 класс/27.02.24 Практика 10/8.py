def f(n, d=1):
    if n == 0:
        return 1
    b = 0
    for i in range(d, n + 1):
        b += f(n-i, i)
    return b
n = int(input("Введите натуральное число:\n"))
print("Количество разложений:", f(n)-1)
