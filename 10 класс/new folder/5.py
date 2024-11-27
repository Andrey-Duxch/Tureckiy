def subtract_last_digit(n):
    count = 0
    while n != 0:
        last_digit = n % 10
        if last_digit != 0:
            n -= last_digit
        else:
            n //= 10
        count += 1
    return count

number = int(input())
count_subtractions = subtract_last_digit(number)
print(count_subtractions)