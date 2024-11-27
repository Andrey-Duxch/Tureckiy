def s(A, B, C):
    ds = abs((A[0] - C[0]) * (B[1] - C[1]) - (A[1] - C[1]) * (B[0] - C[0]))
    if ds == 0:
        return 0
    return ds * 0.5
x1, y1 = map(float, input("x1, y1 ="). split())
x2, y2 = map(float, input("x2, y2 ="). split())
x3, y3 = map(float, input("x3, y3 ="). split())
x4, y4 = map(float, input("x4, y4 = "). split())
x5, y5 = map(float, input("x5, y5 ="). split())
n = s((x1, y1),(x2, y2), (x5, y5)) + s((x2, y2), (x5, y5), (x4, y4)) + s((x2, y2), (x3, y3),(x4, y4))
print("Площадь пятиугольника =", n)