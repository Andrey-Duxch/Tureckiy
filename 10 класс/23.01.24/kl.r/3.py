n = int(input("Введите N:"))
for i in range(1, n+1):
    b = 1
    while i >= b:
        b = b * 10
        if i * i % b == i:
            print(f'{i} * {i} =', i * i)
