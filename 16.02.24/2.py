def tr(a, b, c):
    return a+b >c and a+c > b and b+c >a
def p(a, b, c):
    return a**2=b**2+c**2 or b**2=a**2+c**2 or c**2=b**2+a**2

a, b, c = map(float,input("").split())
if tr(a, b, c)