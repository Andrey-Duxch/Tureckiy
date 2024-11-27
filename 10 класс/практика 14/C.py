from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 5) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
s = []
for i in A:
    if A.count(i) > 1 and i not in s:
        s.append(i)
if s:
    print("Есть:", ", ".join(str(i) for i in s))
else:
    print("Нет")
