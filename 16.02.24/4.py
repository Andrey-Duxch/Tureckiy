def p(a, b):
    for i in range(2, min(a, b)+ 1):
        if a % i == 0 and b % i == 0:
            return False
    return True
a,b = map(int,input("Введите 2 натуральных числа:\n").split())
if p(a, b):
    print(f"Числа {a} и {b} взаимно простые.")
else:
    print(f"Числа {a} и {b} не взаимно простые.")
