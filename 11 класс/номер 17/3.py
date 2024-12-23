num = [int(i) for i in open('input3.txt')]
max_39 = max([x for x in num if 1000 <= abs(x) <= 9999 and str(abs(x)).endswith('39')])
max_392 = max_39**2
count = 0
max_sum = float('-inf')
for i in range(len(num)-1):
    a, b = num[i], num[i + 1]
    digit_4 = (1000 <= abs(a) <= 9999) != (1000 <= abs(b) <= 9999)
    if digit_4 and (a + b)**2 <= max_392:
        count  += 1
        max_sum = max(max_sum, a+b)
print(count, max_sum)