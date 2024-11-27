a = int(input("Введите натуральное число:\n"))
s = 0
while a != 0:
    s += a % 10
    a //= 10
print(s)
