def f(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a, b = [int(i) for i in input("Введите два натуральных числа:\n").split()]
print(f"НОД({a}, {b}) = {f(a,b)}.")