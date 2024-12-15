file = open('input2.txt')
arr = [int(_) for _ in file]
counter = 0
max_summ = 0
for i in range(len(arr) - 1):
    if (abs(arr[i]) % 7 == 0 or abs(arr[i + 1]) % 7 == 0) and (arr[i] + arr[i + 1]) % 100 == 19:
        counter += 1
        max_summ = max(max_summ, arr[i] + arr[i + 1])
print(counter, max_summ)