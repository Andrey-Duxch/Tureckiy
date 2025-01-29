from fnmatch import fnmatch
def div(x):
    return {k for i in range(1, int(x**0.5)+1) if x % i == 0 for k in(i, x // i)}
count = 7
for i in range(1, 10**7 + 1):
    if fnmatch(str(i), "*0??3*"):