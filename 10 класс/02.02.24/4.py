def equation(x1, y2):
    x1, y1 = map(float, x1.split(";"))
    x2, y2 = map(float, y2.split(";"))
    k =(y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(k, b)

equation("0;0", "1;1")