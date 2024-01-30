for i in range(100, 1000):
    a = i // 10 % 10
    b = i % 10
    c = i // 100
    if c**3 + a**3 + b**3 == i:
        print(i)
