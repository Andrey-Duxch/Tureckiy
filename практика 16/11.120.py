from random import randint
n = int(input("Введите количество элементов:\n"))
rost = [randint(180, 190) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in rost)}')
B = max(rost)
k = rost.count(B)
print(f"Самый большой рост имеют:", k)