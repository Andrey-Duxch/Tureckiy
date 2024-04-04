from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 5) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
min = 0
max = 0
for i in range(1,n):
    if A[i] >= A[max]:
        max = i
    if A[i] <= A[min]:
        min = i
print("Максимальный элемент:", 'A[', max, ']=', A[max])
print("Минимальный элемент:", 'A[', min, ']=', A[min])