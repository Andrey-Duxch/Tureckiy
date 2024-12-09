from functools import*
c = 0
@lru_cache(None)
def F(n):
    if n <= 15:
        return n*n +11
    if n > 15 and n % 2 ==0:
        return F(n//2) + n*n*n - 5*n
    if n>15 and n% 2 !=0:
        return F(n-1) + 2*n +3

for i in range(1000):
    if str(F(i)).count('6') >= 3:
        c += 1
print(c)