from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
s = 0 if n == 0 else sum(i for i in A)/n
print(f'Среднее арифметическое {s}')
