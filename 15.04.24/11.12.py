a = []
b = 300
while len(a) != 21:
    b += 1
    if b % 13 == 0 or b % 17 == 0:
        a.append(b)
    else:
        pass
print(*a)