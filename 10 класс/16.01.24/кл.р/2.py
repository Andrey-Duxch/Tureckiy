a, b, c = [int(i) for i in input(f"Введите три числа:\n").split()]
if a == b == c:
    print("Все числа одинаковые")
elif a == b or b == c or a == c:
    print("Два числа одинаковые")
elif a != b and b != c and c!= a:
    print("нет одинаковых чисел")