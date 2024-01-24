n = int(input("Введите натуральное число:"))
p = int(input())
s = 0
for i in range(n):
    bi = int(input("" + str(i + 1) ))
    s += bi
if s < p:
    print("Верно")
else:
    print("неверно")

