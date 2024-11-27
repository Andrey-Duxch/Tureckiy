n = int(input())
b = 1
c = 1
for i in range(n - 1):
    if b == 1:
        c += 4
        b = 0
    elif b == 0:
        c += 2
        b = 1
print(c)