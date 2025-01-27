def div(x):
    return sorted ({k for i in range(2, int(x**0.5)+1) if x % i == 0 for k in (i, x//i)})
count = 0
for i in range(250200, 250001 + 1000):
    d = div(i)
    s = max(d) + min(d) if len(d) >0 else 0
    if s % 123 == 17 and s!= 0:
        print(i, s)
        count+=1
    if count == 5:
        break