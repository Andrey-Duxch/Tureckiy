a = int(input("Напишите число"))
k = 0
while a != 0:
    b = a%10
    a //= 10
    k += 1
print(k)
