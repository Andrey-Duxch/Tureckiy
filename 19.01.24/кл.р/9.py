x = float(input("Введите сумму вклада:"))
p = float(input("Введите процент вклада:"))
y = float(input("Введите желаемую сумму:"))
c = 0
while x < y:
    x = x * (1 + p / 100)
    x = int(100*x)/100
    c += 1
print(c)
