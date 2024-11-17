def count_sub(n):
    count = 0
    while n > 0:
        last_d = n % 10
        if last_d == 0:
            n = n - int(str(n)[0:1:])
        n -= last_d
        count += 1
    return count
numb = int(input(''))
print(count_sub(numb))
