def a(n):
    while n > 0:
        if n - 1000 >= 0:
            print("M", end="")
            n -= 1000
        elif - 100 <= (n - 1000) < 0:
            print("CM", end="")
            n -= 900
        elif n - 500 >= 0:
            print("D", end="")
            n -= 500
        elif -100 <= (n - 500) < 0:
            print("CD", end="")
            n -= 400
        elif n - 100 >= 0:
            print("C", end="")
            n -= 100
        elif -10 <= (n - 100) < 0:
            print("XC", end="")
            n -= 90
        elif n - 50 >= 0:
            print("L", end="")
            n -= 50
        elif -10 <= (n - 50) < 0:
            print("XL", end="")
            n -= 40
        elif n - 10 >= 0:
            print("X", end="")
            n -= 10
        elif  n - 10 == -1:
            print("IX", end="")
            n -= 9
        elif n - 5 >= 0:
            print("V", end="")
            n -= 5
        elif  n - 5 == -1:
            print("IV", end="")
            n -= 4
        elif n - 1 >= 0:
            print("I", end="")
            n -= 1
n = int(input("Введите натуральное число:\n"))
a(n)