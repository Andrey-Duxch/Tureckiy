def A(n):
    s = [i for i, b in enumerate(n) if str(b)[-1] == "0"]
    return s
B = [2, 4, 8, 9 ,20, 10]
r = A(B)
print("индекс элементов оканчивающихс на 0:", *r)