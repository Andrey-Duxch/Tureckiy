def tr(a, b, c):
    return a+c > b and a+b > c and b+c > a
a,b,c = map(float,input("Введите стороны треугольника:\n").split())
if tr(a, b, c):
    print("Треугольник существует")
else:
    print("Треугольник не существует")