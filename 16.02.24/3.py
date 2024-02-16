def p(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        return True
    return False
n = int(input("Введите натуральное число:\n"))
if p(n):
    print(f"Число {n} совершенное.")
else:
    print(f"Число {n} не совершеннное.")

