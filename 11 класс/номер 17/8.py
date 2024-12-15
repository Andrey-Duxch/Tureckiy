num = [int(i) for i in open('input8.txt')]
min_2 = min( [x for x in num if 10 <= x <= 99 and x % sum(map(int, str(x))) == 0])
count= 0
max_sum = float('-inf')
for i in range(len(num)- 1):
    a, b = num[i], num[i+ 1]
    if a % min_2==0 or b % min_2 == 0:
        count += 1
        max_sum = max(max_sum, a + b)
print(count, max_sum)