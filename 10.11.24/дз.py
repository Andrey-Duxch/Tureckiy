file = open('input.txt.')
count = 0
for string in file:
    a = [int(x) for x in string.split()]
    a_2 = [x for x in a if a.count(x) == 2]
    a_u = [x for x in a if a.count(x) == 1]
    if (len(a_2) == 2 and len(a_u) == 4) and (sum(a_u)/4 <= sum(a_2)/2):
        print(a_2, a_u)
        count+=1
print(count)
file.close()
#наименьший номер строки таблицы: 34