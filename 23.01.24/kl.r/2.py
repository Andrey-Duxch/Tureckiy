n = int(input())
for i in range(100,1000):
    a = i // 10 % 10
    b = i % 10
    c = i // 100
    if c**n + a**n + b**n == i:
        print(i)
