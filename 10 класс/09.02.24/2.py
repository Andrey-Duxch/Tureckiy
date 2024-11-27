import math
def a(n):
    if n == 2 or n == 3:
        return "Простое"
    if n <= 1 or n % 2 == 0:
        return "Составное"
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return "Составное"
    return "Простое"
for i in range(1,10000):
    print(f"{i} - {a(i)}")

