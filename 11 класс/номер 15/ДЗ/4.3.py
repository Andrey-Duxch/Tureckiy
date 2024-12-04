def f(x):
    return (x in A)<= (not x in P) and ((not x in Q) <= (not x in A))
P = {2,4,6,8,10,12,14,16,18,20}
Q = {3,6,9,12,15,18,21,24,27,30}
A = set(range(-100,10000))
for x in range(-100,10000):
    if f(x) == 0:
        A.remove(x)
print(len(A),A)