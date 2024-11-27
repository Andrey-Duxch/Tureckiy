from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(120, 190) for _ in range(n)]
print(f'Рост:\n{" ".join(str(i) for i in A)}')
count = sum(1 for i in A if i >= 170)
print(f"Рост больше 170 сантиметров имеют {count} учеников.")
if count >= 5:
    print("Можно сформировать баскетбольную команду.")
else:
    print("Нельзя сформировать баскетбольную команду.")
