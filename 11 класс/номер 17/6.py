num = [int(i) for i in open('input6.txt')]
max_4_7 = max([x for x in num if 1000 <= abs(x) <= 9999 and abs(x) % 10 == 7], default=float('-inf'))
count = 0
max_sum = float('-inf')
for i in range(len(num) - 2):
    a, b, c = num[i], num[i+ 1], num[i+ 2]
    end_7= sum(1 for x in [a, b, c] if 1000 <= abs(x) <= 9999 and abs(x) % 10 == 7)
    if end_7 >= 2 and (a + b + c) > max_4_7:
        count += 1
        max_sum = max(max_sum,a+b+c)
print(count, max_sum)