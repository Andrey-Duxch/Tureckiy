from random import randint
n = int(input("Введите чётное количество элементов:\n"))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
c = A[0:n//2]
r = A[n//2:]
for i in range(len(c)):
    for j in range(len(c)-2, i-1, -1):
        if c[j] > c[j+1]:
            c[j], c[j+1] = c[j+1], c[j]
for i in range(len(r)):
    nmin = i
    for j in range(i + 1, len(r)):
        if r[j] > r[nmin]:
            nmin = j
    r[i], r[nmin] = r[nmin], r[i]
result = c + r
print("После сортировки:\n", *result)
