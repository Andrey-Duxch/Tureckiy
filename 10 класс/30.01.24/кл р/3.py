n = int(input("Введите N:"))
for i in range(1, n+1):
    a = i
    while a > 0:
        b = a % 10
        a //= 10
        if b == 0 or i % b != 0:
            break
    else:
        print(i, end=" ")



