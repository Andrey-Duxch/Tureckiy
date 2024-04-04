from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 5) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
s = []
for i in range(n-1):
