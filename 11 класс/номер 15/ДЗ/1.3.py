def DEL(x,a):
    return ((x%33 == 0) <= ((x%a != 0)) <= (x%242 !=0))
for a in range(1,10000):
    if all(DEL(x,a) == 1 for x in range(1,726)):
        print(a)

