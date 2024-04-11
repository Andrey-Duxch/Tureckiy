from random import randint
n = 22
a = [randint (-170, 170) for i in range(n)]
print(*a)
B =[]
C = []
for i in range(22):
    if a[i] >= 0:
        B.append(a[i])
    else:
        C.append(a[i])
M = sum(i for i in B)
D = sum(i for i in C)
print(f"Средний рост девочек:{M/len(B)}")
print(f"Средний рост мальчиков:{-1*(D/len(C))}")
