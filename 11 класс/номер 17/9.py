num = [int(i) for i in open('input9.txt')]
max_8 = max([x for x in num if str(abs(x)).startswith('8')])
count = 0
min_sum = float('inf')
for i in range(len(num)-2):
    a, b, c = num[i], num[i+ 1], num[i + 2]
    starts_6 = sum(1 for x in [a, b, c] if str(abs(x)).startswith('6'))
    if starts_6 <= 1 and (a + b + c) >= max_8:
        count += 1
        min_sum = min(min_sum, a + b + c)
print(count, min_sum)