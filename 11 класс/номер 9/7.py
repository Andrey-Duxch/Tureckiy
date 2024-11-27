file = open('input.txt')
count = 0
for string in file:
    a = sorted(int(x) for x in string.split())
    a_3 = [x for x in a if x % 3 ==0]
    if len(a_3) == 3 and ((a[5]-a[0]) <= sum(a_3)):
        print(a_3)
        count+=1
print(count)