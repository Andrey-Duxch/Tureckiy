def a(n):
    k = 0
    while n > 0:
        b = n % 10
        n = n // 10
        k += b
    return k
n = int(input("Напишите число:"))
print(f"Сумма цифр {n} = {a(n)}")
