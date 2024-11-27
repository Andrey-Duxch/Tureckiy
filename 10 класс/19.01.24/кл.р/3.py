n = int(input("Введите число N:\n"))
s = 0
b = 1
c = 0
while b < n:
    b = c + b
    c = b - c
    s += c
if n == 0:
    print("введена цифра 0")
elif n < 0:
    print("Введено число меньше нуля")
else:
    print("Сумма", s)
