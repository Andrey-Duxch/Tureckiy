num = [int(i) for i in open('input2.txt')]
count = 0
max_sum = float('-inf')
for i in range(len(num) - 1):
    if ((num[i] % 7 == 0 or num[i + 1] % 7 == 0) and str(num[i] + num[i + 1]).endswith('19')):
        count += 1
        max_sum = max(max_sum, num[i] + num[i + 1])
print(count, max_sum)