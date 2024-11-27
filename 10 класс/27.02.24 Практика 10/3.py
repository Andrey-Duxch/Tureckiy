def bin(a):
    if a > 1:
        bin(a//2)
    print(a % 2, end="")
n = int(input(""))
bin(n)