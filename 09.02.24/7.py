def s(A, B, C):
    ds = abs((A[0] - C[0]) * (B[1] - C[1]) - (A[1] - C[1]) * (B[0] - C[0]))
    if ds == 0:
        return 0
    return ds * 0.5


print(s((0, 0), (0, 5), (5, 0)))
