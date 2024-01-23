n = int(input("Введите натуральное число:\n"))
v = 0
k = [0] * 10
while n > 0:
    a = n % 10
    k[a] += 1
    n //= 10
    if 2 in k:
        v += 1
if v >= 1:
    print("Да.")
else:
    print("Нет.")
