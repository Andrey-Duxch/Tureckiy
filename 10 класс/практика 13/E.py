from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
result = 0
for i in range(n):
    if i % 2 == 0:
        result += A[i]
    else:
        result -= A[i]
print("Знакопеременная сумма:", result)
