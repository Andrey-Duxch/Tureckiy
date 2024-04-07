from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 5) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
s = []
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] == A[j] and A[i] not in s:
            s.append(A[i])
if s:
    print("Есть:", ", ".join(str(i) for i in s))
else:
    print("Нет")
