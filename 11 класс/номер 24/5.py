s = open('5.txt').readline()
l = 0
m = 0
for r in range(1,len(s)):
    if s[r-1]+s[r] in 'PP':
        l = r
    else:
        m = max(m, r - l +1)
print(m)