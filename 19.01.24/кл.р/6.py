n = int(input("Введите натуральное число:"))
k = [0] * 10
while n > 0:
    a = n % 10
    k[a] += 1
    print(k)
    n //= 10
if 2 in k:
    print("Да.")
else:
    print("Нет.")
