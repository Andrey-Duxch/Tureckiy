a, b = [int (i) for i in input("Введите два целых числа").split()]
while a < b:
    print(f"{a} * {a} = {a*a}")
    a += 1
print(f"{a} * {a} = {b*b}")



