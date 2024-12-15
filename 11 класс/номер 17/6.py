num = [int(i) for i in open('input6.txt')]
max_1 = max([i for i in num if abs(i) % 10 == 7])
num_output = [(num[i], num[i+1],num[i+2]) for i in range(0, len(num) - 2) if [len(str(abs(num[i]))), len(str(abs(num[i+1]))),len(str(abs(num[i+1])))].count(4) >=2 and (num[i] % 10 == 7 or num[i+1]%10 == 7 or num[i+2] %10 == 7)and sum((num[i], num[i+1], num [i+2])) > max_1]
max_sum = max(sum(x) for x in num_output)
print(len(num_output), max_sum)
