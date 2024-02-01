n = int(input("Сумма количеств цифр от 1 до M:"))
m = 0
s = 0
while s < n:
    m += 1
    s += len(str(m))
print(m)