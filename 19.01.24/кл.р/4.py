a = int(input("Введите натуральное число:"))
s = 0
while a != 0:
    s += a % 10
    a //= 10
print(s)

