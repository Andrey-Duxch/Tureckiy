import sys
sys.setrecursionlimit(2026)
def f(n):
    if n < 11:
        return n
    elif n >= 11:
        return n + f(n - 1)
print(f(2024) - f(2021))
