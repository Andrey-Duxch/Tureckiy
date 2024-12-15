num = [int(i) for i in open('input5.txt')]
min_1 = (min([i for i in num]))
num_output = [(num[i], num[i+1]) for i in range(0, len(num) - 1) if num[i] % 16 == min_1 or num[i+1] %16 == min_1]
max_sum = max(sum(x) for x in num_output)
print(len(num_output), max_sum)