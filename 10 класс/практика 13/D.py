from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
B = [i for i in A if i % 2 == 0]
print(f'Чётные:{" ".join(str(i) for i in B)}')
print(f'Нeчётные:{" ".join(str(i) for i in A if i % 2 != 0)}')