from random import randint
n = int(input("Введите n:\n"))
c = []
while len(c) < n:
    b = randint(1, n)
    if b not in c:
        c.append(b)
print(" ".join(str(i) for i in c))