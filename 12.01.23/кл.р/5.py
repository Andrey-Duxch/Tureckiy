a, b, c, d, e = [int(i) for i in input("Введите пять целых чисел:").split()]
if a > b and a > c and a > d and a > e:
    print("Максимальное число", a)
elif b > a and b > c and b > d and b > e:
    print("Максимальное число", b)
elif c > a and c > b and c > d and c > e:
    print("Максимальное число", c)
elif d > a and d > b and d > c and d > e:
    print("Максимальное число", d)
else:
    print(e)


