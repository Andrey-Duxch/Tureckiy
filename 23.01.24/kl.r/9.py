n = int(input("Введите натуральное число:"))
p = int(input("Введите целое число:"))
s = 0
for i in range(n):
    bi = int(input("Введите целое число b" + str(i + 1) + ":"))
    s += bi
if s < p:
    print("Верно")
else:
    print("Неверно")
