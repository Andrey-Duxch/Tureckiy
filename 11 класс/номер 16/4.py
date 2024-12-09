from functools import*
c = 0
@lru_cache(None)
def F(n):
    if n >25:
        return 2*n*n*n + 1
    if n<= 25:
        return F(n+2) + 2*F(n+3)

for i in range(1000):
    if F(i)%11 == 0:
        c += 1
print(c)
