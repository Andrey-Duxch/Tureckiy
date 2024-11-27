def revers_dig(a):
    if a > 0:
        print(a%10)
        revers_dig(a//10)
n = int(input(""))
revers_dig(n)