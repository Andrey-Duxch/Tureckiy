n = int(input("Введите натуральное число:\n"))
a = ""
while n > 0:
    b = n % 10
    n //= 10
    if a == b:
        print("Да.")
        break
    a = b
else:
    print("Нет.")


