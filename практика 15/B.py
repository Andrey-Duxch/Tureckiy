from random import randint
def f(n):
    if n == 1:
         return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Введите количество элементов:"))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив A:\n{" ".join(str(i) for i in A)}')
B = [i for i in A if f(i)]
print(f'Массив A:\n{" ".join(str(i) for i in B)}')
