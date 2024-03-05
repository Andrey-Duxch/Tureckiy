import sys
sys.setrecursionlimit(120)
def G(n):
    if n < 10:
        return n
    elif n >= 10:
        return G(n - 2)+1
def f(n):
    return G(n-1)
c = 0
for n in range(1, 101):
    for j in range(1, 11):
        if f(n) == j**2:
            c += 1
print(c)
