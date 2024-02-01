n = int(input("Введите N:"))
result = []
for i in range(1, n+1):
    a = [int(d) for d in str(i)]
    if all(b != 0 and i % b == 0 for b in a):
        result.append(i)
        print(i, end=" ")



