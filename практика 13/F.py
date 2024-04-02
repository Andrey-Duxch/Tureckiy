from random import randint
n = int(input("Введите количество элементов:\n "))
A = [randint(0,100) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
s1 = sum(i for i in A if i < 170)
count1 = sum(1 for i in A if i < 170)
s2 = sum(i for i in A if i >= 170)
count2 = sum(1 for i in A if i >= 170)
sr1 = None if count1 == 0 else
sr2 = None if count2 == 0 else print(sr2)
print(f'Среднее арифметическое элементов [0,50):{sr1}')
print(f'Среднее арифметическое элементов [50,100]:{sr2}')