def A(s):
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    b = 0
    d = 0
    for i in s:
        c = r[i]
        if c > d:
            b += c - 2 * d
        else:
            b += c
        d = c
    return b
def B(s):
    import re
    s1 = r'[IVXLCDM]+'
    num = re.findall(s1, s)
    for i in num:
        d = A(i)
        s = s.replace(i, str(d))
    return s
s = input("")
print(B(s))
