file = open('input.txt')
count = 0
for string in file:
    a = sorted(int(x) for x in string.split())

    a_2 = [x for x in a if a.count(x) == 2]
    a_u = [x for x in a if a.count(x) == 1]
    if (len(a_2) == 2 and len(a_u) == 3) and ((a[0]+a[4])**2 < (a[1]**2 + a[2]**2 + a[3]**2)):
        print(a_2, a_u)
        count += 1
print(count)
file.close()