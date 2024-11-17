n = int(input())
c = 0
while n != 0:
    d = n % 10
    if d == 0:
        d =(n // 10) % 10
    n -= d
    c += 1
print(c)