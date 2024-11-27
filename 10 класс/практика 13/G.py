from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(50, 120) for _ in range(n)]
print(f'Масса:\n{" ".join(str(i) for i in A)}')
mass1 = sum(i for i in A if i > 100)
count1 = sum(1 for i in A if i > 100)
mass2 = sum(i for i in A if i <= 100)
count2 = sum(1 for i in A if i <= 100)
srmass1 = mass1 / count1
srmass2 = mass2 / count2
print(f"Средняя масса полных людей: {srmass1}")
print(f"Средняя масса остальных людей: {srmass2}")
