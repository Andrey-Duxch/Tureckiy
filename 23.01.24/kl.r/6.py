a = int(input())
b = int(input())
q = int(input())
if q > 0:
    a, b = min(a, b), max(a, b) + 1
else:
    b, a = min(a, b) - 1, max(a, b)
for x in range(a, b, q):
    print(x)