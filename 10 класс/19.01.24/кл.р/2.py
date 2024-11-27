a, b = [int(i) for i in input("Введите два целых числа:\n").split()]
d = a
e = b
c = 0
while b != 0:
    if b > 0:
        c += a
        b -= 1
    else:
        c -= a
        b += 1
print(f"{d} * {e} = {c}")
