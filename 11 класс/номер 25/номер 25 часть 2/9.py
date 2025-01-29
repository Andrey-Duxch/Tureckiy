from fnmatch import fnmatch
def div(x):
    return {k for i in range(1, int(x**0.5)+1) if x % i == 0 for k in(i, x // i)}
count = 7
for i in range(0, 10**7 + 1, 217):
    if fnmatch(str(i), "14?4*"):
        d = div(i)
        print(i, sum(x for x in d if x%2 != 0))