def m(a,b):
    if b == 0:
        return a
    return m(b, a % b)
a,b = map(int, input("").split())
print(f"НОД({a},{b}) = {m(a,b)}")