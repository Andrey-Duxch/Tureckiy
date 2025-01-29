from fnmatch import fnmatch
def div(x):
    return {k for i in range(1, int(x**0.5)+1) if x % i == 0 for k in(i, x // i)}
count = 7
for i in range(1, 10**7 + 1):
    if fnmatch(str(i), "?6*6*?6"):
        d = div(i)
        if i% 6 == 0 and i% 7 == 0 and i%8 == 0:
            print(i, sum(x for x in d))
            count -= 1
        if count == 0:
            break