def a(n):
    k = 0
    while n > 0:
        b = n % 10
        n = n // 10
        k += b
    return k
n = int(input("Введите первое натуральное число:"))
c = int(input("Введите первое натуральное число:"))
if a(n) > a(c):
    print(f"Сумма цифр числа {n} больше суммы цифр числа {c}")
elif a(c) > a(n):
    print(f"Сумма цифр числа {c} больше суммы цифр числа {n}")
else:
    print(f"Сумма цифр числа {c} равна сумме цифр числа {n}")
