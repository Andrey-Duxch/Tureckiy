from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 5) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
min1 = 0
max1 = 0
for i in range(1, n):
    if A[i] >= A[max1]:
        max1 = i
    if A[i] <= A[min1]:
        min1 = i
print("Максимальный элемент:", 'A[', max1, ']=', A[max1])
print("Минимальный элемент:", 'A[', min1, ']=', A[min1])
