n = int(input("Введите число 0<n<27:"))
k = 0
s = 0
if 0 < n < 27:
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        s = a + b + c
        if s == n:
            k += 1
print(k)
