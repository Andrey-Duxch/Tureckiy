num = [int(i) for i in open('input3.txt')]
max_39 = (max([i for i in num if abs(i) % 100 == 39]))**2
print(max_39)
num_output = [(num[i], num[i+1]) for i in range(0, len(num) - 1) if [len(str(abs(num[i]))), len(str(abs(num[i+1])))].count(4) == 1 and (sum((num[i], num[i+1])))**2 <= max_39]
max_sum = max(sum(x) for x in num_output)
print(len(num_output), max_sum)