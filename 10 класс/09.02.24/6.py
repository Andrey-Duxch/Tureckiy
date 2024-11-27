def a(n):
    r = 0
    while n != 0:
        b = n % 10
        r = r*10 + b
        n = n//10
    return r
n = int(input("Введите натуральное число:\n"))
print(f"После переворота {a(n)}")
