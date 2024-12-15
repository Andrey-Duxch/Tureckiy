def main():
    with open('input10.txt') as f:
        numbers = list(map(int, f.read().strip().split()))
    max_16_0F = float('-inf')
    for num in numbers:
        if hex(num)[-2:] == '0f':
            max_16_0F = max(max_16_0F, num)
    count = 0
    max_sum = float('-inf')
    n = len(numbers)
    for i in range(n - 1):
        a = numbers[i]
        b = numbers[i + 1]
        sum_ab = a + b
        a_7 = (a % 7 == 0)
        b_7 = (b % 7 == 0)
        if (a_7 != b_7) and (sum_ab % max_16_0F == 0):
            count += 1
            max_sum = max(max_sum, sum_ab)
    if count > 0:
        print(count, max_sum)
if __name__ == '__main__':
    main()
