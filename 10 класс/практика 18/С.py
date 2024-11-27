s = input()
list_dig = []
list_zn = []
p = 0
for i in range(len(s)):
    if not (s[i].isdigit()):
        list_dig.append(int(s[p:i]))
        p = i + 1
        list_zn.append(s[i])
list_dig.append(int(s[p:]))

while '*' in list_zn or '/' in list_zn:
    pdiv = list_zn.index('/') if '/' in list_zn else len(list_zn) + 100
    pmul = list_zn.index('*') if '*' in list_zn else len(list_zn) + 100
    if pdiv < pmul:
        list_dig[pdiv] = list_dig[pdiv]/list_dig[pdiv+1]
        k = list_dig.pop(pdiv+1)
        k = list_zn.pop(list_zn.index('/'))
    else:
        list_dig[pmul] = list_dig[pmul] * list_dig[pmul + 1]
        k = list_dig.pop(pmul+1)
        k = list_zn.pop(list_zn.index('*'))

for i in list_zn:
    if i =='+':
        list_dig[0] = list_dig[0] + list_dig[1]
        k = list_dig.pop(1)
    else:
        list_dig[0] = list_dig[0] - list_dig[1]
        k = list_dig.pop(1)
print(*list_dig)
