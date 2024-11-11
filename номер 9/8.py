file = open('input.txt')
count = 0
for string in file:
    a = [int(x) for x in string.split()]
    a_3 = [x for x in a if a.count(x) == 3]
    a_u = [x for x in a if a.count(x) == 1]
    if (len(a_3) == 3 and len(a_u) ==3) and (((sum(a_3))**2) > ((sum(a_u))**2)):
        print(a_3,a_u)
        count+=1
    print(count)
