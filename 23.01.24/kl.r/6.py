a = int(input("Введите начало отрезка:"))
b = int(input("Введите конец отрезка:"))
q = int(input("Введите шаг:"))

if q > 0:
    a, b = min(a, b), max(a, b) + 1
else:
    b, a = min(a, b) - 1, max(a, b)
for x in range(a, b, q):
    y = x**3 + 2*x**2 - 4*x + 1
    print(f"В точке {x} функция равна {y}")
