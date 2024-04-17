from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 10) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
B = sorted(A)
print("После сортировки:\n", *B)
s = []
k = 0
for i in A:
    if i not in s:
        s.append(i)
        k += 1
print("Различных чисел:", k)
