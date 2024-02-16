def tr(a, b, c):
    return a+c > b and a+b > c and b+c > a
a,b,c = map(float,input("Введите стороны треугольника:\n").split())
if tr(a, b, c):
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("Треугольник прямоугольный")
    else:
        print("Прямоугольник не прямоугольный")
else:
    print("Треугольник не существует")
