def A(n):
    sum1 = sum(i for i in n if i > 0)
    sum2 = sum(abs(i) for i in n if i < 0)
    if sum2 == 0:
        return
    b = sum1 / sum2
    return b
N = [1, 2, 3 , 6 , -8, -5, -6]
c = A(N)
print(c)
