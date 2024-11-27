x,d = map(int, input("Введите X и D:\n").split())
print("Массив:")
a =[]
for _ in range(5):
    a.append(x)
    x += d
print(" ".join(str(i) for i in a))
