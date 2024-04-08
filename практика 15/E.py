from random import randint
n = int(input("Введите чётное количество элементов:"))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив A:\n{" ".join(str(i) for i in A)}')
k = list(reversed(A[0:n//2])) + list(reversed(A[n//2:]))
print("Результат:", *k)
