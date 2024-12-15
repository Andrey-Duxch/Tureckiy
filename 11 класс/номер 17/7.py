with open('input7.txt') as f:
    numbers = list(map(int, f.read().strip().split()))
max_1 = max((num for num in numbers if num % 10 == 1))
count = 0
min_sum= float(10000000)
for i in range(len(numbers) - 3):
    num = numbers[i:i + 4]
    count_even = sum(1 for x in num if x % 2 == 0)
    if count_even % 2 == 1 and all(x < max_1 for x in num):
        count += 1
        min_sum = min(min_sum, sum(num))
if count > 0:
    print(count, min_sum)
