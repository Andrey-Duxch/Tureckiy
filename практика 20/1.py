l =set()
for n in range(3,1000):
    s = '1' + '2' * n
    while '12' in s or '332' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
    l.add(len(s))
    print(l)

