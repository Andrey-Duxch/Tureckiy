def squared(a, b, k):
    n = 1
    for i in range(a, b+1):
        if i**2 % k != 0:
            print(f"{i**2:<4}", end=" ")
        n += 1
        if n > 10:
            n = 1
            print()

squared(4,33,9)
