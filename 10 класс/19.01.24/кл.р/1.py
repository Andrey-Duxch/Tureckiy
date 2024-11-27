a, b = [int(i) for i in input("Введите два целых числа:\n").split()]
while a <= b:
    print(f"{a} * {a} = {a*a}")
    a += 1
