from random import randint
n = int(input("Введите количество элементов:"))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив A:\n{" ".join(str(i) for i in A)}')
buf1 = A[0]
for i in range(n - 1):
    buf2 = A [i + 1]
    A [i + 1] = buf1
    buf1 = buf2
A[0] = buf2
print(f'Результат:\n{" ".join(str(i) for i in A)}')
