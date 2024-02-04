m = int(input("Введите значение m: "))
n = int(input("Введите значение n: "))
def a(m, n):
    b = []
    for i in range(1, n):
        s = sum(int(j) for j in str(i))
        if s ** 2 == m:
            b.append(i)
    return b
r = a(m, n)
print("Найденные числа:", r)