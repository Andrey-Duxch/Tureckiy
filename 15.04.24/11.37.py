from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 10) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
s = []
b = []
for i in range(n):
    if i % 2 == 0:
        s.append(i)
    if i % 10 == 0:
        b.append(i)
print("Четные числа:",*s)
print("Элементы оканчивающиеся 0:",*b)