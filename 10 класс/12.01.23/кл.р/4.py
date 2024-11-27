from random import *
a, b, c = [int(i) for i in input("Введите три целых числа:").split()]
if a > b and a > c:
    print("Максимальное число", a)
elif b > a and b > c:
    print("Максимальное число", b)
elif c > a and c > b:
    print("Максимальное число", c)




